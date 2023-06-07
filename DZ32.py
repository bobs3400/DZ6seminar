from random import randint
min_element = int(input("Введите минимальное значение: "))
max_element = int(input("Введите максимальное значение: "))
print(array := [randint(0, 100) for _ in range(20)])
res_index = []
for i in range(20):
    if min_element <= array[i] <= max_element:
        res_index.append(i)
print(res_index)