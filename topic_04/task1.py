def addition(n1,n2):
    return n1 + n2
def subtraction(n1,n2):
    return n1 - n2
def multiplication(n1,n2):
    return n1 * n2
def division(n1,n2):
    if n2 == 0:
        return "Ділення на 0 не можливе"
    return n1 / n2

def value(promt:str):
    while True:
        try:
            return int(input(promt))
        except ValueError:
            print("Значення невірне (введіть число)")
        
while True:
    print("Додавання: + ")
    print("Віднімання: - ")
    print("Множення: * ")
    print("Ділення: / ")
    print("Вихід: 0 ")

    n1 = value("Введіть значення n1: ")
    n2 = value("Введіть значення n2: ")
    p = (input("Операція, яку треба виконати: ")) 

    if p == "0":
        break

    match p:
        case "+":
            print(addition(n1,n2))
        case "-":
            print(subtraction(n1,n2))
        case "*":
            print(multiplication(n1,n2))  
        case "/":
            print(division(n1,n2))
        case _: 
            print("Невірно введена операція, спробуйте *,/,-,+")