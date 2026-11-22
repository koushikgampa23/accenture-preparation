# Documentation

    This document contains python coding questions

## Full questions

    A. Arrays
    Very high priority
    1. Find the largest element in an array.
    2. Find the second-largest element without sorting.
    3. Find the smallest and second-smallest elements.
    4. Reverse an array.
    5. Find duplicate elements in an array.
    6. Remove duplicates from an array.
    7. Find the missing number from 1 to N.
    8. Find the frequency of each element.
    9. Find the element that appears only once.
    10. Find the majority element.
    11. Move all zeros to the end.
    12. Move all negative numbers to one side.
    13. Find the intersection of two arrays.
    14. Find the union of two arrays.
    15. Rotate an array left by K positions.
    16. Rotate an array right by K positions.
    17. Find the pair whose sum equals a target.
    18. Find all pairs with a given difference.
    19. Find the maximum sum of a contiguous subarray.
    20. Find the equilibrium index of an array.
    21. Find the leaders in an array.
    22. Find the product of array elements except self.
    23. Find the maximum difference between two elements.
    24. Merge two sorted arrays.
    25. Sort an array containing only 0s, 1s and 2s.
    B. Strings
    Very high priority
    26. Reverse a string.
    27. Check whether a string is a palindrome.
    28. Check whether two strings are anagrams.
    29. Count vowels and consonants.
    30. Count the frequency of each character.
    31. Find the first non-repeating character.
    32. Find the first repeating character.
    33. Remove duplicate characters from a string.
    34. Find duplicate characters.
    35. Reverse each word in a sentence.
    36. Reverse the order of words in a sentence.
    37. Find the longest word in a sentence.
    38. Check whether a string contains only digits.
    39. Find the most frequent character.
    40. Check whether one string is a rotation of another.
    41. Find the common characters between two strings.
    42. Find the longest common prefix.
    43. Count the number of words in a string.
    44. Replace spaces with a special character.
    45. Find the longest substring without repeating characters.
    C. Numbers and mathematics
    Very high priority
    46. Check whether a number is prime.
    47. Print prime numbers within a given range.
    48. Find the factorial of a number.
    49. Find the Fibonacci series.
    50. Check whether a number is Armstrong.
    51. Check whether a number is a palindrome.
    52. Reverse a number.
    53. Find the sum of digits of a number.
    54. Count the number of digits.
    55. Find GCD and LCM.
    56. Find the power of a number without using **.
    57. Check whether a number is perfect.
    58. Check whether a number is a strong number.
    59. Convert decimal to binary.
    60. Convert decimal to hexadecimal.
    61. Find the number of trailing zeros in a factorial.
    62. Find the number of factors of a number.
    63. Find the sum of numbers divisible by 3 and 5.
    64. Calculate the number of carries when adding two numbers.
    D. Dictionary and hashing
    Very high priority
    65. Count the frequency of words in a sentence.
    66. Find the common elements in two lists using dictionaries.
    67. Find the first unique element.
    68. Group anagrams together.
    69. Find two numbers whose sum equals a target.
    70. Find the most frequent element.
    71. Find the top K frequent elements.
    72. Find duplicate elements using a dictionary.
    73. Find whether two arrays have the same frequency distribution.
    74. Find the intersection of multiple lists.
    E. Searching and sorting
    75. Implement linear search.
    76. Implement binary search.
    77. Find the first occurrence of an element in a sorted array.
    78. Find the last occurrence of an element.
    79. Find the insertion position of an element.
    80. Implement bubble sort.
    81. Implement selection sort.
    82. Implement insertion sort.
    83. Merge two sorted lists.
    84. Find the Kth largest element.
    85. Search in a rotated sorted array.
    F. Two pointers and sliding window
    86. Find a pair with a given sum in a sorted array.
    87. Remove duplicates from a sorted array in-place.
    88. Check whether a string is a palindrome using two pointers.
    89. Find the maximum sum of a subarray of size K.
    90. Find the longest substring without repeating characters.
    91. Find the minimum-length subarray with sum greater than or equal to K (positive numbers).
    92. Find the longest sequence of ones after replacing at most K zeros.
    93. Find the maximum average subarray of size K.
    G. Matrix problems
    94. Find the sum of matrix diagonals.
    95. Find the transpose of a matrix.
    96. Rotate a matrix by 90 degrees.
    97. Print matrix elements in spiral order.
    98. Find the largest element in each row.
    99. Find the row with the maximum number of ones.
    100. Search for an element in a sorted matrix.
    101. Count the number of islands in a binary matrix.
    H. Stack, recursion and basic DSA
    102. Check balanced parentheses.
    103. Implement a stack using a list.
    104. Implement a queue using a list or deque.
    105. Find the next greater element.
    106. Reverse a stack.
    107. Calculate factorial using recursion.
    108. Generate Fibonacci using recursion.
    109. Find the sum of an array using recursion.
    110. Generate all subsets of an array.
    111. Implement Tower of Hanoi.

## Important interview questions

    0. Flattening question:
    Question:
        nested = {
            "user": {"name": "John", "age": 30, "add": "US"},
            "items": [1, {"id": {"name": "koushik"}}, 3, {"id": 19}],
        }
    Result:
    [('user.name', 'John'), ('user.age', 30), ('user.add', 'US'), ('items.1.id', 42), ('items.3.id', 19)]

    Code:
        def flattening(nested, result, key_history=""):
            if isinstance(nested, dict):
                for key, value in nested.items():
                    new_key = f"{key_history}.{key}" if key_history else key
                    flattening(value, result, new_key)

            elif isinstance(nested, list):
                for index, value in enumerate(nested):
                    new_key = f"{key_history}.{index}" if key_history else str(index)
                    flattening(value, result, new_key)

            else:
                # base case: int, str, etc.
                result.append((key_history, nested))

            return result

        print(flattening(nested, []))

    My way:
        # Flattening question
        nested = {
            "user": {"name": "John", "age": 30, "add": "US"},
            "items": [1, {"id": 42}, 3, {"id": 19}],
        }


        def flattening(nested, result, key_history):
            if isinstance(nested, dict):
                for key, value in nested.items():
                    new_key = key_history + "." + key if key_history else key
                    if isinstance(value, int) or isinstance(value, str):
                        result.append((new_key, value))
                    else:
                        flattening(
                            value, result, new_key
                        )  # Since value is dict recurssion to extract key_history
            if isinstance(nested, list):
                for index in range(len(nested)):
                    nested_elm = nested[index]
                    if isinstance(nested_elm, int) or isinstance(nested_elm, str):
                        pass
                    else:
                        new_key = key_history + "." + str(index)
                        flattening(nested_elm, result, new_key)
            return result


        result = flattening(nested, [], "")
        print(result)

    1.Authorization and Authentication
        Authentication
            Authentication verifies the identity of a user.
            The system checks whether the user is actually who they claim to be.
        Authorization
            Authorization determines whether an authenticated user has permission to perform a particular action or access a resource.

    2.The employee having Third highest salary
        select * from employee where salary = (select DISTINCT(salary) from employee order by salary desc limit 1 offset 2) order by salary;

    3.DENSE_RANK
        #Todo

    3.1.Use where and having class to get the 3rd highest salary of each department
        #Todo

    4.What is an indexing
        An index is a data structure that helps the database locate records faster without scanning the entire table
        Advantages:
            Faster data retrieval.
            Reduces full table scans for suitable queries.
            Improves performance of WHERE, JOIN, ORDER BY and sometimes GROUP BY operations.
            Can improve lookup performance on frequently queried columns.
        Disadvantages:
            The database inserts the row into the table.
            It updates the relevant indexes.
            It may need to split or rebalance index pages in certain situations.
        Where should we create indexes
            Frequently queried columns.
            Foreign keys used in JOINs.
            Columns used frequently in WHERE conditions.
            Columns used in sorting and filtering.

    5. How is memory managed in python
        Python manges memory though its memory manager, private heap, reference counting, garbage collector
        Main concepts(5):
            Python memory management architecture, Refernce counting, Garbage collection, Stack vs heap memory, Memory leaks

        1. How Python manages memory
            Python allocates memory dynamically when the object is created
            Example:
                a = [1, 2, 3], b = "hello", c = 100
            Python allocates memory for these objects in its private heap
            The Python memory manager is responsible for:
                Allocating memory for objects.
                Managing allocated memory.
                Reusing memory when objects are no longer needed.
                Releasing memory when possible.
        2. Reference counting
            Python keeps track of how many references point to an object.
            Example:
                a = [1, 2, 3]
                b = a
                c = a
            del removes a reference, not necessarily the object itself.
        3. Garbage Collection
            What happens if two objects reference each other?
            Example:
                a = []
                b = []

                a.append(b)
                b.append(a)
            #a references b.
            #b reference a.
                del a
                del b
            Their reference counts are still nonzero because they reference each other.
            This is called a reference cycle.
            Python's cyclic garbage collector detects unreachable reference cycles and reclaims them.
            With can intract with garbage collector using gc
            Example:
                import gc
                gc.collect()
        4. Stack memory vs Heap memory
            Stack:
                Stores function call frames and local execution state
                Automatically managed as functions execute and return
                Function calls create frames
            Heap:
                Stores Python objects
                Managed by Python memory manager
                Objects are dynamically allocated
        5.How does Python actually allocate memory?
            Private heap: Stores Python objects.
            Python memory allocator: Manages memory requests.
            pymalloc: Optimizes allocation of small objects, typically up to 512 bytes.
            Operating system: Provides memory to the Python process.

            Python may retain memory for reuse instead of immediately returning it to the operating system when an object is deleted.
            This is why you might notice that memory usage doesn't immediately decrease even after deleting objects.
        6. What is a memory leak in python
            A memory leak occurs when objects that are no longer needed remain reachable, so their memory cannot be reclaimed.
            Example:
                data = []
                def process():
                    data.append("some large data")
                for i in range(100000):
                    process()
            Here, the global list continuously grows because we keep adding objects and never remove them.
            Even though Python has garbage collection, it cannot automatically remove objects that are still referenced.

            How to prevent memory leaks:
                - Avoid unnecessary global variables.
                - Remove references to objects when no longer needed.
                - Be careful with caches and unbounded collections.
                - Close files and database connections using context managers.
                - Monitor memory using tracemalloc.
        Summary:
            Concept - Meaning
            Reference counting - Tracks references to objects
            Garbage collection - Reclaims unreachable reference cycles
            Heap               - Stores Python objects
            Stack/frame	       - Holds function execution state
            pymalloc	       - Efficient allocator for small objects
            Memory leak	       - Unwanted objects remain reachable

    7. Shallow copy vs deep copy:
        Shallow copy:
            A shallow copy creates a new outer object, but the nested objects are still shared between the original and copied objects.
        Deep copy:
            A deep copy creates a new outer object and recursively copies nested objects as well.
    8. Mutable objects vs immutable objects
        Mutable: Objects whose contents can be changed after creation.
        Immutable: Objects whose value cannot be changed after creation.
                    example: int, float, tuples are immutable
        Example:
            a=10
            a=20
            The original integer object 10 is not modified. Instead, the variable a is reassigned to refer to another integer object, 20.

        Example2:
            a = ([1, 2, 3], 10)
            a[0].append(4)
            print(a)

            The tuple itself is immutable.
            The list inside the tuple is mutable.
            You are modifying the list, not replacing the tuple's element.
        Example3:
            a = (1, 2, 3)
            a += (4,)
            print(a)
    8.1 Answer this questions
        def add(item, items=[])
            items.append(item)
            return items

        a = add(1)
        b = add(2, [])
        c = add(3)

        print(a) #[1,3] since a still referencing to default items object
        print(b) #[2] since i had given array then the add happens to given array
        print(c) #[1,3] #The appending happens to default items that is referred by a and c so same value

    8.2 is vs ==
        is - Checks whether two variables refer to the exact same object in memory.
        == - Checks whether two objects have equal values. It does not necessarily check whether their data types are identical.

        Example:
            a = True
            b = 1

            print(a==b) #True since python considers True as 1.
            print(a is b) #False the reference of 1 and True are different
            print(type(a) == type(b)) #False, since a is bool and b is integer

        Example2:
                l1 = [1, 2, 3]
                l2 = list(l1)
                print(l2 is l1) # False Here the l1 is assigned to l2 new reference created
                print(l2 == l1) # True values are same

                t1 = (1, 2, 3)
                t2 = tuple(t1)
                t3 = tuple(t1)
                print(t3 is t2) # False
                print(t3 == t2) # True

                s1 = 'ABC'
                s2 = 'ABC'
                print(s1 is s2) # True, python internally uses string objects and assign to new same object

                a = [1,2,3]
                b = a
                c = [1,2,3]

                print(a==b) #True same values
                print(a is b) #True same reference
                print(a==c) #True
                print(a is c) #False

    9. Tuples vs lists
        Python lists are dynamic arrays. They sometimes allocate extra capacity to accommodate future elements, reducing the need to resize on every append.
        Tuples are fixed-size collections, so they don't need this dynamic resizing mechanism.
        However:
            Tuples are often smaller in memory than equivalent lists.
            Tuples can be slightly faster to create and iterate over in some situations.
            Tuples are not universally faster than lists for every operation.

    10. Difference class methods, static methods and instance methods

        Instance methods take self as their first parameter. They can access both instance and class variables. However, assigning a value through self creates or modifies an instance attribute rather than modifying the class variable.

        Class methods use the @classmethod decorator and take cls as their first parameter. They can access and modify class-level variables. We don't need to create an object to invoke them.

        Static methods use the @staticmethod decorator. They don't receive either self or cls as an implicit argument. They are generally used for utility operations logically related to the class.

        Code:
        class Test:
            company = "honda"

            def __init__(self, name):
                self.name = name

            def get_info(self):
                print(self.name, self.company)

            def set_company(self, new_company):
                self.company = new_company #Creates a new instance variable company,not modifying class attribute

            @classmethod
            def set_company_name(cls, new_company):
                cls.company = new_company

            @staticmethod
            def calculate(a, b):
                print(4 + 5)


        test1 = Test("instance")
        test1.get_info() #instance honda
        test1.set_company("hero") #instance hero
        test1.get_info() #instance hero

        test2 = Test("instance2")
        test2.get_info() #instance2 honda

        Test("class method").set_company_name("hero")

        test1.get_info() #instance1 hero
        test2.get_info() #instance2 hero

        Test("static method").calculate(4, 5) #9

        Code2:
        class Employee:
            company = "ABC"

            @classmethod
            def update_company(cls, name):
                cls.company = name

        class Developer(Employee):
            pass

        Employee.update_company("Google")

        print(Employee.company) # ABC
        print(Developer.company) # ABC

        Developer.update_company("Microsoft")

        print(Employee.company) # ABC
        print(Developer.company) # Microsoft

    11. OOPS in python
        Encapsulation, Abstraction, Polymorphism, Inheritance, class and objects

## Use full git commands

    git init - To initialize git
    git branch -M main - Create a main branch
    git remote add origin https://github.com/koushikgampa23/accenture-preparation.git
    git commit -m "initial commit"
    git push -u origin main

    later we can use git push origin main

### Find the largest element in an array.

    arr = [1, 4, 3, 5, 2]

    max_elm = arr[0]
    for elm in arr[1:]:
        if elm > max_elm:
            max_elm = elm

    print(max_elm)

### Find the second-largest element without sorting.

    #two traversals
    arr = [1, 4, 3, 5, 2, 6]

    largest_elm = arr[0]

    for elm in arr:
        if elm > largest_elm:
            largest_elm = elm
    print(largest_elm)

    second_largest_elm = float("-inf")
    for elm in arr:
        if elm > second_largest_elm and largest_elm != elm:
            second_largest_elm = elm

    print(second_largest_elm)

    Optimized one:
        ### Find the second-largest element without sorting.
        #one traversals
        arr = [1, 4, 3, 5, 2, 6]

        largest_elm = float("-inf")
        second_largest_elm = float("-inf")

        for elm in arr:
            if elm > largest_elm:
                second_largest_elm = largest_elm
                largest_elm = elm

            elif elm > second_largest_elm and elm != largest_elm:
                second_largest_elm = elm

        print(largest_elm, second_largest_elm)

        # Dry run
        1 > -inf -> largest 1 and second -inf
        4 > 1 -> largest 4 and second 1
        3 > 4 -> no, 3>1 second 3
        5>4 -> largest = 5 and second 4
        2 > 5 -> no and 2 > 4 no
        6 > 5 -> largest 6 and second 5

### Find the third-largest element without sorting.

    #one traversals
    arr = [1, 4, 3, 5, 2, 6, 7, 0, 10]

    largest = float("-inf")
    second = float("-inf")
    third = float("-inf")

    for elm in arr:
        if elm > largest:
            third = second
            second = largest
            largest = elm
        elif elm > second and elm != largest:
            third = second
            second = elm
        elif elm > third and elm != second and elm != largest:
            third = elm

    print(largest, second, third)

### Find the second smallest element without sorting.

    #one traversals
    arr = [0, 4, 3, 5, 2, 6, 7, 11, 10]

    smallest = float("inf")
    second_smallest = float("inf")

    for elm in arr:
        if elm < smallest:
            second_smallest = smallest
            smallest = elm
        elif elm < second_smallest and elm != smallest:
            second_smallest = elm

    print(smallest, second_smallest)

### Reverse an array

    arr = [0, 4, 3, 5, 2, 6, 7, 11, 10]

    i = 0
    j = len(arr) - 1

    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

    print(arr)

    # Time complecity n/2 = 0(n)
    # Space complexity 0(1) modifiying exisiting array

### Find duplicate elements in an array.

    arr = [1, 2, 3, 4, 2, 1, 3, 1, 0]

    freq_count = {}
    duplicate_elem = set()

    for elm in arr:
        if elm not in freq_count:
            freq_count[elm] = 0
        freq_count[elm] += 1
        if freq_count[elm] > 1:
            duplicate_elem.add(elm)

    print(duplicate_elem)

    # Time complexity -> iteration 0(n), searching 0(1)
    # Space complexity -> 0(k) k distinct elements for set and dict

### Remove duplicates from an array.

    from copy import deepcopy

    arr = [1, 2, 3, 4, 2, 1, 3, 1, 0]

    freq_count = {}
    result = []

    for elm in arr:
        freq_count[elm] = freq_count.get(elm, 0) + 1

        if freq_count[elm] > 1:
            continue

        result.append(elm)

    print(result)

### Find the missing from 1 to N.

    arr = [1, 2, 4, 6, 7]
    N = 8

    missing_elems = []

    arr = set(arr)

    for i in range(1, N + 1):
        if i not in arr:
            missing_elems.append(i)

    print(missing_elems)

### Find the element that appears only once.

    arr = [1, 2, 3, 5, 6, 2, 3, 1]

    elm_freq = {}

    for elm in arr:
        elm_freq[elm] = elm_freq.get(elm, 0) + 1

    freq_elm = {}

    for elm, freq in elm_freq.items():
        freq_elm[freq] = freq_elm.get(freq, [])
        freq_elm[freq].append(elm)

    print(freq_elm)

    print(freq_elm[1])

### Find the majority element

    #If element repeats more than half then it is called majority element

    arr = [1, 2, 3, 1, 1, 1, 1, 5]

    elm_freq = {}
    majority = None

    for elm in arr:
        elm_freq[elm] = elm_freq.get(elm, 0) + 1
        if elm_freq[elm] > len(arr) / 2:
            majority = elm

    if majority:
        print(majority)
    else:
        print("No majority element")

### Find the intersection of two arrays.

    ### Find the intersection of two arrays.

    arr1 = [1, 2, 3, 4, 5]
    arr2 = [3, 4]

    intersection_arr = []

    for elm1 in arr1:
        if elm1 in arr2:
            intersection_arr.append(elm1)

    print(intersection_arr)


    # Time complexicity: 0(n*m), n-elms in arr1, m-elems in arr2
    # Space complexicity: 0(n+m)

    # Optimized approach

    arr1 = [3, 4]

    arr2 = [1, 2, 3, 4, 5]

    i = 0
    j = 0

    intersection = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            intersection.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr1[i]:
            j += 1

    print(intersection)

    Time Complexity: 0(m+n)

### Union of 2 arrays

    arr1 = [3, 4]

    arr2 = [1, 2, 3, 4, 5]

    i = 0
    j = 0

    union = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            union.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            union.append(arr1[i])
            i += 1
        elif arr2[j] < arr1[i]:
            union.append(arr2[j])
            j += 1


    print(union)

## Two pointers

### Move all zeros to the end.

    arr = [0, 1, 0, 3, 12]

    i = 0
    j = 1

    while j < len(arr):
    if arr[i] != 0:
    i += 1
    if arr[i] == 0 and arr[j] != 0:
    arr[i], arr[j] = arr[j], arr[i]
    i += 1
    j += 1

    print(arr)

### Find the missing numbers between elements

    arr = [1, 2, 4, 6, 8]

    i = 0
    j = 1
    missing_elems = []

    while j < len(arr):
    difference = arr[j] - arr[i]

        for index in range(arr[i] + 1, arr[j]):
            missing_elems.append(index)

        i += 1
        j += 1

    print(missing_elems)

### Rotate an array left by K positions.

    arr = [1, 2, 3, 4]
    k = 2

    prefix = arr[:k]
    suffix = arr[k:]

    print(suffix + prefix)

    Another approach:

    Reverse the k elements and Reverse the entire array
    arr = [1,2,3,4]
    k = 3

    reverse_k_elements = [3,2,1,4]
    reverse_entire = [4,1,2,3]

    arr = [1, 2, 3, 4]
    k = 3

    # reverse first k elements

    i = 0
    j = k - 1

    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

    # reverse entire array

    i = 0
    j = len(arr) - 1

    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

    print(arr)

### Find the pair whose sum equals a target.

    arr = [1, 2, 5, 4, 0, 4]
    target = 8

    a = set()

    for elm in arr:
        difference = target - elm
        if difference in a:
            print(elm, difference)
            break
        a.add(elm)

    # Time complexicity - 0(n), n - len(arr), 0(1) for searching since using set
    # Space complexicity - 0(k), distinct elements in arr

### Find all pairs with a given difference.

    arr = [1, 2, 5, 4, 0, 4, 6]
    difference = 2

    a = set()
    pairs = []

    for elm in arr:
        below_pair_elm = elm - difference
        above_pair_elm = elm + difference
        if below_pair_elm in a:
            pairs.append((elm, below_pair_elm))
        if above_pair_elm in a:
            pairs.append((elm, above_pair_elm))
        a.add(elm)

    print(pairs)

### Find the maximum sum of a contiguous subarray.

    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

    max_sum = float("-inf")
    current_sum = 0

    for elm in arr:
        current_sum += elm
        max_sum = max(max_sum, current_sum)
        if current_sum < 0:
            current_sum = 0

    print(max_sum)

## Strings

### Reverse a string.

    a = "abc"

    reversed_str = ""

    i = len(a) - 1

    while i >= 0:
        reversed_str += a[i]
        i -= 1

    print(reversed_str)

### Reverse a string.

    s1 = "listen"
    s2 = "silent"

    reversed_str = ""

    i = len(s2) - 1

    while i >= 0:
        reversed_str += s2[i]
        i -= 1

    if reversed_str == s1:
        print("palindrome")
    else:
        print("not palindrome")

### Check whether a number is Armstrong.

    n = 153

    n = str(n)

    calculated_sum = 0

    power = len(n)

    for char in n:
        num = int(char)
        calculated_sum += num**power

    if calculated_sum == int(n):
        print("Armstrong number")
    else:
        print("Not")

    Extract numbers mathematically:
        153 // 10 gives round off number 15.3 to 15 eliminating last digit
        153 % 10 gives remainder that is 3
    Code:
        n = 153
        temp = n
        nums = []

        while n > 0:
            nums.append(n % 10)
            n = n // 10

        calulated_sum = 0
        for elm in nums:
            calulated_sum += elm ** len(nums)

        if temp == calulated_sum:
            print("Armstrong")
        else:
            print("no")

## Interview level questions

### 1.Rat and food problem

    There are r rats in a locality. Each rat consumes unit amount of food.
    You are given an array arr, where each element represents the amount of food available in a particular house.
    Find the minimum number of houses required to provide sufficient food to all the rats.

    r = 7
    unit = 2
    arr = [2, 8, 3, 5, 7, 4, 1, 2]


    def rats_food(r, unit, arr):
        food_needed = r * unit
        cumulated_food = 0
        houses = 0

        if len(arr) == 0:
            return -1

        if food_needed == 0:
            return 0

        for elm in arr:
            cumulated_food += elm
            houses += 1
            if cumulated_food >= food_needed:
                return (cumulated_food, houses)
        return 0


    houses = rats_food(r, unit, arr)
    print(houses)

### 2. Number of Carries

    Given two positive integers, calculate how many carry operations occur when adding them.

    Code:
        num1 = 999
        num2 = 1

        carry = 0
        count = 0

        while num1 > 0 or num2 > 0:
            num1_digit = num1 % 10
            num2_digit = num2 % 10

            digits_sum = num1_digit + num2_digit + carry
            carry = 0

            if digits_sum // 10 > 0:
                carry += 1
                count += 1

            num1 = num1 // 10
            num2 = num2 // 10

        print(count)

### 3 Decimal to N-base Conversion

    Given a decimal number num and a base n, convert the decimal number into the specified base.

# Interview Questions

## Celery vs asyncio

    Both asyncio and Celery are used to execute tasks without blocking the main execution flow, but they solve different problems.

    Asyncio - is used for concurrency within the application process. It uses an event loop to manage multiple coroutines. When one coroutine encounters an I/O-bound operation, such as an API call or database operation, it can yield control to the event loop, allowing other coroutines to execute while waiting for the result.

    Celery - is a distributed task queue used for executing background jobs. We push tasks to a message broker like Redis or RabbitMQ, and separate Celery workers consume and execute those tasks independently of the web application.
    Celery also provides task tracking through task IDs, retries, scheduling, and result management using a result backend.

    For example, I would use asyncio when I need to make multiple external API calls concurrently within a request. I would use Celery for long-running operations such as sending emails, generating reports, processing files, or executing scheduled jobs.

    So, the main difference is that asyncio provides concurrency within the application, whereas Celery provides distributed background task processing.

### What is the difference between async and await?

    async def defines a coroutine function.
    Calling an async function creates a coroutine object.
    await suspends the current coroutine until the awaited operation completes.
    While waiting, the event loop can execute other scheduled tasks.

### Answer the below questions

    call_api1 takes 3 seconds
    call_api2 takes 5 seconds

#### Code1:

    async def main():
    response1 = await call_api1() #takes 3 seconds
    response2 = await call_api2() # takes 5 seconds

    Total time taken = 8 seconds, since await waites until we get the result
    Key takeaway: Awaiting one coroutine before starting the next produces sequential execution.

#### Code2:

    import asyncio

    async def main():
        response1, response2 = await asyncio.gather(
            call_api1(),
            call_api2()
        )

        print(response1)
        print(response2)

    asyncio.run(main())

    Takes 5 seconds, gather executes call_api1 and call_api2 concurrently and yields the results to response1 and response2

    Note: Gather yields the result until all the coourtines are executed, so we cant get call_api1() at 3 seconds need to wait until response2 is also completed

    If we wanted results as soon the coourtine is executed we can use create_task to schedule coorutine and get the result

    asyncio.create_task() schedules a coroutine to run as an independent task on the event loop.
    import asyncio

    async def main():
        task1 = asyncio.create_task(call_api1()) #Scheduled call_api1() in event loop
        task2 = asyncio.create_task(call_api2()) #Scheduled call_api2() in event loop

        result1 = await task1
        result2 =  await task2

        Takes 5 seconds to complete, in this approach we get result1 at 3 seconds no need to wait until we get result2

#### What happens if we schedule tasks sequentially?

    async def main():
    task1 = asyncio.create_task(call_api1()) #Scheduled task1 at event loop

    response1 = await task1 #Cooutine needs to yield result for response1

    task2 = asyncio.create_task(call_api2())

    response2 = await task2

    Time taken is 8 seconds, they execute sequentially, here task is scheduled and yielded in next step

    gather(): When you need all API responses together.
    create_task(): When you need to schedule and manage tasks independently.
    as_completed(): When you want to process results as soon as individual tasks complete.

    tasks = [
        asyncio.create_task(call_api1()),
        asyncio.create_task(call_api2()),
        asyncio.create_task(call_api3())
    ]

    for task in asyncio.as_completed(tasks):
        result = await task
        print(result)

#### How do you handle exceptions in asyncio.gather()?

    API 1 succeeds in 2 seconds.
    API 2 succeeds in 3 seconds.
    API 3 fails after 5 seconds.

    By default, asyncio.gather() propagates the first exception to the caller. Other submitted awaitables aren't automatically cancelled.

    Code:
        results = await asyncio.gather(
            call_api1(),
            call_api2(),
            call_api3(),
            return_exceptions=True #Allows us to return an exception if any task raised an exception
        )

        for result in results:
            if isinstance(result, Exception):
                print("API failed:", result)
            else:
                print("API succeeded:", result)

#### Implement retry logic in asyncio

    Code:
        async def call_with_retry(api, retries=3):
            for attempt in range(retries):
                try:
                    return await api()
                except TimeoutError:
                    if attempt == retries - 1:
                        raise
                    await asyncio.sleep(1)

        results = await asyncio.gather(
            call_with_retry(call_api1),
            call_with_retry(call_api2),
            call_with_retry(call_api3),
            return_exceptions=True
        )

### Multithreading vs Multiprocessing

    Python supports both multithreading and multiprocessing.

    In conventional CPython, the Global Interpreter Lock (GIL) allows only one thread at a time to execute Python bytecode within a process.

    Multithreading allows us to create multiple threads within the same process. These threads share the same memory space, making communication easier. It is particularly useful for I/O-bound operations, such as making API calls, downloading files or database operations.

    Multiprocessing, on the other hand, creates multiple independent processes, each with its own memory space and Python interpreter. These processes can execute simultaneously on different CPU cores, making multiprocessing suitable for CPU-intensive operations.

    For example, I would use threading for downloading multiple files concurrently and multiprocessing for performing CPU-intensive calculations.

    Communication:
    Threads:
        Shared variables, locks, queues
    Multiprocessing:
        Queues, pipes, shared memory

#### What is a race condition and how will you mitigate

    A race condition occurs when multiple threads access and modify shared mutable data concurrently, and the final result depends on the order of execution. For example, two threads can read the same counter value and both increment it, causing one update to be lost. The GIL does not guarantee protection against such race conditions. We can prevent this by using a threading lock to ensure that only one thread enters the critical section at a time.

    "The main reason we use multithreading in Python is to improve the performance of I/O-bound operations, such as API calls, database queries, and file operations.

    Although the GIL allows only one thread to execute Python bytecode at a time in traditional CPython, when a thread performs an I/O operation, it can release the GIL while waiting. During that time, another thread can execute.

    This allows multiple I/O-bound operations to make progress concurrently and reduces overall waiting time."

#### Scenario: if i wanted to make 10 external api calls

    "I would prefer asyncio for making 10 external API calls because these are I/O-bound operations. Instead of creating and managing multiple OS threads, I can schedule multiple coroutines using asyncio.gather(). Whenever one coroutine waits for an API response, the event loop can switch to another coroutine. This improves resource utilization and allows concurrent execution.

    However, if I'm working with an existing synchronous or blocking library that doesn't support async operations, I would consider multithreading using ThreadPoolExecutor."

## Scenario based django questions

### What happens when user double taps submit to register for account

    A user fills out a registration form and clicks Submit.
    Due to network latency, the user clicks Submit again because they think the first click didn't work.
    As a result, Django receives two POST requests almost simultaneously.

    "When a user submits the registration form multiple times, I would use Django's get_or_create() along with a database-level unique constraint on the email field.

    The unique constraint guarantees that duplicate records cannot be inserted, even if multiple requests arrive simultaneously.

    If the first request creates the user, the second request retrieves the existing user. If both requests initially check before insertion, Django handles the uniqueness conflict and retries the lookup."

### How to prevent double payments for user

    To prevent double payments, I would implement an idempotent payment architecture.

    First, whenever the user initiates a payment, I generate a unique idempotency key for that payment attempt and store it in PostgreSQL with a unique constraint.

    Whenever the frontend sends a payment request, Django checks whether that idempotency key already exists. If it does, I return the existing payment attempt instead of initiating another payment.

    For a new payment attempt, Django creates an order with the payment gateway and stores the gateway order ID.

    After the user completes the payment, I verify the transaction status with the payment gateway and update my local payment record.

    Now, consider a network timeout. The payment gateway might have successfully deducted the amount, but Django may not have received the response. In that situation, I wouldn't immediately mark the payment as failed. I would maintain the payment status as PENDING or UNKNOWN and verify it with the payment gateway.

    For payments that remain unresolved, I would use Celery background tasks with exponential backoff to periodically reconcile the payment status. I would also implement payment gateway webhooks to receive status updates.

    Once I receive a confirmed SUCCESS or FAILED status, I update the database accordingly. If the payment remains unresolved, I keep it pending and escalate it rather than incorrectly marking it as failed.

    Finally, I would ensure that payment processing and order fulfilment are idempotent so that duplicate requests or duplicate webhooks never result in duplicate charges or duplicate order fulfilment.

    "I would use transaction.atomic() with select_for_update() to lock the order row while checking and creating a payment attempt. This ensures concurrent requests for the same order are serialized. Additionally, I would enforce a database-level unique constraint to prevent multiple active payment attempts for the same order. Together, these mechanisms protect against duplicate payment initiation."

### Two users try to book the same movie seat at exactly the same time. How would you prevent both users from booking it?

    "I would use PostgreSQL transactions and select_for_update() to prevent concurrent users from acquiring the same seat.

    When a user requests a seat, I would lock the seat row, check its availability, and change its status from AVAILABLE to HELD. I would also store a hold expiry timestamp, such as five minutes.

    I would commit the transaction immediately and release the database lock. Payment would happen outside the transaction.

    Once payment is verified, I would start another transaction, lock the seat, validate the hold, and update it to CONFIRMED.

    If payment definitively fails or the hold expires, I would release the seat using a background Celery task. For uncertain payment outcomes, I would first verify the gateway status.

    I would also enforce a database constraint to prevent duplicate confirmed bookings."

### If a api takes 8-10 seconds how would you optimize it

    "If a Django API takes 8–10 seconds, I would first measure where the time is being spent rather than immediately optimizing the database.

    I would measure the total API execution time using time.perf_counter() and inspect database query count and execution time.

    I would check for N+1 queries and optimize ORM access using select_related() and prefetch_related().

    Next, I would inspect slow SQL queries using PostgreSQL's EXPLAIN ANALYZE and add appropriate indexes where necessary.

    If database queries aren't the bottleneck, I would profile Python application logic and check external API calls or other blocking operations.

    Finally, I would consider Redis caching, pagination, and reducing unnecessary response data. After each change, I would benchmark again to verify the improvement."

## Celery based questions

    i use @shared_task to register the function as celery task object.
    It makes the task available to Celery's task registration mechanism.
    It allows the task to be discovered and executed by Celery workers.

    1.Why shared_task instead of app.task?
    shared_task is useful in Django applications because it avoids directly coupling individual Django apps to a particular Celery application instance.

    2.what happens when we call a celery task using .delay()
        1.Django calls .delay()
            .delay() is a shortcut for .apply_async().
        2.Celery prepares a task message
            Task name
            Task ID (UUID)
            Arguments and keyword arguments
            Relevant execution options
        3.Message is published to the broker
            Celery's messaging layer (Kombu) communicates with Redis or RabbitMQ and publishes the message to the configured queue.
        4.Celery worker consumes the message
            The worker listens to its configured queues and receives the task message.
        5.Worker executes the task
            It identifies the registered task by its name and executes the corresponding function with the supplied arguments.
        6.Task state/result is stored
            If a result backend is configured, Celery can store the task state and result. Django can retrieve it using the returned task ID.

    3.Difference between .delay() and .apply_async()
        send_email.delay("user@gmail.com")
        send_email.apply_async(
            args=["user@gmail.com"],
            countdown=60,
            queue="email_queue"
        )

        Feature	delay()	apply_async()
        Arguments	Yes	Yes
        Custom queue	No	Yes
        Countdown	No	Yes
        ETA	No	Yes
        Execution options	Limited	Extensive
    Essentially, .delay() is a convenient shortcut for .apply_async().

    Important Note:
    the Django application and Celery worker share the same application code and task definitions, but they run as separate processes/containers.
    The worker must be configured with the same broker connection and must discover the tasks it needs to execute.
    Also, depends_on controls startup order, not necessarily service readiness.

    4. Full defination of celery
        "Celery is a distributed task queue used to execute background tasks asynchronously.

        It consists of four major components: producer, message broker, Celery worker, and result backend.

        The producer can be a Django or FastAPI application. When the application triggers a Celery task using .delay() or .apply_async(), Celery serializes the task information and publishes it to the message broker, such as Redis or RabbitMQ.

        The Celery worker continuously listens to the configured queues, consumes the task messages, and executes the corresponding registered task functions.

        Once execution is completed, the task status and result can be stored in the result backend, such as Redis or PostgreSQL, allowing the application to retrieve the result using the task ID.

        This architecture helps us offload time-consuming operations like sending emails, generating reports, and processing files from the main HTTP request-response cycle."

    5. Redis as message broker and result backend
        Redis as Broker	                Redis as Result Backend
        Stores pending task messages	Stores task execution states/results
        Workers consume messages	    Application retrieves results
        Used for task distribution	    Used for result tracking
        Queue-oriented	                Task-ID-oriented

### A Celery worker picks up a task, executes it successfully, but crashes before acknowledging the message.

    By default, Celery uses early acknowledgement (acks_late=False).
    Celery flow:
        Worker receives the task.
        Worker acknowledges the message to Redis/RabbitMQ.
        Worker executes the task.
        If the worker crashes during execution, the broker has already received the acknowledgement.
    In this case, the task might be lost because the broker considers it acknowledged.

    Code:
    @shared_task(acks_late=True)
    def process_payment(payment_id):
        # Process payment
        pass

    Prevent this:
    acks_late=True
    Celery flow:
        Worker receives the task.
        Worker executes the task.
        If execution succeeds, the worker acknowledges the message.
        If the worker crashes before acknowledgement, the broker may redeliver the message.

    This means the same task can execute more than once.

Real world example:
Imagine a payment-processing task: - Worker processes payment successfully. - Worker crashes before acknowledging the message. - Broker redelivers the message. - Another worker receives the same payment task.
Now you might process the payment twice!

    Therefore, even with acks_late=True, you need idempotency to prevent duplicate processing.

    For example, use a unique payment ID and a database constraint or transaction to ensure that a payment is processed only once.

### How would you design your Django application to ensure that the same task doesn't produce duplicate side effects?

    "When we configure late acknowledgement in Celery, a task can be redelivered if a worker crashes before acknowledging it. This can result in duplicate task execution.

    To prevent duplicate business operations, I would implement idempotency in the application layer. For example, for payment processing, I would generate a unique idempotency key for each payment and maintain its processing status in the database.

    Whenever a worker receives a task, it checks whether the payment has already been successfully processed. If it has, the worker skips the operation. Otherwise, it proceeds with processing.

    I would also use database transactions, appropriate locking and the payment gateway's idempotency mechanism to handle concurrent execution safely."

#### E commerce application

    Whenever a customer places an order:
        1. Save the order in PostgreSQL.
        2. Send an order confirmation email.
        3. Generate an invoice PDF.
        4. Send an SMS notification.

    Would you execute all these operations inside the Django API request, or would you offload some operations to Celery?

    Django transaction.on_commit()
    Django provides a mechanism to execute callbacks only after a database transaction successfully commits.

    Code:
        from django.db import transaction

        with transaction.atomic():

            order = Order.objects.create(
                user=user,
                total_amount=1000
            )

            transaction.on_commit(
                lambda: send_email.delay(order.id)
            )

            transaction.on_commit(
                lambda: generate_invoice.delay(order.id)
            )

            transaction.on_commit(
                lambda: send_sms.delay(order.id)
            )

    We can trigger a celery task only after the order is commited to order table.

    Next question:
    Suppose:
        - PostgreSQL successfully saves the order.
        - transaction.on_commit() executes.
        - Redis is temporarily unavailable.
        - Celery cannot publish the email, invoice and SMS tasks.
    How would you ensure that these tasks are not permanently lost?
        Transactional Outbox Pattern
        Instead of directly publishing tasks to Redis after committing the order, we save an event in a separate PostgreSQL table within

        The same transaction.
        order_id	status
        101	CREATED

        Outbox table
        event_id	event_type	status
        1	SEND_EMAIL	PENDING
        2	GENERATE_INVOICE	PENDING
        3	SEND_SMS	PENDING

        Now we have another background process called an Outbox Publisher.

        Its responsibility:
        1. Periodically fetch pending events from PostgreSQL.
        2. Publish them to Redis.
        3. If publishing succeeds, mark the event as published.
        4. If Redis is unavailable, retain the event as pending and retry later.

        One additional production consideration: if the publisher crashes after successfully publishing an event but before marking it as published, it might publish the same event again. Therefore, consumers must be idempotent.

    Interview ready:
        "I would implement the Transactional Outbox Pattern to ensure reliable background task publishing.

        Instead of directly publishing Celery tasks after the database transaction commits, I would save the order and corresponding events in an Outbox table within the same database transaction.

        A separate publisher process would periodically fetch pending events and publish them to Redis. If Redis is unavailable, the events remain pending and can be retried later.

        I would also implement idempotency because the same event might be published more than once."

### What is the difference between increasing concurrency and increasing the number of worker containers?

    Concurrency means the number of tasks a Celery worker can execute simultaneously.
    Celery can use:
        - Multiprocessing (prefork), commonly the default.
        - Threads.
        - Eventlet or gevent.
        - Solo (one task at a time).
    4 workers with 4 concurrency give 4*4 = 16 tasks are simentanously happening in celery

    Concurrency	                                    Horizontal scaling
    Increases execution slots per worker	        Increases worker instances
    Can increase CPU/memory pressure	            Distributes workload across instances
    Configured using --concurrency	                Achieved by adding worker containers/instances
    Vertical scaling within worker configuration	Horizontal scaling

### How would you prioritize tasks in celery

    "I would implement separate queues using Celery task routing. Payment-related tasks would be routed to a dedicated payment queue, while report-generation tasks would go to a separate reporting queue.

    I would configure dedicated Celery workers for each queue so that long-running reporting tasks cannot block critical payment-related tasks.

    Additionally, Celery supports task-level priorities through apply_async, but I would prefer queue separation for workload isolation."

### How do you cancel a task in celery

    Case 1: Task is still waiting in the queue
            Use revoke()
            Celery broadcasts a revoke message to workers. When a worker encounters that task, it skips execution.

        Code:
        from celery.result import AsyncResult

        task = AsyncResult(task_id)
        task.revoke()

    Case 2: Task is already executing
            task.revoke(terminate=True)
            This terminates the worker process executing that particular task, not necessarily the entire Celery worker or all its concurrent tasks.

            However, killing a worker process can have side effects depending on the execution pool and worker configuration. That's why it isn't recommended as normal application-level cancellation.

    Recommended for case2:
    Consider iam generating excel file with 1 million records and the processing is 6,00,000 lakhs
        Code:
        @shared_task(bind=True)
        def generate_excel(self, user_id):

            chunk_size = 5000

            for offset in range(0, 1000000, chunk_size):

                cancelled = redis_client.get(
                    f"cancel:{self.request.id}"
                )

                if cancelled:
                    return "Task cancelled"

                records = fetch_records(offset, chunk_size)

                process_records(records)

            return "Excel generated successfully"
    Before every chunk processing check is the task cancelled or not by using cancel:task_id
