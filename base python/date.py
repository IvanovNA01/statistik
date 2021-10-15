# модуль работы с датой, датой-временем, временем (классы)
from datetime import date, datetime, time, timedelta
# по умолчанию используются английские наименования, ксли хотим использовать текущую локализацию, подключаем locale
# import locale
# locale.setlocale(locale.LC_ALL, "")
# now = datetime.now()
# print(now.strftime("%d %B %Y (%A)"))        # 03 Май 2017 (среда)


# работа с датой
day = date(2017, 5, 2)  # год, месяц, день
print(day)      # 2017-05-02
today = date.today()
print(today)      # 2021-07-03
print("{}.{}.{}".format(today.day, today.month, today.year))      # 3.7.2021

# работа с временем
current_time = time()
print(current_time)     # 00:00:00

current_time = time(16, 25)
print(current_time)     # 16:25:00

# час, мин, сек, микросек (если параметр не указан - 0)
current_time = time(16, 25, 45)
print(current_time)     # 16:25:45

# работа с датой-временем
# год, месяц, день, час, мин, сек, микросек (если параметр не указан - 0)
deadline = datetime(2017, 5, 10, 4, 30)
print(deadline)     # 2017-05-10 04:30:00
# метод передающий текущие дату-время
now = datetime.now()
print(now)     # 2021-07-03 11:18:56.239443
print("{}.{}.{}  {}:{}".format(now.day, now.month,
      now.year, now.hour, now.minute))  # 3.7.2021  11:21

print(now.date())  # тек дата
print(now.time())  # тек время


# метод strptime(str, format), который позволяет распарсить строку и преобразовать ее в дату
# %d: день месяца в виде числа
# %m: порядковый номер месяца
# %y: год в виде 2-х чисел
# %Y: год в виде 4-х чисел
# %H: час в 24-х часовом формате
# %M: минута
# %S: секунда


deadline = datetime.strptime("22/05/2017", "%d/%m/%Y")
print(deadline)     # 2017-05-22 00:00:00

deadline = datetime.strptime("22/05/2017 12:30", "%d/%m/%Y %H:%M")
print(deadline)     # 2017-05-22 12:30:00

deadline = datetime.strptime("05-22-2017 12:30", "%m-%d-%Y %H:%M")
print(deadline)     # 2017-05-22 12:30:00
# Фоматирование дат и времени, объектов date и time в обоих этих классах предусмотрен метод strftime(format)

# %a: аббревиатура дня недели. Например, Wed - от слова Wednesday(по умолчанию используются английские наименования)
# %A: день недели полностью, например, Wednesday
# %b: аббревиатура названия месяца. Например, Oct(сокращение от October)
# %B: название месяца полностью, например, October
# %d: день месяца, дополненный нулем, например, 01
# %m: номер месяца, дополненный нулем, например, 05
# %y: год в виде 2-х чисел
# %Y: год в виде 4-х чисел
# %H: час в 24-х часовом формате, например, 13
# %I: час в 12-ти часовом формате, например, 01
# %M: минута
# %S: секунда
# %f: микросекунда
# %p: указатель AM/PM
# %c: дата и время, отформатированные под текущую локаль
# %x: дата, отформатированная под текущую локаль
# %X: время, форматированное под текущую локаль
now = datetime.now()
print(now.strftime("%Y-%m-%d"))             # 2017-05-03
print(now.strftime("%d/%m/%Y"))             # 03/05/2017
print(now.strftime("%d/%m/%y"))             # 03/05/17
print(now.strftime("%d %B %Y (%A)"))        # 03 May 2017 (Wednesday)
print(now.strftime("%d/%m/%y %I:%M"))       # 03/05/17 01:36

# Сложение и вычитани дат и времени
# для добавления или вычитания периода времени исп класс timedelta
# timedelta([days] [, seconds] [, microseconds] [, milliseconds] [, minutes] [, hours] [, weeks])
three_hours = timedelta(hours=3)
print(three_hours)       # 3:00:00
three_hours_thirty_minutes = timedelta(hours=3, minutes=30)  # 3:30:00

two_days = timedelta(2)  # 2 days, 0:00:00

two_days_three_hours_thirty_minutes = timedelta(
    days=2, hours=3, minutes=30)  # 2 days, 3:30:00

# сложение
now = datetime.now()
print(now)                      # 2017-05-03 17:46:44.558754
in_two_days = now + two_days
print(in_two_days)              # 2017-05-05 17:46:44.558754
# вычитание
till_ten_hours_fifteen_minutes = now - timedelta(hours=10, minutes=15)
print(till_ten_hours_fifteen_minutes)  # 2017-05-05 07:31:44.558754

# Свойства timedelta
# Класс timedelta имеет несколько свойств, с помощью которых мы можем получить временной промежуток:
# days: возвращает количество дней
# seconds: возвращает количество секунд
# microseconds: возвращает количество микросекунд
# Кроме того, метод total_seconds() возвращает общее количество секунд, куда входят и дни, и собственно секунды, и микросекунды

now = datetime.now()
twenty_two_may = datetime(2017, 5, 22)
period = now - twenty_two_may
print("{} дней  {} секунд   {} микросекунд".format(
    period.days, period.seconds, period.microseconds))
# n дней  m секунд   k микросекунд

print("Всего: {} секунд".format(period.total_seconds()))
# Всего: r секунд

# Сравнение дат
# Также как и строки и числа, даты можно сравнивать с помощью стандартных операторов сравнения
deadline = datetime(2022, 5, 22)
if now > deadline:
    print("Срок сдачи проекта прошел")
elif now.day == deadline.day and now.month == deadline.month and now.year == deadline.year:
    print("Срок сдачи проекта сегодня")
else:
    period = deadline - now
    print("Осталось {} дней".format(period.days))

# перевод из  общего кол-ва секунд в дату и время в формате datetime
datetime.fromtimestamp(1581714066).strftime(
    "%B %d, %Y %I:%M:%S")  # 'February 14, 2020 11:01:06'
