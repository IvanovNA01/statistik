# Кортеж (tuple) представляет последовательность элементов, кортеж является неизменяемым (immutable) типом
# объявления
user = ("Tom", 23)
user = "Tom", 23
user = ("Tom",)
# передача списка в кортеж
users_list = ["Tom", "Bob", "Kate"]
users_tuple = tuple(users_list)
print(users_tuple)      # ("Tom", "Bob", "Kate")

users = ("Tom", "Bob", "Sam", "Kate")
print(users[0])     # Tom
print(users[2])     # Sam
print(users[-1])     # Kate

# получим часть кортежа со 2 элемента по 4
print(users[1:4])       # ("Bob", "Sam", "Kate")

# можем разложить кортеж на отдельные переменные
user = ("Tom", 22, False)
name, age, isMarried = user
print(name)             # Tom
print(age)              # 22
print(isMarried)        # False
# перебор кортежей
for item in user:
    print(item)

i = 0
while i < len(user):
    print(user[i])
    i += 1

name = "Tom"
if name in user:
    print("Пользователя зовут Tom")
else:
    print("Пользователь имеет другое имя")

# возврат из функции


def get_user():
    name = "Tom"
    age = 22
    is_married = False
    return name, age, is_married


user = get_user()
print(user[0])              # Tom
print(user[1])              # 22
print(user[2])              # False
# сложные кортежи
countries = (
    ("Germany", 80.2, (("Berlin", 3.326), ("Hamburg", 1.718))),
    ("France", 66, (("Paris", 2.2), ("Marsel", 1.6)))
)  # кортеж countries состоит из 2х кортежей, которые включают в себя кортежи, состоящие из других кортежей

for country in countries:
    countryName, countryPopulation, cities = country
    print("\nCountry: {}  population: {}".format(
        countryName, countryPopulation))
    for city in cities:
        cityName, cityPopulation = city
        print("City: {}  population: {}".format(cityName, cityPopulation))
