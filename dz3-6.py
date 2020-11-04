def my_func():
    user_inp = input("Введите латинские буквы через пробел: \n")
    for el in user_inp.split():
        letters = 0
        for i in el:
            if 97 <= ord(i) <= 122:
                letters += 1
        print(el.title() if letters == len(el) else f"{el} - Можно вводить только латинские буквы!")


my_func()
