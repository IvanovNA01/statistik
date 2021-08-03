# объявление класса
class Person:
    # параметр self указывается первым у каждой функции класса, это ссылка на текущий объект класса
    # конструктор - вызывается при создании объекта класса, передаем значение параметру name
    def __init__(self, name):
        # устанавливаем значение параметра класса (по умолчанию общедоступные), сразу его и определяем
        self.name = name

    def display_info(self):
        print("Привет, меня зовут", self.name)
    # конструктор удаления вызывается при вызове метода del "имя объекта" или после автом удаления по окончании скрипта

    def __del__(self):
        print(self.name, "удален из памяти")


class Auto:
    # конструктор
    def __init__(self, name):
        self.name = name
# self.name позволяет обратиться к переменной класса определенной в этом классе, speed - входной атрибут

    def move(self, speed):
        print(self.name, "едет со скоростью", speed, "км/ч")

# Вариант класса с инкапсюляцией(параметры класса privat доступны для изменения через get и set функции-свойства)


class PersonClose:
    def __init__(self, name):
        # устанавливаем имя, для закрытия прямого доступа извне класса приставка __
        self.__name = name
        self.__age = 1          # устанавливаем возраст
# функция приема и изменения параметра класса с проверкой

    def set_age(self, age):
        if age in range(1, 100):
            self.__age = age
        else:
            print("Недопустимый возраст")
# функции вывода значений

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name

    def display_info(self):
        print("Имя:", self.__name, "\tВозраст:", self.__age)


# инкапсюляцию можно проводить через  аннотаций, которые предваряются символом @ (@property-геттер, @имя_свойства_геттера.setter-сеттер)
class PersonProperty:
    def __init__(self, name, age):
        self.__name = name  # устанавливаем имя
        self.__age = age      # устанавливаем возраст

# функция вывода значения геттер, определяется перед сеттером
    @property
    def age(self):
        return self.__age
# функция приема и изменения параметра класса с проверкой

    @age.setter
    def age(self, age):
        if age in range(1, 100):
            self.__age = age
        else:
            print("Недопустимый возраст")
# функции вывода значений

    @property
    def name(self):
        return self.__name

# метод __str__() наследуется от суперкласса object, и позволяет олучить строковое представление объекта или вывести объект в виде строки
    def display_info(self):
        print(self.__str__())

    def __str__(self):
        return "Имя: {} \t Возраст: {}".format(self.__name, self.__age)

# наследование подклассом Employee функций и параметров надкласса PersonProperty
# Полиморфизм - изменение функционала, унаследованного от базового класса


class Employee(PersonProperty):
    # определение конструктора
    def __init__(self, name, age, company):
        # вызывается конструктор базового класса PersonProperty, для того чтобы была из подкласса изменять атрибуты определенные в надклассе
        PersonProperty.__init__(self, name, age)
        self.company = company

    def details(self, company):
        # print(self.__name, "работает в компании", company) # так нельзя, self.__name - приватный атрибут и доступен только в надклассе
        # в подклассе доступны через ключевое слово self все методы и атрибуты надкласса PersonProperty, кроме закрытых атрибутов типа __name или __age
        # создании объекта Employee мы фактически используем конструктор надкласса. И кроме того, у этого объекта мы можем вызвать все методы надкласса
        # в self.name вызывается гет функция надкласса
        print(self.name, "работает в компании", company)

# переопределение метода display_info надкласса PersonProperty
    def display_info(self):
        # вызов метода из надкласса с атрибуьами изменнеными в подклассе
        PersonProperty.display_info(self)
        print("Компания:", self.company)


class Student(PersonProperty):
    # определение конструктора
    def __init__(self, name, age, university):
        PersonProperty.__init__(self, name, age)
        self.university = university

    # переопределение метода display_info
    def display_info(self):
        print("Студент", self.name, "учится в университете", self.university)
