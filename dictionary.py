# словари
# определение
# dictionary = { ключ1:значение1, ключ2:значение2, ....}
users = {1: "Tom", 2: "Bob", 3: "Bill"}
elements = {"Au": "Золото", "Fe": "Железо", "H": "Водород", "O": "Кислород"}
objects = {1: "Tom", "2": True, 3: 100.6}
# пустой словарь
objects = {}
objects = dict()
# Преобразование из списка или кортежа в словарь
users_list = [
    ["+111123455", "Tom"],
    ["+384767557", "Bob"],
    ["+958758767", "Alice"]
]
users_dict = dict(users_list)
# {"+111123455": "Tom", "+384767557": "Bob", "+958758767": "Alice"}

print(users_dict)
users_tuple = (
    ("+111123455", "Tom"),
    ("+384767557", "Bob"),
    ("+958758767", "Alice")
)
users_dict = dict(users_tuple)
print(users_dict)
# Получение и изменение элементов
# dictionary[ключ]
users = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"
}

# получаем элемент с ключом "+11111111"
print(users["+11111111"])      # Tom

# установка значения элемента с ключом "+33333333", Если при установке значения элемента с таким ключом в словаре не окажется, то произойдет его добавление
# Но если мы попробуем получить значение с ключом, которого нет в словаре, то Python сгенерирует ошибку KeyError
users["+33333333"] = "Bob Smith"
print(users["+33333333"])      # Bob Smith
key = "+4444444"
if key in users:  # проверка наличия элемента с таким ключом
    user = users[key]
    print(user)
else:
    print("Элемент не найден")
# для получения элементов можно использовать метод get
# get(key): возвращает из словаря элемент с ключом key. Если элемента с таким ключом нет, то возвращает значение None
# get(key, default): возвращает из словаря элемент с ключом key. Если элемента с таким ключом нет, то возвращает значение по умолчанию default
key = "+55555555"
user = users.get(key)
user = users.get(key, "Unknown user")
# Для удаления элемента по ключу применяется оператор del
del users["+55555555"]
# удаление с проверкой
if key in users:
    user = users[key]
    del users[key]
    print(user, "удален")
else:
    print("Элемент не найден")
# Другой способ удаления представляет метод pop()
# pop(key): удаляет элемент по ключу key и возвращает удаленный элемент. Если элемент с данным ключом отсутствует, то генерируется исключение KeyError
# pop(key, default): удаляет элемент по ключу key и возвращает удаленный элемент. Если элемент с данным ключом отсутствует, то возвращается значение default
users["+55555555"] = "Bob Smith"  # добавили
key = "+55555555"
user = users.pop(key)
print(user)

user = users.pop("+4444444", "Unknown user")
print(user)
# Если необходимо удалить все элементы
users.clear()
# Копирование словарей
users = {"+1111111": "Tom", "+3333333": "Bob", "+5555555": "Alice"}
users2 = users.copy()
# объединение словарей
users = {"+1111111": "Tom", "+3333333": "Bob", "+5555555": "Alice"}

users2 = {"+2222222": "Sam", "+6666666": "Kate"}
users.update(users2)
# При этом словарь users2 остается без изменений. Изменяется словарь users, в который добавляются элементы другого словаря

print(users)
# {"+1111111": "Tom", "+3333333": "Bob", "+5555555": "Alice", "+2222222": "Sam", "+6666666": "Kate"}
print(users2)   # {"+2222222": "Sam", "+6666666": "Kate"}
# если необходимо, чтобы оба исходных словаря были без изменений, а результатом объединения был какой-то третий словарь
# то можно предварительно скопировать один словарь в другой
users3 = users.copy()
users3.update(users2)
# Перебор словаря
users = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"
}
for key in users:
    print(key, " - ", users[key])
# Метод items() возвращает набор кортежей. Каждый кортеж содержит ключ и значение элемента, которые при переборе мы тут же можем получить в переменные key и value
for key, value in users.items():
    print(key, " - ", value)
