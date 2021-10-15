import pandas as pd

taxi = pd.read_csv(
    r"C:\Users\Espad\Projects\python\statistik\ML_teaching\2_taxi_nyc.csv",
    encoding="windows-1251",
    sep=",",
).rename(columns={"pcp 01": "pcp_01", "pcp 06": "pcp_06", "pcp 24": "pcp_24"})
drive_on_the_city = (
    taxi.groupby(["borough"])
    .agg({"pickups": "sum"})
    .sort_values("pickups", ascending=False)
)
min_pickups = drive_on_the_city["pickups"].idxmin()

mean_hday = (
    taxi.query('hday=="Y"')
    .groupby(["borough"], as_index=False)
    .agg({"pickups": "mean"})
    .sort_values("pickups", ascending=False)
)

mean_wday = (
    taxi.query('hday=="N"')
    .groupby(["borough"], as_index=False)
    .agg({"pickups": "mean"})
    .sort_values("pickups", ascending=False)
)

mean_allday = taxi.groupby(["borough", "hday"]).agg({"pickups": "mean"}).unstack()
max_mean_wday = mean_allday[
    mean_allday["pickups"]["Y"] > mean_allday["pickups"]["N"]
].index  # groupby(max(mean(pickups))), "Y"
# unstack - разделяет мультииндекс, 1 лвл оставляет, 2 переводит в столбцы обращение [1lvl][2lvl]
pickups_by_mon_bor = (
    taxi.groupby(["pickup_month", "borough"], as_index=False)
    .agg({"pickups": "sum"})
    .sort_values("pickups", ascending=False)
)


def temp_to_celcius(tempF):
    return (tempF - 32) * 5 / 9


print(temp_to_celcius(taxi["temp"].head()))
