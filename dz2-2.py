user_list = []
n = 0
while True:
    write = input("Заполните список. Когда закончите, щёлкните 'Enter': ")
    if write == "":
        break
    user_list.append(write)
print(f"До преобразования: {user_list}")
while n + 1 < len(user_list):
    user_list[n], user_list[n + 1] = user_list[n + 1], user_list[n]
    n += 2
print(f"После преобразования: {user_list}")


