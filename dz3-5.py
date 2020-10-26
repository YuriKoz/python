def my_func():
    summ = 0
    while True:
        user_str = input("Введите числа через пробел, для выхода нажмите 'q': ").split()
        for el in user_str:
            if el == "q":
                return summ
            summ += int(el)


print(my_func())
