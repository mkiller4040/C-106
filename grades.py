import csv, numpy as np
# import plotly.express as plot

Marks_In_Percentage = []
Days_Present = []

with open("gradesData.csv") as f :
    df = csv.DictReader(f)
    # scatterplot = plot.scatter(df, x = "Size of TV", y = "Average time spent watching TV in a week (hours)")
    # scatterplot.show()

    for i in df :
      Marks_In_Percentage.append(float(i["Marks In Percentage"]))
      Days_Present.append(float(i["Days Present"]))

corrCoef = np.corrcoef(Marks_In_Percentage, Days_Present)
print(corrCoef[0,1])