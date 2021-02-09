# 1 Задание

a = 15
print(a)
b = 25
print(b)
c = a + b
print(c)

number = input("Введите число > ")
print(number)
name = input("Введите имя > ")
print(name)

# 2 Задание

time = int(input("Введите время в секундах > "))
hours = time // 3600
rest = time % 3600
minutes = rest // 60
seconds = rest % 60
print(f"Время: {hours}:{minutes}:{seconds}")

# 3 задание

n = input("Введите число > ")
a = int(n + n)
b = int(n + n + n)
summ = int(n) + a + b
print(summ)

# 4 Задание

number = input("Введите число > ")
x = 0
for i in number:
    while int(i) > x:
        x = int(i)
print(f"Самая большая цифра: {x}")

# 5 Задание

revenue = int(input("Введите значение выручики:  "))
costs = int(input("Введите значение издержек:  "))
profit = revenue - costs

if profit >= 0:
    print(f"Выручка фирмы составляет: {profit}")
else:
    print(f"Убыток фирмы составляет: {profit}")

if profit > 0:
    profitability = int(profit / revenue * 100)
    print(f"Реантабельность фирмы составляет: {profitability} %")
    workers = int(input("Введите количество сотрудников в фирме: "))
    profit_on_workers = int(profit / workers)
    print(f"Прибыль фирмы на одного сотрудника составляет: {profit_on_workers}")
else:
    print("Фирма не рентабельна")

# 6 Задание

result = float(input("Текущий результат: "))
target = float(input("Требуемый результат: "))
day = 1

if result < target:
    while result < target:
        result = result + (result / 10)
        day += 1
        print(f"На {day} день спортсмен достиг результата - не менее {result} км")
