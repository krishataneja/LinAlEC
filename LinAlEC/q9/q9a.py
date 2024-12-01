def find_roots():
    degree = int(input("Enter the degree of the polynomial: "))
    coefficients = [complex(input(f"Enter coefficient for x^{i}: ")) for i in range(degree + 1)]
    roots = [complex(i, i) for i in range(1, degree + 1)]
    iterations = 100
    tolerance = 1e-10

    for _ in range(iterations):
        for i in range(degree):
            numerator = sum(coefficients[j] * (roots[i] ** j) for j in range(degree + 1))
            denominator = 1
            for j in range(degree):
                if i != j:
                    denominator *= (roots[i] - roots[j])
            correction = numerator / denominator
            roots[i] -= correction
        if all(abs(sum(coefficients[j] * (root ** j) for j in range(degree + 1))) < tolerance for root in roots):
            break

    for i, root in enumerate(roots):
        print(f"Root {i + 1}: {root}")

find_roots()
