# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines()
#     print(data)

import csv
with open("weather_data.csv") as weather_data:
    data = csv.reader(weather_data)
    for row in data:
        print(row)
