class ComplexNumber:
    def __init__(s, r, i):
        s.r = r
        s.i = i

    def __repr__(s):
        return f"{s.r} + {s.i}i" if s.i >= 0 else f"{s.r} - {-s.i}i"

    def __add__(s, other):
        return ComplexNumber(s.r + other.r, s.i + other.i)

    def __mul__(s, other):
        real_part = s.r * other.r - s.i * other.i
        imag_part = s.r * other.i + s.i * other.r
        return ComplexNumber(real_part, imag_part)

    def __truediv__(s, other):
        if other.r == 0 and other.i == 0:
            raise ValueError("cant be dividwd")
        d = other.r ** 2 + other.i ** 2
        real_part = (s.r * other.r + s.i * other.i) / d
        imag_part = (s.i * other.r - s.r * other.i) / d
        return ComplexNumber(real_part, imag_part)

    def __abs__(s):
        return (s.r ** 2 + s.i ** 2) ** 0.5

    def cc(s):
        return ComplexNumber(s.r, -s.i)


a = ComplexNumber(3, 4)
b = ComplexNumber(1, -2)

print("CN1:", a)
print("CN2:", b)
print("a + b:", a + b)
print("a * b:", a * b)
print("a / b:", a / b)
print("|a|:", abs(a))
print("conjugate of a", a.cc())
