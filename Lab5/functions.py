def partial_pivot(A, n):
    for i in range(n):
        pivot_row = i

        for j in range(i + 1, n):
            if abs(A[j][i]) > abs(A[pivot_row][i]):
                pivot_row = j

        if pivot_row != i:
            A[i], A[pivot_row] = A[pivot_row], A[i]

        for j in range(i + 1, n):
            factor = A[j][i] / A[i][i]
            A[j] = [A[j][k] - factor * A[i][k] for k in range(n + 1)]

        print([A[i] for i in range(n)])


def back_substitute(A, n):
    x = [None for _ in range(n)]
    for i in range(n - 1, -1, -1):
        sum_val = sum(A[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (A[i][n] - sum_val) / A[i][i]
    return x

def gausian(A, n):
    partial_pivot(A, n)
    return back_substitute(A, n)
