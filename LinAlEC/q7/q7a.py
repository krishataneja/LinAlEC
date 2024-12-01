def det_cofactor(m):
    try:
        if len(m) != len(m[0]):
            return "matrix must be square"
        
        def minor(m1, row, col):
            return [r[:col] + r[col+1:] for r in (m1[:row] + m1[row+1:])]

        def cofactor(mat):
            val = 0
            for i in range(len(m1)):
                sign = (-1) ** i
                submatrix = minor(mat, 0, i)
                val += sign * m1[0][i] * det_cofactor(submatrix)
            return val
        
        if len(m) == 1:
            return m[0][0]
        elif len(m) == 2:
            return m[0][0] * m[1][1] - m[0][1] * m[1][0]
        
        return cofactor(m)
    
    except Exception as e:
        return f"error: {str(e)}"

m1= [[4, 7], [2, 6]]
m2 = [[3, 0, 2], [2, 0, -2], [0, 1, 1]]

print(det_cofactor(m1))
print(det_cofactor(m2))
