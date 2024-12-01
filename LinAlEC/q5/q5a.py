def inv(A):
    n = len(A)
    m = len(A[0])
    
    if n != m:
        print("matrix is not sqaurw")
        return None
    
    augmnt = [row + [1 if i == j else 0 for j in range(n)] for i, row in enumerate(A)]
    
    for i in range(n):
        if augmnt[i][i] == 0:
            print("cant invert")
            return None
        div = augmnt[i][i]
        augmnt[i] = [x / div for x in augmnt[i]]
        
        for j in range(n):
            if i != j:
                ratio = augmnt[j][i]
                augmnt[j] = [augmnt[j][k] - ratio * augmnt[i][k] for k in range(2 * n)]
    
    inv = [row[n:] for row in augmnt]
    return inv

A = [[4, 7], [2, 6]]
inv_A = inv(A)

if inv_A is not None:
    print("inverse:")
    for row in inv_A:
        print(row)
else:
    print("not invertiable.")
