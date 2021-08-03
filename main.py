# доступ к файлу account под псевданимом (ко всем внутренним ф-ям и классам)
import account as acc
# импортируем из файла classes выбранные классы (для конкретизации выбора)
from classes import Person, Auto, PersonClose, PersonProperty, Employee, Student
import random


rnd = str(hex(random.randint(1, 10000)))
len = int(len(rnd))
string = rnd[2:len]
print('#' + rnd)
# создание объектов классов, при создании вызывается конструктор
tom = Person("Tom")
tom.display_info()  # Привет, меня зовут Tom

bmw = Auto("BMW")
bmw.move(65)  # BMW едет со скоростью 65 км/ч

jack = PersonClose("jack")

jack.display_info()          # Имя: jack  Возраст: 1
jack.set_age(-3486)          # Недопустимый возраст
jack.set_age(25)
jack.display_info()          # Имя: jack  Возраст: 25

# jack.__age = 43 подобное присвоение не пройдет, так как параметр класса закрыт
# вызов конструктора
sam = PersonProperty(12, "sam")

sam.display_info()      # Имя: sam  Возраст: 1
sam.age = -3486         # Недопустимый возраст
print(sam.age)          # 1
sam.age = 36
sam.display_info()      # Имя: sam  Возраст: 36
print(sam)  # вызывается метод __str__()

# создание объекта подкласса наследника
ken = Employee(18, "ken", "Aple")
ken.details("Google")
ken.age = 36
ken.display_info()  # ken работает в компании Google

# создание объектов подклассов полиморфов в списке
people = [PersonProperty("Tom", 23), Student("Bob", 19, "Harvard"),
          Employee("Sam", 35, "Google")]

for person in people:
    person.display_info()
    print()  # пустая строка между итерациями

# Проверка типа объекта класса
for person in people:
    if isinstance(person, Student):
        # можем считать данные, так как у закрытой name есть геттер, а остальные открыты
        print(person.university)
    elif isinstance(person, Employee):
        print(person.company)
    else:
        print(person.name)
    print()


def main():  # главная ф-я

    rate = int(input("Введите процентную ставку: "))
    money = int(input("Введите сумму: "))
    period = int(input("Введите период ведения счета в месяцах: "))

    # обращение к файлу account
    result = acc.calculate_income(rate, money, period)
    print("Параметры счета:\n", "Сумма: ", money, "\n", "Ставка: ", rate, "\n",
          "Период: ", period, "\n", "Сумма на счете в конце периода: ", result)


# обработка исключений
try:  # блок информации которую нужно проверить
    number1 = int(input("Введите первое число: "))
    number2 = int(input("Введите второе число: "))
    if number2 == 0:  # самостоятельный вызов исключения, проверка если равно 0 выведет сообщение об ошибке и выйдет
        # общий вид исключения
        raise Exception("Второе число не должно быть равно 0")
    print("Результат деления двух чисел:",
          number1/number2)  # если все правильно
except ValueError:  # случай некорректно введенного значения
    print("Введены некорректные данные")
except Exception as e:  # общий вид исключения, можно не писать Exception, если не используется AS - получение информации об происшедшей ошибке
    print(e)
print("Завершение программы")
