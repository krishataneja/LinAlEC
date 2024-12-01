def det_PLU(A):
    try:
        if len(A) != len(A[0]):
            return "matrix must be squared"

        def permute(m, p):
            return [m[i] for i in p]

        def plu_decomp(m):
            n = len(m)
            pe = list(range(n))
            l = [[0] * n for _ in range(n)]
            u = [row[:] for row in m]
            for i in range(n):
                pivotr = max(range(i, n), key=lambda x: abs(u[x][i]))
                if pivotr != i:
                    u[i], u[pivotr] = u[pivotr], u[i]
                    pe[i], pe[pivotr] = pe[pivotr], pe[i]
                for j in range(i + 1, n):
                    if u[i][i] == 0:
                        return "matrix is singular"
                    ratio = u[j][i] / u[i][i]
                    l[j][i] = ratio
                    for k in range(i, n):
                        u[j][k] -= ratio * u[i][k]
            for i in range(n):
                l[i][i] = 1
            return l, u, pe

        l, u, pe = plu_decomp(A)
        det = 1
        for i in range(len(u)):
            det *= u[i][i]
        if pe != list(range(len(A))):
            det *= -1
        return det
    
    except Exception as r:
        return f"error: {str(r)}"

m1 = [[4, 7], [2, 6]]
m2 = [[3, 0, 2], [2, 0, -2], [0, 1, 1]]

print(det_PLU(m1))
print(det_PLU(m2))
