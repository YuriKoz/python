start_list = [8, 6, 4, 4, 3]
print(f"Текущий рейтинг: {start_list}")
numb = int(input("Введите новый элемент рейтинга: "))
coun = start_list.count(numb)
for el in start_list:
    if coun > 0:
        little = start_list.index(numb)
        start_list.insert(little + coun, numb)
        break
    else:
        if numb > el:
            big = start_list.index(el)
            start_list.insert(big, numb)
            break
        elif numb < start_list[len(start_list) - 1]:
            start_list.append(numb)
print(f"Теперь рейтинг выглядит вот так: {start_list}")

