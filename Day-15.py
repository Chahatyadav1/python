import pandas

# file=pandas.read_csv("weather_data.csv")
# print(file[file.temp==14])    # to read specific row
# print(file.day)               # to read col
# d=file.day.to_dict()         # to dict also similar to csv
# print(d)

# data=pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20260723.csv")
# grey=data[data["Primary Fur Color"]== "Gray"]
# len_of_gray=len(grey.X.to_list())
# print(len_of_gray)
# Cinnamon=data[data["Primary Fur Color"]== "Cinnamon"]
# len_of_Cinnamon=len(Cinnamon.X.to_list())
# print(len_of_Cinnamon)
# Black=data[data["Primary Fur Color"]== "Black"]
# len_of_Black=len(Black.X.to_list())
# print(len_of_Black)
# dict={
#     "Color": ["Gray","Cinnamon","Balck"],
#     "Count": [len_of_gray,len_of_Cinnamon,len_of_Black]
# }
# a=pandas.DataFrame(dict)
# print(a)