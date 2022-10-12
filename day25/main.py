# import csv
import numpy as np
import pandas as pd

# # option 1: read csv raw
# with open("weather.csv", "r") as file:
#     data = file.readlines()
#
# # option 2: inbuilt csv
# with open("weather.csv", "r") as file:
#     data = csv.reader(file)

df = pd.read_csv("weather.csv")

print(df["temp"].mean())

print(df["temp"].agg(["mean", "max "]))
