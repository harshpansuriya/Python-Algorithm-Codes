def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp


def bubbleSort(A):
    totalRun = 0

    for i in A:
        for j in range(len(A) - 1):
            totalRun += 1
            if A[j] > A[j+1]:
                swap(A, j, j+1)
    return A, totalRun


A = [9, 4, 6, 2, 8, 1, 3]
print(bubbleSort(A))
