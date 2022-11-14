import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels = data[data["Primary Fur Color"] == "Gray"]
grey_squirrels_count = len(grey_squirrels)
print(grey_squirrels_count)
red_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
red_squirrels_count = len(red_squirrels)
print(red_squirrels_count)
black_squirrels = data[data["Primary Fur Color"] == "Black"]
black_squirrels_count = len(black_squirrels)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Grey", "Red", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

print(data_dict)
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")

# data = pandas.read_csv("weather_data.csv")
# print(data)
# print(type(data))
# temperatures = data["temp"]
# print(temperatures)
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
#
# avg = data["temp"].mean()
# print(avg)
#
# print(data["temp"].max())
# print(data["temp"].min())
#
# # Get Data in Columns
# print(data["condition"])
# print(data.condition)
#
# # Get Data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# temp_fahrenheit = int(monday.temp) * 9/5 + 32
# print(temp_fahrenheit)
#
# # Create a dataframe from scratch
# data_dict = {
#     "students" : ["Amy", "James", "Angela"],
#     "scores" : [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

