import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census.csv")

# create color summary csv
color_summary = data.groupby("Primary Fur Color")["Unique Squirrel ID"].count()
color_summary = pd.DataFrame(color_summary)
color_summary.to_csv("color_summary.csv")