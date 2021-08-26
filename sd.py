import csv
import math
import statistics

with open("data.csv",newline="") as a:
    reader=csv.reader(a)
    file_data=list(reader)

data=file_data[0]
print(data)

def mean (data):
    n=len(data)
    total=0

    for i in data:
        total+=int(i)
    
    mean=total/n
    return mean

squared_list=[]

for num in data:
    a=int(num)-mean(data)
    a=a**2
    squared_list.append(a)

sum=0
for i in squared_list:
    sum+=i

result=sum/(len(data)-1)
standard_deviation=math.sqrt(result)
print(standard_deviation)


'''
data1=[]

for a in data:
    a=int(a)
    data1.append(a)

print(statistics.mean(data1))
print(statistics.stdev(data1))
'''
