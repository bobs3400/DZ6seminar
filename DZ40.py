first_elem = int(input("Введите первый элемент: "))
difference = int(input("Введите разность: "))
num_elem = int(input("Введите количество элементов: "))
array = [first_elem]
for i in range(2, num_elem + 1):
    array.append(first_elem + (i - 1) * difference)
print(array)