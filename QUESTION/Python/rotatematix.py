def rotate_matrix(matrix):
    n = len(matrix)
    
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    for i in range(n):
        matrix[i].reverse()
    
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

n = int(input())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

rotated_matrix = rotate_matrix(matrix)
print_matrix(rotated_matrix)
