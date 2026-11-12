### Rotate an array left by K positions.

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
