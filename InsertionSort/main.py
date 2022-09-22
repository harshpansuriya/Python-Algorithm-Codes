# Shifting Element

def insertionSort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i -= 1
        A[i+1] = key
    return A


A = [9, 4, 6, 2, 8, 1, 3]
print(insertionSort(A))
