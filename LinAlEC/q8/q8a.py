def inner_prod(v1, v2):
    try:
        if len(v1) != len(v2):
            return "they don't have the same dimension"

        res = 0
        for m in range(len(v1)):
            res += v1[m] * v2[m]
        
        return res
    
    except Exception as x:
        return f"error: {str(x)}"

v1 = [1, 3, 5]
v2 = [2, 4, 6]

print(inner_prod(v1, v2))
