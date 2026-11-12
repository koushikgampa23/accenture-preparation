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
