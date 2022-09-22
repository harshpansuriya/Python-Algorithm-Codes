# Multiplying two matrix using nested loops

# 2X2 matrix "X"
X = [[1, 2],
     [2, 3]]

# 2X2 matrix "Y"
Y = [[2, 3],
     [3, 4]]

result = [[0, 0],
          [0, 0]]

for i in range(len(X)):
    for j in range(len(Y[0])):
        for k in range(len(Y)):
            result[i][j] += X[i][k] * Y[k][j]

for end in result:
    print(end)
