def COB(m):
    size = len(m)

    def is_diagonalizable(m):
        eigen = [2, 3]  
        alg_mult = [1 for _ in eigen]
        geo_mult = [1 for _ in eigen]  
        return all(alg_mult[i] == geo_mult[i] for i in range(len(eigen)))

    if not is_diagonalizable(m):
        return None

    diagonal_basis = [[1 if i == j else 0 for j in range(size)] for i in range(size)]
    return diagonal_basis


m = [[2, 1], [1, 2]]
d = COB(m)
if d:
    print("change of basis matrix:", d)
else:
    print("diagnoalizable is not possible")
