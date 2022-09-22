# Iterative Binary Search

def binaryIterative(arr, start, end, target):
    while start <= end:

        mid = (start + end) // 2
        if arr[mid] < target:
            start = mid + 1

        elif arr[mid] > target:
            end = mid - 1

        else:
            return mid

    return start
    # return -1


# Recursive Binary Search

def binaryRecursive(arr, start, end, target):
    if end >= start:

        mid = start+end-1//2
        if arr[mid] < target:
            binaryRecursive(arr, mid+1, end, target)

        elif arr[mid] > target:
            return binaryRecursive(arr, start, mid - 1, target)

        else:
            return mid

    else:
        return -1


arr = [2, 5, 8, 10, 16, 22, 25]
target = 22

resultIterative = binaryIterative(arr, 0, len(arr) - 1, target)
resultRecursive = binaryRecursive(arr, 0, len(arr) - 1, target)

if resultIterative != -1:
    print("For Iterative binary Search Element is present at index %d" %
          resultIterative)
else:
    print("Element is not present in array")

if resultIterative != -1:
    print("For Recursive binary Search Element is present at index %d" %
          resultRecursive)
else:
    print("Element is not present in array")
