class LinearSystem:
    def __init__(self, A, b):
        self.A = A
        self.b = b
        if len(A) != len(b):
            raise ValueError("Error: Number of rows in A must match the size of b.")
        for row in A:
            if len(row) != len(A[0]):
                raise ValueError("Error: All rows in A must have the same number of columns.")

    def display(self):
        print("Matrix A:")
        for row in self.A:
            print(row)
        print("Vector b:")
        for value in self.b:
            print(value)

# Example usage
A_example = [
    [2, 3],
    [4, 5]
]
b_example = [6, 7]

try:
    system = LinearSystem(A_example, b_example)
    system.display()
except ValueError as e:
    print(e)
