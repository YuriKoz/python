user_input = input("Введите несколько слов через пробел: \n")
for ind, el in enumerate(user_input.split(), 1):
    if len(el) > 10:
        print(ind, el[:10])
    else:
        print(ind, el)




