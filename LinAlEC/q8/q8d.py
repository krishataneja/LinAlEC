def qr_factorisation(A):
    try:
        def dot_product(v1, v2):
            return sum(v1[i] * v2[i] for i in range(len(v1)))
        
        def vector_norm(v):
            return sum(v[i] * v[i] for i in range(len(v))) ** 0.5
        
        def scalar_multiply(scalar, v):
            return [scalar * v[i] for i in range(len(v))]
        
        def vector_subtract(v1, v2):
            return [v1[i] - v2[i] for i in range(len(v1))]

        def qr_orthogonalisation(A):
            n = len(A[0])
            m = len(A)
            q = []
            r = [[0] * n for _ in range(n)]
            
            for j in range(n):
                v = [A[i][j] for i in range(m)]
                for i in range(j):
                    proj = scalar_multiply(dot_product(v, q[i]) / dot_product(q[i], q[i]), q[i])
                    v = vector_subtract(v, proj)
                r[j][j] = vector_norm(v)
                q.append(scalar_multiply(1 / r[j][j], v))
                
            return q, r

        q, r = qr_orthogonalisation(A)
        return q, r
    
    except Exception as x:
        return f"errora: {str(x)}"

A = [[1, 2], [3, 4], [5, 6]]
Q, R = qr_factorisation(A)
print("Q:", Q)
print("R:", R)
