def solveNQueens(n):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col:
                return False
        for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
            if board[i] == j:
                return False
        for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
            if board[i] == j:
                return False
        return True

    def solve(row):
        if row == n:
            result.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                solve(row + 1)
                board[row] = -1

    def create_output(board):
        solution = []
        for i in range(n):
            row = ['.'] * n
            row[board[i]] = 'Q'
            solution.append("".join(row))
        return solution

    result = []
    board = [-1] * n
    solve(0)

    final_result = [create_output(solution) for solution in result]
    final_result.sort()   
    return final_result

n = int(input("Enter the value of n: "))
solutions = solveNQueens(n)
for solution in solutions:
    for row in solution:
        print(row)
    print()
