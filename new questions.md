1. Celery – additional interview questions
   Highest priority
   A. Task execution and architecture
   1. What is the difference between delay() and apply_async()?
   2. What is the difference between a Celery broker and a result backend?
   3. Can Celery work without Redis?
   4. What happens when you execute task.delay() internally?
   5. What is the difference between Celery Worker and Celery Beat?
   6. Can multiple workers consume tasks from the same queue?
   7. How do you create multiple queues in Celery?
   8. How do you route different tasks to different queues?
   9. What happens if a worker crashes while executing a task?
   10. What happens if a task takes 30 minutes to complete?

       B. Task failure and reliability

   11. What is the difference between task retry and task redelivery?
   12. What is acks_late?
   13. What is task_reject_on_worker_lost?
   14. What is the visibility timeout in Redis broker?
   15. What happens if a task is executed twice?
   16. How do you make Celery tasks idempotent?
   17. How do you prevent duplicate task execution?
   18. What happens if all three retry attempts fail?
   19. How do you implement exponential backoff?
   20. How do you handle tasks that continuously fail?

       C. Scaling and performance

   21. How do you determine the optimal Celery concurrency?
   22. What is the difference between prefork, threads and gevent pools?
   23. What is the difference between concurrency and number of workers?
   24. What is Celery prefetch multiplier?
   25. What happens if prefetch multiplier is too high?
   26. How do you prioritize critical tasks over normal tasks?
   27. How do you monitor queue length?
   28. How do you scale workers automatically?
   29. How do you prevent memory leaks in long-running workers?
   30. How do you handle a backlog of one million tasks?

       D. Practical implementation scenarios

   31. You have a task processing one million records. How would you process it efficiently?
   32. A user starts an Excel export containing one million records. How would you implement cancellation?
   33. A Celery task sends an email, but the worker crashes immediately afterward. How do you avoid duplicate emails?
   34. Redis is available, but workers are not consuming messages. How would you debug it?
   35. Your tasks are taking longer than their expected execution time. How would you investigate?
   36. How would you implement scheduled tasks using Celery Beat?
   37. How would you prevent two Celery workers from processing the same business operation simultaneously?
   38. How would you handle a task dependent on another task's completion?

2. Redis – additional interview questions
   Highest priority
   A. Fundamentals
   1. Why do we use Redis in Django applications?
   2. Is Redis a database or a cache?
   3. What is the difference between Redis and PostgreSQL?
   4. What data structures does Redis support?
   5. What is the difference between Redis Lists, Sets and Sorted Sets?
   6. What is Redis Pub/Sub?
   7. What is Redis persistence?
   8. What are RDB and AOF?
   9. What happens when Redis runs out of memory?
   10. What is Redis eviction policy?
       B. Caching implementation
   11. How do you implement Redis caching in Django?
   12. What is cache-aside strategy?
   13. What is cache invalidation?
   14. How do you set cache expiration using TTL?
   15. What happens when cached data becomes stale?
   16. How do you prevent cache stampede?
   17. What is cache penetration?
   18. What is cache avalanche?
   19. How do you invalidate cache when a database record is updated?
   20. When should you avoid caching?
       C. Distributed systems
   21. How do you implement distributed locking using Redis?
   22. What happens if a Redis lock expires while a task is still executing?
   23. How do you prevent race conditions using Redis?
   24. What is the difference between Redis transactions and database transactions?
   25. What is Redis Sentinel?
   26. What is Redis Cluster?
   27. How would you achieve Redis high availability?
   28. What happens if Redis restarts?
   29. Can Redis guarantee that every message will be delivered exactly once?
   30. How would you monitor Redis memory and latency?
       D. Practical scenarios
   31. Multiple users request the same expensive API simultaneously. How would you reduce database load using Redis?
   32. How would you implement API rate limiting using Redis?
   33. How would you implement OTP expiration?
   34. How would you maintain a user's session using Redis?
   35. How would you prevent two users from booking the same seat using Redis and PostgreSQL?

3. Django – implementation and internals
   Highest priority
   A. Django internals
   1. Explain the Django request-response lifecycle.
   2. What happens internally when a request reaches Django?
   3. What is middleware? How do you create custom middleware?
   4. What is the difference between WSGI and ASGI?
   5. What is the difference between synchronous and asynchronous Django views?
   6. What happens when you use async def in a Django view?
   7. What is the difference between APIView, GenericAPIView and ViewSet?
   8. What is the difference between serializers and models?
   9. What is the difference between authentication and authorization?
   10. How does Django handle database connections?
       B. Django ORM and optimization
   11. What is the difference between select_related() and prefetch_related()?
   12. What is the N+1 query problem?
   13. How do you identify slow database queries?
   14. What is the difference between only() and defer()?
   15. What is the difference between annotate() and aggregate()?
   16. What is the difference between get(), filter() and first()?
   17. What are database indexes? When should you create them?
   18. What is bulk_create() and when would you use it?
   19. How do you perform database transactions in Django?
   20. What is transaction.atomic()?
   21. What is F() expression and how does it help prevent race conditions?
   22. What is select_for_update()?
   23. How do you optimize an API making 100 database queries?
   24. How do you handle pagination for millions of records?
       C. Real-world Django scenarios
   25. Two users book the same seat simultaneously. How would you prevent double booking?
   26. A user clicks the payment button twice. How do you prevent duplicate payments?
   27. An API receives 500 concurrent requests. How would you handle them?
   28. A Django API takes 10 seconds to respond. How would you debug and optimize it?
   29. A database transaction fails halfway through. What happens?
   30. How would you implement soft deletion?
   31. How would you implement audit logging?
   32. How would you handle file uploads for large files?
   33. How would you implement role-based permissions?
   34. How would you prevent unauthorized access to another user's records?
   35. How would you handle a database schema change without downtime?
   36. Django + Celery integration
       These are particularly important because your interviewer is already asking about the interaction between these components.
   37. How do you trigger a Celery task from a Django API?
   38. Why should we use transaction.on_commit() when triggering Celery tasks?
   39. What happens if a Django database transaction rolls back after a Celery task is published?
   40. How do you pass data from Django to Celery?
   41. Should you pass a Django model object or its ID to a Celery task?
   42. How do you track task execution status in Django?
   43. How do you show task progress to the frontend?
   44. How do you cancel a running Celery task?
   45. What is the difference between revoke() and revoke(terminate=True)?
   46. How do you handle a task that depends on a database record that hasn't committed yet?
   47. How do you implement an Outbox Pattern using Django and Celery?
   48. How do you ensure a task is not lost if Redis becomes unavailable?
   49. PostgreSQL – backend implementation
   50. What is the difference between INNER JOIN and LEFT JOIN?
   51. What is a database index?
   52. What is a composite index?
   53. What is a deadlock?
   54. What is a race condition?
   55. What are ACID properties?
   56. What is transaction isolation?
   57. What is the difference between optimistic and pessimistic locking?
   58. How do you identify slow queries using EXPLAIN ANALYZE?
   59. How do you handle connection pooling?
   60. What happens when 1,000 requests try to access PostgreSQL simultaneously?
   61. How do you prevent duplicate records at the database level?
   62. Docker and deployment
   63. Why do we run Django and Celery in separate containers?
   64. How do containers communicate with each other?
   65. How do you pass environment variables to Docker containers?
   66. What is the difference between CMD and ENTRYPOINT?
   67. What is Docker Compose?
   68. How do you execute Django migrations during deployment?
   69. What happens if a container crashes?
   70. How do you check container logs?
   71. How do you implement health checks?
   72. How do you scale Celery workers using Docker Compose?
   73. How do you ensure migrations don't run simultaneously from multiple application containers?
   74. How would you deploy a Django application without downtime?
