from functools import reduce
new_list = []
[new_list.append(el) for el in range(100, 1001) if el % 2 == 0]
print(reduce(lambda a, b: a * b, new_list))
