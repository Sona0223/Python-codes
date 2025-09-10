import numpy as np
rows1 = int(input("Enter number of rows for first matrix: "))
cols1 = int(input("Enter number of columns for first matrix: "))
print("Enter elements of first matrix row-wise (space separated):")
matrix1 = []
for _ in range(rows1):
    row = list(map(int, input().split()))
    matrix1.append(row)
matrix1 = np.array(matrix1)
rows2 = int(input("Enter number of rows for second matrix: "))
cols2 = int(input("Enter number of columns for second matrix: "))
print("Enter elements of second matrix row-wise (space separated):")
matrix2 = []
for _ in range(rows2):
    row = list(map(int, input().split()))
    matrix2.append(row)
matrix2 = np.array(matrix2)
if matrix1.shape == matrix2.shape:
    add = np.add(matrix1, matrix2)
    print("Addition of matrices:\n", add)
else:
    print("Addition not possible. Matrices must have same dimensions.")
if matrix1.shape == matrix2.shape:
    subtract = np.subtract(matrix1, matrix2)
    print("Subtraction of matrices:\n", subtract)
else:
    print("Subtraction not possible. Matrices must have same dimensions.")
print("Transpose of first matrix:\n", np.transpose(matrix1))
print("Transpose of second matrix:\n", np.transpose(matrix2)) 