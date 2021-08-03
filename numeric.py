n = int(input("Введите целое число:"))
print("это оно", n, "?")
print("а это оно в кубе", n**3)  # Возводим число n в степень 3

x = 0b101   # 101 в двоичной системе равно 5
a = 0o11    # 11 в восьмеричной системе равно 9
y = 0x0a        # a в шестнадцатеричной системе равно 10
b = x*y*a
print("b=", b)
print("{0} in binary {0:08b}   in hex {0:02x} in octal {0:02o}".format(b))


def func(t):
    if t > 3:
        if t > 4:
            print("more again")


print(7 % 2)  # Получение остатка от деления числа 7 на 2. Результат - 1
print(7 / 2)  # 3.5
print(7 // 2)  # 3
func(b)

first_number = 2.0001
second_number = 0.1
third_number = first_number + second_number  # 2.1001000000000003
print(round(third_number, 4))  # 2.1001

a = 5
b = 6
result = 5 == 6  # сохраняем результат операции в переменную
print(result)  # False - 5 не равно 6
print(a != b)  # True
print(a > b)  # False - 5 меньше 6
print(a < b)  # True

bool1 = True
bool2 = False
print(bool1 == bool2)  # False - bool1 не равно bool2

age = 22
weight = 58
isMarried = False
result = age > 21 and weight == 58 and isMarried
print(result)  # False, так как isMarried = False
result = age > 21 or isMarried
print(result)  # True, так как выражение age > 21 равно True
print(not age > 21)  # False
print(not isMarried)  # True

name = "Tom"
age = 33
info = "Name: " + name + " Age: " + str(age)
print(info)  # Name: Tom Age: 33

print("Кафе \"Central Perk\"")  # "Central Perk"
str1 = "1a"
str2 = "aa"
str3 = "Aa"
print(str1 > str2)  # False, так как первый символ в str1 - цифра
print(str2 > str3)  # True, так как первый символ в str2 - в нижнем регистре

age = 18
if age >= 21:
    print("Доступ разрешен")
elif age >= 18:
    print("Доступ частично разрешен")
else:
    print("Доступ запрещен")

#! Программа по вычислению факториала
number = int(input("Введите число: "))
i = 1
factorial = 1
while i <= number:
    factorial *= i
    i += 1
print("Факториал числа", number, "равен", factorial)

number = int(input("Введите число: "))
factorial = 1
for i in range(1, number+1):  # функция range ниже
    factorial *= i
print("Факториал числа", number, "равен", factorial)

choice = "y"
while choice.lower() == "y":  # lower преобразует прописные в строчные символы
    print("Привет")
    choice = input(
        "Для продолжения нажмите Y, а для выхода любую другую клавишу: ")
print("Работа программы завешена")

# функция range
range(5)            # 0, 1, 2, 3, 4
range(1, 5)         # 1, 2, 3, 4
range(2, 10, 2)     # 2, 4, 6, 8
range(5, 0, -1)     # 5, 4, 3, 2, 1

for i in range(1, 10):
    for j in range(1, 10):
        # конец строки на каждой итерации равен табуляции
        print(i * j, end="\t")
    print("\n")  # после окончания внешней итерации переход на новую строку

#! Программа Обменный пункт

print("Для выхода нажмите Y")

while True:  # бесконечный цикл
    data = input("Введите сумму для обмена: ")
    if data.lower() == "y":
        break  # выход из цикла
    money = int(data)
    if money < 0:
        print("Сумма должна быть положительной!")
        continue  # переход к новой итерации
    cache = round(money / 56, 2)
    print("К выдаче", cache, "долларов")

print("Работа обменного пункта завершена")


def create_default_user():
    name = "Tom"
    age = 33
    return name, age


user_name, user_age = create_default_user()
print("Name:", user_name, "\t Age:", user_age)
