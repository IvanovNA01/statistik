import pandas as pd
from datetime import datetime  # library of work to date

today_date = datetime.today().strftime("%Y-%m-%d")  # get today date
df = pd.read_csv("lesson_1_data.csv", encoding="windows-1251", sep=";")
# df = df.describe() - mean, std, kwartyl, count
df = df.rename(
    columns={
        "Номер": "number",
        "Дата создания": "create_date",
        "Дата оплаты": "paym_date",
        "Title": "title",
        "Статус": "status",
        "Заработано": "money",
        "Город": "city",
        "Платежная система": "payment_system",
    }
)
all_money = df["money"].sum()
# df[["title", "money"]].head() - 5 rows on the 2 columns of datafraim (title and money)
# df.status - out of column "status", if its coll on english, without ' '
all_money = round(df.money.sum(), 2)
money_by_city = (
    df.query('status=="Завершен"')
    .groupby(["title", "city"], as_index=False)
    .aggregate({"money": "sum", "number": "count"})
    .sort_values("money", ascending=False)
    .rename(columns={"number": "sucsess_orders"})
)
# query - запрос с предусловием выборки
# as_index=False - чтобы title не выступал в роли индекса, не использовать с idxmin() и idxmax() - вызывают индекс min,max значения
# ascending=False - по убыванию
# if we need group by many columns - used list of this columns [...]
# our aggregate func describte as dict {column:func}
money_by_city.to_csv(
    "money_by_city.csv", index=False
)  # do not add column index to scv file
money_title = (
    df.query('status=="Завершен"')
    .groupby("title", as_index=False)
    .aggregate({"money": "sum", "number": "count"})
    .sort_values("money", ascending=False)
    .rename(columns={"number": "sucsess_orders"})
)

file_name = "money_title_{}.csv"
file_name = file_name.format(today_date)

# money_title["money"].sum() - для проверки себя стоит пересчитать
if money_title["money"].sum() == all_money:
    print("its ok, file {} is ready to work!".format(file_name))
    money_title.to_csv(file_name, index=False)
else:
    print("lose the money!")


print(money_title["money"].sum())
