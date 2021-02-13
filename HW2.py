# Задание 1

my_types = [
    None, b"10,15,25", bytearray(b'15, A, b'), (5 < 10), {'name': "Alex", 'age': '15'}, frozenset({'1', 'b'}),
    {'A', '1', }, ('1', 'A', 'b'), ['1, A, b'], "Hello", 10.5, 57]

for i in my_types:
    print(f'{i} is {type(i)}')

# Задание 2

my_list = list(input("Введита числа: "))

for i in range(1, len(my_list), 2):
    my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]
print(my_list)

# Задание 3

mouth = int(input("Введите номер месяца: "))
seasons_list = ['winter', 'spring', 'summer', 'autumn']

if mouth == 1 or mouth == 2 or mouth == 12:
    print(seasons_list[0])
elif mouth == 4 or mouth == 5 or mouth == 6:
    print(seasons_list[1])
elif mouth == 6 or mouth == 7 or mouth == 8:
    print(seasons_list[2])
elif mouth == 9 or mouth == 10 or mouth == 11:
    print(seasons_list[3])

#

mouth = int(input("Введите номер месяца: "))
seasons_dict = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'autumn'}

if mouth == 1 or mouth == 2 or mouth == 12:
    print(seasons_dict.get(1))
elif mouth == 4 or mouth == 5 or mouth == 6:
    print(seasons_dict.get(2))
elif mouth == 6 or mouth == 7 or mouth == 8:
    print(seasons_dict.get(3))
elif mouth == 9 or mouth == 10 or mouth == 11:
    print(seasons_dict.get(4))

# Задание 4

words = input("Введите слова: ")
a = words.split(' ')
for i, el in enumerate(a, 1):
    if len(el) > 10:
        el = el[0:10]
    print(f"{i} - {el}")

# Задание 5

my_list = [10, 7, 4, 0]
number = int(input("Введите число: "))
c = my_list.count(number)

for el in my_list:
    if c > 0:
        i = my_list.index(number)
        my_list.insert(i + c, number)
        break
    else:
        if number > el:
            j = my_list.index(el)
            my_list.insert(j, number)
            break
        elif number < my_list[len(my_list) - 1]:
            my_list.append(number)
print(my_list)
