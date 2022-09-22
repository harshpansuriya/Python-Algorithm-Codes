def bubbleSort(A):
    totalRun = 0
    for i in range(len(A)):
        for j in range(len(A)-i-1):
            totalRun += 1
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    return A, totalRun


A = [9, 4, 6, 2, 8, 1, 3]
print(bubbleSort(A))
