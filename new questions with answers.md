# Celery

### What is the difference between delay() and apply_async()?

      "Delay is a shortcut method of apply_async. Both methods are used to send tasks to the Celery broker. Delay accepts task arguments, whereas apply_async provides additional execution configurations such as countdown, ETA, queue, priority and expiration. I would use delay for simple task execution and apply_async when I need scheduling, routing or other execution controls."

      Arguments i can pass to apply_async:
        ETA, countdown, expires, queue

    countdown - specifies how many seconds Celery should wait before executing a task.
    expires - specifies the maximum time a task is allowed to wait before it becomes invalid.
    ETA - another execution scheduling option.
    Instead of specifying the number of seconds to wait, you specify the exact date and time.

    Note:
    Countdown and ETA determine when a task becomes eligible for execution. They do not guarantee that execution starts at that exact time. Worker availability and queue congestion can introduce delays.

    Example:
        task.apply_async(
            countdown=60,
            expires=300
        )
    countdown-
    Celery waits for 60 seconds.
    After 60 seconds, the task becomes eligible for execution.
    Suppose a user registers on your application. You want to send a welcome email after 1 minutes.

    Expires -
    It expires 300 seconds after being scheduled.
    If a worker hasn't started executing it by then, it is discarded as expired.
    An OTP is valid for only 2 minutes. Sending that OTP after 2 minutes is useless.

    1.Question:
    The task becomes eligible at 10:01 AM.
    However, your Celery worker is busy processing other tasks and picks up this task only at 10:04 AM.
    Will the task execute or be discarded? Why?
    Ans:
        The worker picks up the task at 10:04 AM, which is before its expiration time of 10:05 AM.
        Therefore, the task can execute successfully.
        If the worker picked it up at 10:06 AM, it would be expired and discarded.

    2.Question:
    Suppose a task starts executing at 10:04 AM, The task takes 10 minutes to complete. Will Celery terminate the task at 10:05 AM because its expiration time has passed, or will it allow the task to finish?
    Ans:
        Celery will not terminate an already-running task just because its expiration time has passed.
        expires controls how long a task remains valid while waiting to be executed. It is not a timeout for task execution.

    Difference between expires, soft_time_limit, hard_time_limit
    1. expires
        Controls how long a task remains valid while waiting to start execution.
        - If the worker hasn't started the task before its expiration deadline, the task is discarded.
        - It does not terminate an already-running task.
    2. soft_time_limit
        Controls the maximum execution time before Celery raises a SoftTimeLimitExceeded exception.
        - The task is already running.
        - Celery raises an exception when the soft limit is reached.
        - You can catch the exception and perform cleanup operations.
        Code:
            from celery.exceptions import SoftTimeLimitExceeded
            @app.task(soft_time_limit=60)
            def generate_report():
                try:
                    # Long-running operation
                    process_records()
                except SoftTimeLimitExceeded:
                    print("Task execution time exceeded")
                    # Perform cleanup
    3. time_limit
        Controls the hard execution time limit.
        - If the task exceeds this limit, the worker forcibly terminates the task process.
        - Normal cleanup code is not guaranteed to execute.
        Code:
            @app.task(time_limit=120)
            def generate_report():
                process_records()

    Both delay() and apply_async executes tasks asyncronously, requires celery brokers.
    apply()
    Unlike delay() and apply_async():
        - It does not send a message to the broker.
        - It does not require a worker to execute the task.
        - It executes immediately in the current process.
        - It returns an EagerResult.
    Can be mostly used in testing since we dont need celery workers, celery brokers.

    Code:
        result = send_email.apply(args=["test@gmail.com"])
        print(result.successful())
        print(result.get())

    1.Question:
        will successful and get are executed
        @app.task
        def add(a, b):
            return a + b

        result = add.apply(args=[10, 20])

        print(result.successful())  # True
        print(result.get())

### celery result analysis

    Code:
        result = add.delay(10, 20)

        print(result.id)
        print(result.status)
        print(result.ready())
        print(result.successful())
        what is the output

        Ans:
            result.id = uuid
            status = PENDING - Task hasn't started; it may also mean the state is unknown
            ready() = False - Task hasn't finished
            successful() = False - Task hasn't completed successfully

            Note:
            - ready() checks whether the task has finished execution, regardless of success or failure.
            - successful() checks whether the task finished successfully.

    Lifecycle:
    Pending - Task is waiting for execution or its state is unknown
    STARTED - Worker has started executing the task (when task-start tracking is enabled).
    SUCCESS - Task completed successfully.
    FAILURE - Task execution failed.

    Question:
        1.Suppose the task has started executing, but it hasn't finished yet.
        What will these return?
        Ans:
            result.status - Started
            result.ready() - False
            result.successful() - False

            status: Returns STARTED because the worker has begun executing the task (assuming task-start tracking is enabled else Pending).
            ready(): Returns False because execution hasn't finished.
            successful(): Returns False because the task hasn't completed successfully yet.

        2.The task has finished execution, but it encountered an exception.
        Ans:
            status → FAILURE: Task execution failed.
            ready() → True: Task execution is finished, regardless of outcome.
            successful() → False: Task did not complete successfully.
            failed() → True: Task execution resulted in failure.
            result.get() -> it raises the original ZeroDivisionError by default because propagate=True is the default.
            if propagate is False -> This returns the exception object instead of raising it.

### Celery Retry

        Feature	                self.retry()	    autoretry_for
    Retry decision	            Developer	        Celery
    Manual control	            Yes	                Limited
    Exception handling	        Explicit	    Configured exceptions
    Custom countdown	        Yes	            Yes, through retry options
    Conditional retry	        Yes	                Not directly
    Best for	        Complex retry logic	    Simple retry logic

    1. Using self.retry()
        You can manually retry a task when a specific exception occurs.
        Code:
            from celery import Task
            from celery.exceptions import Retry

            @app.task(bind=True, max_retries=3)
            def process_payment(self, payment_id):
                try:
                    response = payment_gateway.charge(payment_id)
                    return response

                except TemporaryGatewayError as exc:
                    raise self.retry(
                        exc=exc,
                        countdown=5
                    )
        bind=True gives access to the task instance through self
        max_retries=3 allows up to three retries after the initial attempt.
        countdown=5 waits five seconds before retrying.
        exc=exc preserves the original exception information.

    2. Using autoretry_for
        Celery can automatically retry specified exceptions without manually writing self.retry().
        Code:
            @app.task(
                autoretry_for=(TemporaryGatewayError,),
                retry_kwargs={'max_retries': 3},
                retry_backoff=True
            )
            def process_payment(payment_id):
                response = payment_gateway.charge(payment_id)
                return response

        autoretry_for specifies which exceptions trigger retries.
        max_retries=3 allows three retries.
        retry_backoff=True enables exponential backoff.(detailed explanation at point 4)

    3.Code for self.retry()
        A payment gateway can give 503-service unavailable retry it, 429-too many requests try after some time, 400 - bad request dont try, 402- payment declined dont try
        Code:
            @app.task(bind=True, max_retries=3)
            def process_payment(self, payment_id):
                try:
                    response = payment_gateway.charge(payment_id)

                    if response.status_code == 503:
                        raise TemporaryGatewayError()

                    if response.status_code == 429:
                        retry_after = int(
                            response.headers.get("Retry-After", 30)
                        )
                        raise RateLimitError(retry_after)

                    if response.status_code == 400:
                        raise ValueError("Invalid payment request")

                    if response.status_code == 402:
                        raise ValueError("Payment declined")

                    return response.json()

                except TemporaryGatewayError as exc:
                    raise self.retry(exc=exc, countdown=30)

                except RateLimitError as exc:
                    raise self.retry(
                        exc=exc,
                        countdown=exc.args[0]
                    )
    4.autoretry()
        Code:
            @app.task(
                autoretry_for=(ConnectionError,),
                retry_kwargs={'max_retries': 5},
                retry_backoff=True
            )
            def fetch_external_data():
                return external_api.fetch()
        retry_backoff=True means Celery automatically calculates the increasing retry delays. with 2**n starts at 0,1,2,4,8,16...

        if the retry_backoff = 10
        Here, the base delay is 10 seconds, so the approximate sequence is:
        10 → 20 → 40 → 80 → 160 seconds.

        Why is exponential backoff useful?
            Imagine your application sends requests to a payment gateway, and the gateway is temporarily down.

            If 1,000 Celery tasks retry every second, the gateway receives another 1,000 requests every second.

            This can worsen the outage.

            With exponential backoff:
            - Retry requests become less frequent.
            - The external service gets time to recover.
            - Your application avoids continuously overwhelming the service.

        "Exponential backoff is a retry strategy in which the waiting time between retries increases exponentially. It helps prevent overwhelming an external service during temporary failures. In Celery, we can enable it using retry_backoff=True with autoretry_for."

    5.Question
        Suppose:
            @app.task(
                autoretry_for=(ConnectionError,),
                retry_kwargs={'max_retries': 4},
                retry_backoff=True
            )
            If the initial task execution fails with ConnectionError, how many total execution attempts are possible?
            Ans:
                Initial execution: 1 attempt
                Maximum retries: 4 attempts
                Total possible executions: 5
                max_retries=4 means four additional attempts, not four attempts in total.

### acks_late True/False

    When a Celery worker receives a task from the message broker (Redis/RabbitMQ), it needs to inform the broker whether it has accepted responsibility for that task.
    There are two important concepts:
        - ACK: Worker tells the broker that the task has been acknowledged.
        - NACK / requeue: Worker indicates that the message should not be considered successfully handled and may be delivered again, depending on broker and configuration.
    Two strategies:
    1.Early acknowledgement (default):
    Flow:
        Broker sends task to worker.
        Worker acknowledges the task.
        Worker starts executing the task.
        Worker crashes unexpectedly.
    The broker has already received the ACK, so it generally won't redeliver that task.
    2.Late acknowledgement:
        @app.task(acks_late=True)
        Flow:
            Broker sends task to worker.
            Worker starts executing the task.
            Worker crashes before acknowledging.
            Broker may redeliver the unacknowledged task.
        The task can be delivered again instead of being lost.
        With late acknowledgement, a task might execute more than once. Therefore, your task should ideally be idempotent.
    Note:
    Late acknowledgement provides at-least-once delivery semantics, not exactly-once execution.

    Celery has task_reject_on_worker_lost, which affects whether a task is requeued when its worker process is abruptly lost. Late acknowledgement alone does not guarantee redelivery in every worker-crash scenario.

    Questions:
    1.Scenario:
    You have a Django application that generates Excel reports containing 1 million records.
    A Celery worker picks up the task and starts processing 600,000 records.
    Suddenly, the worker crashes because of an out-of-memory error.
    Assume the broker is Redis.
        Q1: If you're using the default early acknowledgement (acks_late=False), what happens to the task?
        Ans:
            "When acks_late=False, Celery acknowledges the task as soon as the worker receives it, before executing it. If the worker crashes during execution, the broker has already received the acknowledgement. Therefore, the task generally won't be redelivered, and the task may be lost."

        Q2: If changed config to acks_late=True, will the next worker start processing from 600,001
        Ans:
            Worker receives the task.
            Worker starts execution.
            Worker processes 600,000 records.
            Worker crashes.
            The task hasn't been acknowledged.
            The broker can redeliver it to another worker.

            Will processing resume from record 600,001?
            No. Celery doesn't automatically remember the progress of your Python function.
            If the worker crashes after processing 600,000 records, the new worker starts the loop again.
    2.Scenario:
    Your Celery worker processes a payment successfully.
    The payment gateway charges the customer ₹5,000.
    Before Celery acknowledges the task, the worker crashes.
    The broker redelivers the task to another worker.
        Q1:How would you prevent the customer from being charged twice?
        Ans:
            Late acknowledgement – helps prevent task loss.
            Idempotency – prevents duplicate business operations.

            Don't rely only on the database status check. There is a possible crash window:
            Payment gateway charges the customer.
            Worker crashes before updating PostgreSQL to SUCCESS.
            Another worker receives the task.
            Database still says PENDING.

            The second worker might charge again.
            That's why you should also send the same idempotency key to the payment gateway, assuming the gateway supports idempotency.

            Also use database transactions and appropriate locking or conditional updates to protect concurrent processing.

        Q2: Why do we use task_reject_on_worker_lost=True
        Ans:
            "acks_late=True delays acknowledgement until task execution finishes. However, Celery may acknowledge a task when its worker child process is abruptly lost. reject_on_worker_lost=True changes this behavior so the task can be requeued and delivered to another worker."

            One caution: Repeated worker crashes can cause a task to be delivered repeatedly, potentially creating a message loop. Use retry limits, monitoring and idempotent task implementations.

### Concurrency and prefetch_multiplier

    celery -A myproject worker --concurrency=4

    With --concurrency=4, one Celery worker can execute up to 4 tasks simultaneously (assuming the default prefork pool).
    Imagine 20 tasks in queue:
        4 tasks start executing.
        When 1 finishes, another task can take its place.
        When 3 finish, 3 more can start.
        This continues until all 20 tasks are completed.

    Concurrency is not the same as prefetch.
        - Concurrency = how many tasks can execute at the same time.
        - Prefetch = how many tasks a worker can reserve from the broker in advance, including tasks waiting for an execution slot.

    concurrency 4 and worker_prefetch_multiplier=4
        A worker may reserve up to 16 tasks, depending on the broker and acknowledgement configuration. But it still executes only 4 simultaneously.
    celery -A myproject worker --concurrency=4
        By default, worker_prefetch_multiplier is 4.

    Question:
    Scenario1:
    You have a Celery worker configured as:
        celery -A myproject worker --concurrency=4
    By default, worker_prefetch_multiplier is 4.

    Q1: a: What is the maximum number of tasks this worker may reserve from the broker?
        b: If you change worker_prefetch_multiplier=1, what changes?
        c: Why might setting it to 1 be beneficial when processing long-running tasks?
    Ans:
        a: Default prefetch_multiplier is 4 and conucurrency is  total tasks = 4*4 = 16
        b: With worker_prefetch_multiplier = 1 and concurrency 4:
        - The worker reserves up to 4 tasks.
        - It executes up to 4 tasks simultaneously.
        - As tasks complete and are acknowledged, it can reserve more tasks.
        c:
            Consider:
            Concurrency 2 worker_prefetch_multiplier 4
            Total tasks it can reserve from broker are 8
            Here the 4 tasks are executed simuntanously and 4 are reserved, since it is long running process it might take time to execute new tasks from the reserved tasks, during this time the other worker can be ideal

            With worker_prefetch_multiplier = 1 and concurrency 4:
            - The worker reserves up to 4 tasks.
            - It executes up to 4 tasks simultaneously.
            - As tasks complete and are acknowledged, it can reserve more tasks.
            This is particularly useful for long-running tasks because it reduces the chance that one worker holds tasks while another worker has available execution slots.

        "Concurrency determines how many tasks a worker can execute simultaneously, whereas the prefetch multiplier determines how many tasks a worker can reserve from the broker relative to its concurrency. For long-running tasks, I prefer setting the prefetch multiplier to 1 to avoid unfair task distribution and allow other workers to pick up tasks sooner."

        One nuance: exact reservation and acknowledgement behavior can depend on the broker and acknowledgement configuration

### Priority of tasks

    Suppose you have payment processing, email notifications, and report generation tasks.
    How would you assign high, medium, and low priorities using Celery's apply_async()?
    Code:
        process_payment.apply_async(
            args=[payment_id],
            priority=1
        )

        send_email.apply_async(
            args=[email_id],
            priority=5
        )

        generate_report.apply_async(
            args=[report_id],
            priority=9
        )

    For the standard Celery Redis and RabbitMQ configurations:
        - 0 = highest priority
        - 9 = lowest priority
    Priority support and its range depend on the broker. RabbitMQ supports priority queues when configured appropriately. Redis uses a different priority implementation, with its own limitations.

    Note:
    Priority means higher-priority tasks are generally selected ahead of lower-priority tasks when the broker has competing messages available. It does not interrupt tasks that are already running.

    For example, if four report-generation tasks are already running and a payment task arrives, the payment task cannot automatically interrupt those four tasks.

### Start dedicated queues

    # Dedicated payment worker
    celery -A myproject worker -Q payment_queue -n payment_worker@%h

    # Dedicated email worker
    celery -A myproject worker -Q email_queue -n email_worker@%h

    # Dedicated report worker
    celery -A myproject worker -Q report_queue -n report_worker@%h

    The -Q option tells the worker which queue to consume from.

### Task routing in django

    Suppose your Django application has 100 payment tasks and 10,000 email notification tasks.
    You want payment tasks to have dedicated workers, so email traffic never delays payment processing.
    Would you use separate queues, separate workers, or separate Celery applications? Explain your architecture.

    I would use seperate queue as payment_queue dedicated for payment processing
    and use dedicated queue as email_queue for email notifications

    2. How do you decide the number of workers and concurrency?
    You don't randomly choose 5 or 10 workers.

    You consider:
    1. Task execution time: How long does each payment or email task take?
    2. Task arrival rate: How many tasks arrive per second or minute?
    3. Hardware resources: CPU, memory and network capacity.
    4. External service limits: Email provider API rate limits and payment gateway limits.
    5. SLA: How quickly should a payment or email task finish?

    if your email provider allows only 50 emails per second, having 100 concurrent email tasks doesn't automatically mean you can send 100 emails per second.
    If payment provider allows only 10 payment processing a second

    email_queue --concurrency=10 --worker=5 -> 5*10 process 50 email per second
    payment_queue --concurrency=4 --worker=3 -> 12 task processing per second

### How do you handle duplicate payment processing

    To prevent duplicate payment processing in Django with Celery, I would combine idempotency, database transactions, row-level locking and late acknowledgement.

    1. Idempotency: I would generate a stable idempotency key for each logical payment using its payment ID. All duplicate Celery tasks and retries would reuse the same key. This ensures that the payment gateway can identify duplicate requests and avoid charging the customer multiple times.

    2. Database locking: I would use Django's transaction.atomic() and select_for_update() to lock the payment row. The first worker would change the status from PENDING to PROCESSING and commit the transaction. Other workers would then see PROCESSING and skip duplicate processing.

    3. External API call: I would call the payment gateway outside the database transaction to avoid holding database locks during network requests. I would pass the same idempotency key to the gateway.

    4. Late acknowledgement: I would configure Celery with acks_late=True so that tasks are acknowledged after execution. If a worker crashes, the message can be redelivered, subject to Celery's worker-loss configuration.

    5. Handling uncertain outcomes: If the gateway confirms success or definitive failure, I would update the database accordingly. If the gateway returns a timeout or unknown response, I would not immediately mark the payment as failed. I would retry or schedule reconciliation using exponential backoff and the same idempotency key.

    6. Processing lease: To recover payments stuck in PROCESSING after a worker crash, I would maintain a processing expiry timestamp. After the lease expires, another worker can safely take ownership and reconcile the payment.

    7. Fencing token: To prevent an older worker from updating the payment after another worker takes ownership, I would use a unique processing token or fencing token and perform conditional database updates.

    This approach helps prevent duplicate charges, handle worker crashes and maintain payment consistency.**

### What is the difference between a Celery Broker and a Result Backend?

    Broker:
        - Acts as a communication medium between the producer and Celery workers.
        - Contains queues holding task messages.
        - Messages contain task information, including task name, task ID and arguments.
    Result Backend:
        Stores task execution results.
        Can store task states such as PENDING, STARTED, SUCCESS and FAILURE.
        Can use PostgreSQL or Redis, depending on configuration.

    The broker is responsible for delivering tasks to workers, whereas the result backend is responsible for storing task execution states and results.
    The same Redis instance can perform both responsibilities, although they are logically separate.
    One additional detail: storing results is optional. You can configure Celery with task_ignore_result=True when you don't need task results.

    Interview:
        "The Celery broker acts as a communication medium between the producer and workers. It stores task messages in queues and delivers them to workers for execution.
        The result backend stores the execution status and return value of tasks. For example, it can store whether a task is pending, started, successful or failed.
        We need a broker to distribute tasks and a result backend when we need to track task execution and retrieve results.
        Redis can act as both the broker and result backend, provided we configure both separately."

### Can Celery work without Redis?

    Celery doesn't depend exclusively on Redis.
    RabbitMQ is a supported alternative broker.

    Broker	        Purpose
    Redis	        In-memory data store and message broker
    RabbitMQ	    Dedicated message broker
    Amazon SQS	    Managed cloud message queue

    Feature	                Redis	                    RabbitMQ
    Architecture	        In-memory data store	    Dedicated message broker
    Message delivery	    Fast queue operations	    Rich messaging and routing
    Routing	                Basic queue routing	        Exchanges and routing keys
    Persistence	            RDB/AOF options	            Durable queues and persistent messages
    Complex                 routing	                    Limited	Strong support
    Common use	            Caching and task queues	    Enterprise messaging

    For a typical Django + Celery application:
    - Redis: Good for simpler architectures, fast task queues and caching.
    - RabbitMQ: A strong choice when you need advanced routing, acknowledgements and messaging controls.

    Interview:
        "Yes, Celery can work without Redis. It supports alternative brokers such as RabbitMQ and Amazon SQS. Redis is commonly used because it is fast and simple to configure. RabbitMQ provides more advanced message routing and delivery controls. For applications requiring complex routing and messaging reliability, I would consider RabbitMQ."

### What happens internally when you execute task.delay()?

    Code:
        @shared_task
        def send_email(user_id):
            print(f"Sending email to {user_id}")
        send_email.delay(101)
    When task.delay() is triggered
        Celery sends serailized message to the celery broker
        {
            "task": "myapp.tasks.send_email",
            "id": "some-uuid",
            "args": [101],
            "kwargs": {}
        }
    Actual flow:
        The Django application has registered the task through Celery.
        The Celery worker starts with the same application configuration and imports/discovers the registered tasks.
        The worker maintains a task registry mapping task names to Python task implementations.
        When the worker receives the message, it reads the task name.
        It looks up the task name in its registry.
        It executes the corresponding Python function with the supplied arguments.
        Note:
        The actual function stays in the worker's Python environment. Only the task name and arguments are transmitted through Redis.

    Interview:
        When we use the @shared_task decorator, Celery registers the function as a task. When we call .delay(), Celery creates a task message containing the task ID, task name, positional arguments and keyword arguments.

        This message is serialized and published to the configured broker, such as Redis.

        The Celery worker consumes the message, identifies the task using its registered task name, looks up the corresponding Python function in its task registry and executes it with the supplied arguments.

        The result can then be stored in the configured result backend."

### Celery Worker vs Celery Beat
