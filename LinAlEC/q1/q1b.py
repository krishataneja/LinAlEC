class Vector:
    def __init__(self, s, dt="real"):
        
        if dt not in ["real", "complex"]:
            raise ValueError("data must be real or complex")
        self.s = s
        self.dt = dt
        self.elem = []

    def populate(self, items):
       
        if len(items) != self.s:
            raise ValueError(f"vector needs {self.s} elements.")
        
       
        for v in items:
            if self.dt == "real" and not isinstance(v, (int, float)):
                raise TypeError("elements must be real.")
            if self.dt == "complex" and not isinstance(v, (int, float, complex)):
                raise TypeError("elements must be compelx")

        self.elem = items

    def display(self):
       
        print(f"vector: {self.dt}, length: {self.s}, elem: {self.elem}")

    def __str__(self):
       
        return f"vector({self.dt}, size={self.s}): {self.elem}"



if __name__ == "__main__":
   
    real_vec = Vector(4, dt="real")
    real_vec.populate([5.1, -2.3, 3.8, 0.0])
    real_vec.display()

   
    complex_vec = Vector(3, dt="complex")
    complex_vec.populate([2 + 1j, -3j, 4.5])
    complex_vec.display()
