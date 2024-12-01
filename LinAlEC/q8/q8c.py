
def gram_schmidth(A):
    try:
        def proj(v, u):
            dot = sum(v[i] * u[i] for i in range(len(v)))
            norm_u = sum(u[i] * u[i] for i in range(len(u)))
            return [dot / norm_u * u[i] for i in range(len(u))]
        
        def subtract(v, pr):
            return [v[i] - pr[i] for i in range(len(v))]
        
        orthoset = []
        for t in A:
            for orthovector in orthoset:
                pr = proj(t, orthovector)
                t = subtract(t, pr)
            orthoset.append(t)
        
        return orthoset
    
    except Exception as r:
        return f"errror: {str(r)}"

A= [[1, 2], [2, 3], [3, 4]]
print(gram_schmidth(A))
