n = 1
pattern = []
result = {"название": [], "стоимость": [], "количество": [], "ед": []}
while True:
    param = dict()
    prod = input("Введите название Вашего товара: ")
    param["название"] = prod
    result["название"].append(prod)
    cost = float(input("Спасибо. А теперь введите стоимость: "))
    param["строимость"] = cost
    result["стоимость"].append(cost)
    quantity = int(input("Введите количество товара. Количество должно быть целым числом: "))
    param["количество"] = quantity
    result["количество"].append(quantity)
    unit = input("Теперь введите единицу измерения вашего товара: ")
    param["ед"] = unit
    if unit not in result["ед"]:
        result["ед"].append(unit)
    pattern.append((n, param))
    print(f"Информация о товаре {n} заполнена. Хотите добавить ещё один товар?")
    n += 1
    end = input("Для выхода введите 'q'. Чтобы продолжить, 'enter': ")
    if end == "q":
        break
print(pattern)
print(result)
