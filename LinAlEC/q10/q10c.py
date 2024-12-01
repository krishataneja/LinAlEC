def svd(A):
    def transp(mat): return [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]
    def multiply(a, b): return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
    def eig(mat): 
        n = len(mat)
        v = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
        for _ in range(50):
            for i in range(n):
                for j in range(i + 1, n):
                    if abs(mat[i][j]) > 1e-9:
                        t = (mat[j][j] - mat[i][i]) / (2 * mat[i][j])
                        c = (1 / (1 + t**2)**0.5)
                        s = t * c
                        r = [[1 if p == q else 0 for q in range(n)] for p in range(n)]
                        r[i][i], r[j][j], r[i][j], r[j][i] = c, c, s, -s
                        mat = multiply(multiply(transp(r), mat), r)
                        v = multiply(v, r)
        return [mat[i][i] for i in range(n)], v

    t = transp(A)
    m_mult = multiply(t, A)
    eig_vals, u = eig(m_mult)
    s = [[eig_vals[i]**0.5 if i == j else 0 for j in range(len(eig_vals))] for i in range(len(eig_vals))]
    v_t = multiply(multiply(u, s), transp(A))
    return u, s, v_t

A = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
U, S, V_t = svd(A)
print("U :", U)
print("S :", S)
print("Vt :", V_t)
