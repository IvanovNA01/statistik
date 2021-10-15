from os import rename
import pandas as pd

bookings = pd.read_csv(
    r"C:\Users\Espad\Projects\python\statistik\ML_teaching\bookings.csv", sep=";"
)
bookings_head = bookings.head(7)

# bookings = bookings.rename(str.lower, axis="columns").columns.str.replace(" ", "_")
# replace and lower about using str -> this going to error! оборачиваем lower внутрь rename
# !!! В СЛУЧАЕ ТАКОГО ПРЕОБРАЗОВАНИЯ ОСТАНУТСЯ ОТ ДАТАФРЕЙМА ТОЛЬКО ЗАГЛАВНЫЕ СТОЛБЦЫ - НЕОБХ ИСП Ф-ИИ ВНУТРИ rename
def Lower_replace_columns(old_columns):
    new_columns = old_columns.replace(" ", "_").lower()
    return new_columns


# !!! При передаче ф-ии в качестве аргумента rename указываем ТОЛЬКО имя ф-ии
bookings = bookings.rename(columns=Lower_replace_columns)
# макс число успешных бронирований по странам
bookings_max_count_country = (
    bookings.query("is_canceled==0")
    .groupby("country", as_index=False)
    .agg({"lead_time": "count"})
    .rename(columns={"lead_time": "count_visits"})
    .sort_values("count_visits", ascending=False)
    .head()
)
# среднее продолж ноч брон по отелям
bookings_mean_night_hotel = (
    bookings.groupby("hotel", as_index=False)
    .agg({"stays_total_nights": "mean"})
    .round(2)
)
# кол-во неравных: assigned_room_type != reserved_room_type
bookings_overbooking = bookings.query(
    "assigned_room_type != reserved_room_type"
).count()

most_lovely_month = (
    bookings.query("arrival_date_year==[2016, 2017]")
    .groupby(["arrival_date_year", "arrival_date_month"], as_index=False)
    .agg({"lead_time": "count"})
    .rename(columns={"lead_time": "count_visits"})
    .sort_values("count_visits", ascending=False)
)
# drop_duplicates(subset="arrival_date_year") - удаляет все дубликаты после первого вхождения (subset - по какому столбцу)

most_canceled_month = (
    bookings.query("arrival_date_year==[2015,2016, 2017] & is_canceled==1")
    .groupby(["arrival_date_year", "arrival_date_month"], as_index=False)
    .agg({"lead_time": "count"})
    .rename(columns={"lead_time": "count_visits"})
    .sort_values("count_visits", ascending=False)
    .drop_duplicates(subset="arrival_date_year")
)

max_meancount_people = bookings[["adults", "children", "babies"]].mean()

mean_kids_hotel = (
    bookings.groupby("hotel", as_index=False)
    .agg({"children": "mean", "babies": "mean"})
    .round(2)
)
# создание новой колонки
bookings["total_kids"] = bookings["children"] + bookings.babies

mean_total_kids_hotel = (
    bookings.groupby("hotel", as_index=False)
    .agg({"total_kids": "mean"})
    .sort_values("total_kids", ascending=False)
    .round(2)
)
# % клиентов без детей, отменивших бронь, относительно всех клиентов без детей
# shape[0] - размер столбца ДФ, по умолчанию размер матрицы ДФ - это СПИСОК!
Churn_rate_nokids = round(
    bookings.query("total_kids==0 and is_canceled==1").shape[0]
    * 100
    / bookings.query("total_kids==0").shape[0],
    2,
)
# % клиентов с детьми, отменивших бронь, относительно всех клиентов с детьми
Churn_rate_withkids = round(
    bookings.query("total_kids!=0 and is_canceled==1").shape[0]
    * 100
    / bookings.query("total_kids!=0").shape[0],
    2,
)


print(Churn_rate_nokids)
