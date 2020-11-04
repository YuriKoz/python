n = abs(int(input("Введите целое число: ")))
factorial = 1


def fact(n):
    if n == 0:
        print(f"{n}! = 1")
    for i in range(1, n + 1):
        yield i


for el in fact(n):
    factorial *= el
    print(f"{n}! = {' * '.join([str(el) for el in fact(n)])} = {factorial}")
