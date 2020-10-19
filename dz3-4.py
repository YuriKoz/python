def my_func(x, y):
    c = 1 / (x ** y)
    return c


print(my_func(x=int(input("Введите целое число: ")),
              y=-int(input("Введите целое отрицательное число : "))))


def my_func1(x, y):
    c = 1 / (x ** abs(y))
    return c


print(my_func1(x=int(input("Введите целое число: ")),
               y=int(input("Введите целое отрицательное число : "))))


def my_func2(x, y):
    c = 1
    d = 1
    while c <= abs(y):
        d *= x
        c += 1
    return 1 / d


print(my_func2(x=int(input("Введите целое число: ")), y=int(input("Введите целое отрицательное число : "))))



