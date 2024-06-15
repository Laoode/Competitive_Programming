arr = [1, 2, 3, 4]
arr.append(5)
print(arr)  # Output: [1, 2, 3, 4, 5]


arr = [1, 2, 3, 4, 5]
arr.remove(3)
print(arr)  # Output: [1, 2, 4, 5]

arr = [10, 20, 30, 40, 50]
print(arr[1])  # Output: 20


arr = [10, 20, 30, 40, 50]
arr[2] = 35
print(arr)  # Output: [10, 20, 35, 40, 50]


arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
arr3 = arr1 + arr2
print(arr3)  # Output: [1, 2, 3, 4, 5, 6]


arr = [4, 2, 3, 1, 5]
arr.sort()
print(arr)  # Output: [1, 2, 3, 4, 5]


arr = [1, 2, 3, 4, 5, 6, 7]
print(len(arr))  # Output: 7


arr = [1, 2, 2, 3, 2, 4, 5]
print(arr.count(2))  # Output: 3


arr = [1, 2, 3, 4, 5]
print(arr.index(4))  # Output: 3


arr = [1, 2, 3, 4, 5]
arr.reverse()
print(arr)  # Output: [5, 4, 3, 2, 1]

// except ValueError:
    