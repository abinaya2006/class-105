import csv
import pandas as pd
import plotly_express as px

with open("class2.csv",newline="") as a:
    reader=csv.reader(a)
    data=list(reader)

data.pop(0)
total_marks=0
total_enteries=len(data)

for i in data:
    total_marks+=float(i[1])
    # print(total_marks)

mean=total_marks/total_enteries
print("Mean is : ",mean)

df=pd.read_csv("class2.csv")
sca=px.scatter(df,x="Student Number",y="Marks")
sca.update_layout(shapes=[
    dict(type="line",y0=mean,y1=mean,x0=0,x1=total_enteries)
])
sca.update_yaxes(rangemode="tozero")
sca.show()





