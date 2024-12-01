def cholesky_decomp(m):
    try:
        size = len(m)
        lower = [[0 for _ in range(size)] for _ in range(size)]
        for x in range(size):
            for y in range(x + 1):
                temp_sum = sum(lower[x][k] * lower[y][k] for k in range(y))
                if x == y:
                    lower[x][y] = (m[x][y] - temp_sum) ** 0.5
                else:
                    lower[x][y] = (m[x][y] - temp_sum) / lower[y][y]
        return lower
    except Exception as r:
        return f"errord: {str(r)}"

m = [[4, 12, -16], [12, 37, -43], [-16, -43, 98]]
L = cholesky_decomp(m)
print("lower triangular matrix then will be:", L)


