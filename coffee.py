import csv, numpy as np
# import plotly.express as plot

coffee = []
sleep = []

with open("coffeeData.csv") as f :
    df = csv.DictReader(f)
    # scatterplot = plot.scatter(df, x = "Size of TV", y = "Average time spent watching TV in a week (hours)")
    # scatterplot.show()

    for i in df :
      coffee.append(float(i["Coffee (ml)"]))
      sleep.append(float(i["Sleep (hours)"]))

corrCoef = np.corrcoef(coffee, sleep)
print(corrCoef[0,1])