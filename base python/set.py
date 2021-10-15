# Множество (set) представляют еще один вид набора элементов.множество содержит только уникальные значения.
users = {"Tom", "Bob", "Alice", "Tom"}
print(users)    # {"Tom","Bob","Alice"}
# Также для определения множества может применяться функция set(), в которую передается список или кортеж элементов
users3 = set(["Mike", "Bill", "Ted"])
users = {"Tom", "Bob", "Alice"}
print(len(users))   # 3
users = set()
users.add("Sam")
print(users)
users = {"Tom", "Bob", "Alice"}

user = "Tom"
if user in users:
    users.remove(user)
print(users)    # {"Bob", "Alice"}
# Также для удаления можно использовать метод discard(), который не будет генерировать исключения при отсутствии элемента
user = "Tim"
users.discard(user)
# Для удаления всех элементов вызывается метод clear():
users.clear()
# С помощью метода copy() можно скопировать содержимое одного множества в другую переменную
users = {"Tom", "Bob", "Alice"}
users3 = users.copy()
# Метод union() объединяет два множества и возвращает новое множество:
users = {"Tom", "Bob", "Alice"}
users2 = {"Sam", "Kate", "Bob"}

users3 = users.union(users2)
print(users3)   # {"Bob", "Alice", "Sam", "Kate", "Tom"}
# Метод intersection() производит операцию пересечения множеств и возвращает новое множество:
users3 = users.intersection(users2)
print(users3)   # {"Bob"}
print(users & users2)   # {"Bob"}
# Для получения разности множеств можно использовать метод difference или операцию вычитания:

users3 = users.difference(users2)
print(users3)           # {"Tom", "Alice"}
print(users - users2)   # {"Tom", "Alice"}
# Метод issubset позволяет выяснить, является ли текущее множество подмножеством (то есть частью) другого множества:
users = {"Tom", "Bob", "Alice"}
superusers = {"Sam", "Tom", "Bob", "Alice", "Greg"}

print(users.issubset(superusers))   # True
print(superusers.issubset(users))   # False
# Метод issuperset, наоборот, возвращает True, если текущее множество является надмножеством (то есть содержит) для другого множества:

print(users.issuperset(superusers))   # False
print(superusers.issuperset(users))   # True
# Тип frozen set является видом множеств, которое не может быть изменено.
users = frozenset({"Tom", "Bob", "Alice"})
