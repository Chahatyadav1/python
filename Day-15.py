import pandas

file=pandas.read_csv("weather_data.csv")
print(file[file.temp==14])    # to read specific row
print(file.day)               # to read col
d=file.day.to_dict()         # to dict also similar to csv
print(d)