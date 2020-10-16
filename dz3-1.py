def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "На ноль делить нельзя!"


print(div(a=int(input("Введите делимое: ")), b=int(input("Введите делитель: "))))



