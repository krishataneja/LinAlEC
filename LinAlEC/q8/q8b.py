def is_ortho(v1, v2):
    try:
        if len(v1) != len(v2):
            return "they dont have same dimension"

        b= 0
        for i in range(len(v1)):
            b += v1[i] * v2[i]
        
        if b == 0:
            return True
        return False
    
    except Exception as r:
        return f"error: {str(r)}"

v1 = [1, 2, 3]
v2 = [-3, 2, 1]

print(is_ortho(v1, v2))
