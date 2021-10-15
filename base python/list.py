# списки
import copy

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers2 = list(numbers)
print(numbers[0])   # 1
print(numbers[2])   # 3
print(numbers[-1])  # 9

numbers = [5] * 6  # [5, 5, 5, 5, 5, 5]
print(numbers)

numbers = list(range(10))
print(numbers)      # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers = list(range(2, 10))
print(numbers)      # [2, 3, 4, 5, 6, 7, 8, 9]
numbers = list(range(10, 2, -2))
print(numbers)      # [10, 8, 6, 4]

objects = [1, 2.6, "Hello", True]  # списки могут включать разные типы

companies = ["Microsoft", "Google", "Oracle", "Apple"]
for item in companies:
    print(item)
i = 0
while i < len(companies):  # len передает длину списка
    print(companies[i])
    i += 1

users = ["Tom", "Bob"]
# операции со списками
# добавляем в конец списка
users.append("Alice")  # ["Tom", "Bob", "Alice"]
# добавляем на вторую позицию
users.insert(1, "Bill")          # ["Tom", "Bill", "Bob", "Alice"]

# получаем индекс элемента
i = users.index("Tom")
# удаляем по этому индексу
removed_item = users.pop(i)            # ["Bill", "Bob", "Alice"]

last_user = users[-1]
# удаляем последний элемент
users.remove(last_user)           # ["Bill", "Bob"]
# проверка наличия элемента перед удалением
user = "Bob"
if user in users:
    users.remove(user)

print(users)

# удаляем все элементы
users.clear()

users = ["Tom", "Bob", "Alice", "Tom", "Bill", "Tom"]
users_count = users.count("Tom")  # счет кол-ва нужных элементов
print(users_count)      # 3
# сортировка элементов по алгоритму ключ функции
sorted_users = sorted(users, key=str.lower)
users.sort()  # сортировка элементов - цифровой символ считается "меньше", чем алфавитный заглавный символ, а заглавный символ считается меньше, чем строчный!
print(users)      # ["Alice", "Bill", "Bob", "Tom", "Tom", "Tom"]
users.reverse()  # обратная сортировка элементов
print(users)      # ["Tom", "Tom", "Tom", "Bob", "Bill", "Alice"]

numbers = [9, 21, 12, 1, 3, 15, 18]
print(min(numbers))     # 1
print(max(numbers))     # 21

# копирование списков - так как списки являются объектами ссылочного типа, то при изменении одного, изменится и копия
users1 = ["Tom", "Bob", "Alice"]
users2 = users1
users2.append("Sam")
# users1 и users2 указывают на один и тот же список
print(users1)   # ["Tom", "Bob", "Alice", "Sam"]
print(users2)   # ["Tom", "Bob", "Alice", "Sam"]
# Для того чтобы этого не было и указывали на разные списки можно использовать метод deepcopy(), который определен во встроенном модуле copy (подключить)
users2 = copy.deepcopy(users1)
users2.append("Sam")
# пееменные users1 и users2 указывают на разные списки
print(users1)   # ["Tom", "Bob", "Alice"]
print(users2)   # ["Tom", "Bob", "Alice", "Sam"]

# Копирование части списка
users = ["Tom", "Bob", "Alice", "Sam", "Tim", "Bill"]

slice_users1 = users[:3]   # с 0 по 3
print(slice_users1)   # ["Tom", "Bob", "Alice"]

slice_users2 = users[1:3]   # с 1 по 3
print(slice_users2)   # ["Bob", "Alice"]

slice_users3 = users[1:6:2]   # с 1 по 6 с шагом 2
print(slice_users3)   # ["Bob", "Sam", "Bill"]

# Соединение списков
users1 = ["Tom", "Bob", "Alice"]
users2 = ["Tom", "Sam", "Tim", "Bill"]
users3 = users1 + users2
print(users3)   # ["Tom", "Bob", "Alice", "Tom", "Sam", "Tim", "Bill"]

# Списки списков
users = [
    ["Tom", 29],
    ["Alice", 33],
    ["Bob", 27]
]

print(users[0])         # ["Tom", 29]
print(users[2][0])      # Bob
print(users[0][1])      # 29

# создание вложенного списка
user = list()
user.append("Bill")
user.append(41)
# добавление вложенного списка
users.append(user)

print(users[-1])         # ["Bill", 41]

# добавление во вложенный список
users[-1].append("+79876543210")

print(users[-1])         # ["Bill", 41, "+79876543210"]

# удаление последнего элемента из вложенного списка
users[-1].pop()
print(users[-1])         # ["Bill", 41]

# удаление всего последнего вложенного списка
users.pop(-1)

# изменение первого элемента
users[0] = ["Sam", 18]
print(users)            # [ ["Sam", 18], ["Alice", 33], ["Bob", 27]]

# Перебор вложенных списков
for user in users:
    for item in user:
        # в конце каждой строки вывода итерации добавиться символ
        print(item, end=" | ")

# del variable удаление переменной
# del obj.attr удаление атрибута
# del data[k] удаление элемента по индексу
# del data[i:j] удаление элементов по срезу
list_one = ['spam', 1, 11, 111]
list_two = [2, 22, 'spam', 222]
list_three = [3, 'spam', 33, 333]
# удаляем spam одновременно из трёх списков
del list_one[0], list_two[2], list_three[1]
# добавление нескольких элементов в список
my_list = []
my_list.extend([1, 2, 3])  # None
print(my_list)  # [1, 2, 3]
