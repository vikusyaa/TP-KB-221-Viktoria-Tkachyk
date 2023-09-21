def discriminant(a, b, c):
    D = b**2 - 4*a*c
    return D
a = float(input("Перша цифра:"))
b = float(input("Друга цифра:"))
c = float(input("Третя цифра:"))
print(discriminant(a, b, c))