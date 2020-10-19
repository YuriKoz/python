from itertools import count
from itertools import cycle
from itertools import islice

my_list = [1, 22, 43, 56, 98, 123, 2, 12, 150]  # Первый вариант решения
new_list = []
iterator1 = count(0, 3)
iterator2 = cycle(my_list)
print(list(next(iterator1) for _ in range(20)))
print(tuple(next(iterator2) for _ in range(len(my_list + my_list))))


iterator3 = count(15)  # Второй вариант решения
for i in islice(iterator3, 10):
    new_list.append(i)
print(new_list)


def my_cycle_func(start_list, iteration):
    i = 0
    iterator = cycle(start_list)
    while i < 20:
        print(next(iterator), end=" ")
        i += 1


my_cycle_func(start_list=[1, 22, 43, 56, 98, 123, 2, 12, 150], iteration=int(input("Введите число итераций: ")))










