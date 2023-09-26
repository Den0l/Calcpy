import math

while True:      
    n1 = input("Введите первое число или один из знаков(cos, sin, tg, sqrt): ")
    if "." in n1: 
       n1 = float(n1)
    else:
        n1 = str(n1)
    if (str(n1).isnumeric()) or (n1 in ["cos", "sin", "tg", "sqrt"]) or (isinstance(n1, float)):
        if n1 in ["cos", "sin", "tg", "sqrt"]:
            z = input("Введите число: ")
            if z == '': break  
            while True:
                if z == '+' or z == '-' or z == '*' or z == '/' or z == '^':
                    print("Неверные данные, повторите ввод: ")
                    z = input()
                else: break  
            if n1 == 'sqrt':
                while True:
                    if float(z) > 0: 
                        print(math.sqrt(float(z))) #квадратный корень
                        break
                    else:
                        print("Квадратный корень из отрицательного числа не вычисляется, повторите ввод: ")
                        z = input()
            elif n1 == 'cos': print(math.cos(float(z))) #косинус
            elif n1 == 'sin': print(math.sin(float(z))) #синус
            elif n1 == 'tg': print(math.tan(float(z))) #тангенс
        elif (str(n1).isnumeric()) or (isinstance(n1, float)):    
            z = input("Введите знак(+, -, *, /, ^, !): ")
            if z == '': break
            while True:  
                if z.isnumeric() or z.isalpha():
                    print("Неверные данные, повторите ввод: ")
                    z = input()
                else: break
            if z == '!': 
                print(math.factorial(int(n1)))#факториал 
                continue
            n2 = input("Введите 2 число: ") 
            if "." in n2: 
                n2 = float(n2)
            else:
                n2 = str(n2)
            if n2 == '': break
            while True:
                if (str(n2).isnumeric()) or (isinstance(n2, float)):
                    break
                else:
                    print("Неверные данные, повторите ввод: ")
                    n2 = input()
            if z == '+': print(round(float(n1) + float(n2), 2)) #сложение
            elif z == '-': print(round(float(n1) - float(n2), 2)) #вычитание
            elif z == '*': print(round(float(n1) * float(n2), 2)) #умножение
            elif z == '/':
                while True:
                    if n2 == "0": 
                        print("Делить на ноль нельзя, повторите ввод: ")
                        n2 = float(input())
                    else:
                        print(round(float(n1) / float(n2), 2))#деление
                        break
            elif z == '^': print(round(float(n1) ** float(n2), 2)) #степень
    elif n1 == '': break
    else: print("Неверные данные, повторите ввод.")