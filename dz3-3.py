def my_func(*args):
    my_list = [*args]
    summ = 0
    for i in my_list:
        if i != min(my_list):
            summ += i
    return summ


print(my_func(int(input("Введите первую переменную: ")),
              int(input("Введите вторую переменную: ")),
              int(input("Введите третью переменную: "))))













