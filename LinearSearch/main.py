def search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i+1


arr = [2, 5, 8, 9, 10, 16, 22]
target = 10
print(search(arr, target))
