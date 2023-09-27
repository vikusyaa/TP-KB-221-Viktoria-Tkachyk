a = float(input("Введіть першу цифру: "))
b = float(input("Введіть другу цифру: "))
c = float(input("Введіть третю цифру: "))
import math

def solve_quadratic(a, b, c):
    
    D = b**2 - 4*a*c
    
    if D < 0:
        
        return "Розв'язків немає"
    elif D == 0:
        
        x = -b / (2*a)
        return f"Один розв'язок: x = {x}"
    else:
        
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        return f"Два розв'язки: x1 = {x1}, x2 = {x2}"


result = solve_quadratic(a, b, c)
print(result)
    