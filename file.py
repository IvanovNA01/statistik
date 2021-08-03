import csv  # модуль для работы с текстовыми файлами формата csv
import pickle  # модуль для работы с битовыми файлами формата dat

# открытые файла для записи, с исключением и закрытием в случае ошибки
try:
    somefile = open("hello.txt", "w")
    try:
        somefile.write("hello world")
    except Exception as e:
        print(e)
    finally:
        somefile.close()
except Exception as ex:
    print(ex)
# открытые файла для записи через объект
with open("hello.txt", "w") as somefile:
    somefile.write("hello world")
# открытые файла для дозаписи через объект, в новую строку
with open("hello.txt", "a") as file:
    file.write("\ngood bye, world")
# Еще один способ записи в файл представляет стандартный метод print()
with open("hello.txt", "a") as hello_file:
    print("Hello, world", file=hello_file)
# открытые файла для чтения через объект, построчно
with open("hello.txt", "r") as file:
    for line in file:
        print(line, end="")
# идентично
    str1 = file.readline()
    print(str1, end="")
    str2 = file.readline()
    print(str2)
# идентично
line = file.readline()
while line:
    print(line, end="")
    line = file.readline()
# открытые файла для чтения через объект, все данные в одну строку
with open("hello.txt", "r") as file:
    content = file.read()
    print(content)
# открытые файла для чтения через объект, в список строк
    contents = file.readlines()
    str1 = contents[0]
    str2 = contents[1]
    print(str1, end="")
    print(str2)

# пример программы
# имя файла
FILENAME = "messages.txt"
# определяем пустой список
messages = list()

for i in range(4):
    message = input("Введите строку " + str(i+1) + ": ")
    messages.append(message + "\n")

# запись списка в файл
with open(FILENAME, "a") as file:
    for message in messages:
        file.write(message)

# считываем сообщения из файла
print("Считанные сообщения")
with open(FILENAME, "r") as file:
    for message in file:
        print(message, end="")

# csv - это формат текстовых файлов, Python предоставляет специальный встроенный модуль (import csv - подключаем)
FILENAME = "users.csv"

users = [
    ["Tom", 28],
    ["Alice", 23],
    ["Bob", 34]
]
# Для записи нам надо получить объект writer, который возвращается функцией csv.writer(file). В эту функцию передается открытый файл.
# запись производится с помощью метода writer.writerows(users) Этот метод принимает набор строк
# При открытии файла на запись в качестве третьего параметра указывается значение newline=""
# пустая строка позволяет корректно считывать строки из файла вне зависимости от операционной системы
with open(FILENAME, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(users)
# Если необходимо добавить одну запись, vможно вызвать метод writer.writerow(user)
with open(FILENAME, "a", newline="") as file:
    user = ["Sam", 31]
    writer = csv.writer(file)
    writer.writerow(user)
# Для чтения из файла нам наоборот нужно создать объект reader:
with open(FILENAME, "r", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[0], " - ", row[1])

# Работа со словарями
users = [
    {"name": "Tom", "age": 28},
    {"name": "Alice", "age": 23},
    {"name": "Bob", "age": 34}
]
# функция csv.DictWriter() возвращает объект writer, который позволяет записывать в файл
with open(FILENAME, "w", newline="") as file:
    columns = ["name", "age"]
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()

    # запись нескольких строк
    writer.writerows(users)

    user = {"name": "Sam", "age": 41}
    # запись одной строки
    writer.writerow(user)
# функция csv.DictReader() возвращает объект reader для чтения из файла.
with open(FILENAME, "r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"], "-", row["age"])

# Бинарные файлы в отличие от текстовых хранят информацию в виде набора байт. Для работы с ними в Python необходим встроенный модуль pickle
# dump(obj, file): записывает объект obj в бинарный файл file
# load(file): считывает данные из бинарного файла в объект
FILENAME = "user.dat"

name = "Tom"
age = 19

with open(FILENAME, "wb") as file:
    pickle.dump(name, file)
    pickle.dump(age, file)

with open(FILENAME, "rb") as file:
    name = pickle.load(file)
    age = pickle.load(file)
    print("Имя:", name, "\tВозраст:", age)
