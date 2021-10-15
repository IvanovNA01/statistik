import pandas as pd
from pandas.core import groupby
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv(
    r"C:\Users\Espad\Projects\python\statistik\ML_teaching\lesson_3_data__1_.csv",
    encoding="windows-1251",
)
df_user = df[["tc", "art_sp"]].rename(columns={"tc": "user_id", "art_sp": "brand_info"})
# split('$') - разделяет строку на список строк с разделителем $, в конце brand_info указан производитель [-1] = 1 эл-т с конца!
def split_to_brand(brand_all):
    brand_split = brand_all.split(" ")[-1]
    return brand_split


# apply - позволяет ПРИМЕНИТЬ ф-ию ко всей колонке, создаем новую колонку
df_user["brand_name"] = df_user.brand_info.apply(split_to_brand)
# альтернатива использования def -> lambda используется для однострочных ф-ий
# df_user["brand_name"] = df_user.brand_info.apply(lambda x: x.split(" ")[-1])
# median - медиана кол-ва покупок, describe - стат величины (75% - квартиль 3 из 4, то есть 25% больше 5шт в нашем ДФ)
user_pay = (
    df_user.groupby("user_id", as_index=False)
    .agg({"brand_name": "count"})
    .rename(columns={"brand_name": "count_payment"})
    .query("count_payment > 5")
)

# колич покупок юзером определен бренда ascending=[False,False] - по обеим велич сорт поубыванию
# нам нужно найти любимого производителя, а значит max элемент в каждой группе
lovely_user_pay = (
    df_user.groupby(["user_id", "brand_name"], as_index=False)
    .agg({"brand_info": "count"})
    .rename(columns={"brand_info": "count_lovely_payment"})
    .sort_values(["user_id", "count_lovely_payment"], ascending=[False, False])
    .drop_duplicates(subset="user_id")
    .rename(columns={"brand_name": "lovely_brand"})
)
# альтернатива drop_duplicates - сгруппировать по покупателям и отобрать 1ую строку, если нужна последняя в группе tail()
lovely_user_pay = (
    df_user.groupby(["user_id", "brand_name"], as_index=False)
    .agg({"brand_info": "count"})
    .rename(columns={"brand_info": "count_lovely_payment"})
    .sort_values(["user_id", "count_lovely_payment"], ascending=[False, False])
    .groupby("user_id")
    .head(1)
    .rename(columns={"brand_name": "lovely_brand"})
)
# количество брендов для каждого покупателя
user_brand_unique = (
    df_user.groupby("user_id", as_index=False)["brand_name"]
    .nunique()
    .rename(columns={"brand_name": "count_unique_brand"})
)
# объединение ДФ, аналог join: on - ключ по котор объед, how - способ(left, right, inner)
loyalty_df = user_pay.merge(lovely_user_pay, on="user_id", how="inner").merge(
    user_brand_unique, on="user_id", how="inner"
)
# вывод ДФ с условием внутри, 100% лояльные те у кого всего 1 покупаемый бренд
loyalty_users = loyalty_df[loyalty_df.count_unique_brand == 1]

# создание колонки коэфф лояльности доля любимых: count_lovely_payment/count_payment
loyalty_df["loyalty_koeff"] = loyalty_df.count_lovely_payment / loyalty_df.count_payment
#!!!ПРИ ТАКОМ СПОСОБЕ ВИЗУАЛИЗАЦИИ ВСЕ ГРАФИКИ БУДУТ НА 1 ПЛОСКОСТИ
# визуализация гистограммы распределения метрики лояльности
ax = sns.displot(loyalty_df.loyalty_koeff)
# по каждому бренду определили медиану коэф лояль покупателей и колич покупок
loyalty_brands = (
    loyalty_df.groupby("lovely_brand", as_index=False)
    .agg({"loyalty_koeff": "median", "user_id": "count"})
    .rename(columns={"user_id": "count_payment"})
)
# визуализация баров распределения количества покупок по каждому бренду
ax = sns.barplot(x="lovely_brand", y="count_payment", data=loyalty_brands)
plt.show()

# print(loyalty_df)
