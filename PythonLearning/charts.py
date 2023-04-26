# -*- coding: utf-8 -*-
"""charts.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VrVq0UtHauk0_VaUKs_2t2ya-6b8TzsS

**Charts **
"""

import matplotlib.pyplot as plt
import numpy as np

values = [1, 5, 8, 9, 13,12,7, 11, 8, 12, 14, 9]
plt.title('Single chart title')
plt.plot(values)

sales1 = [1, 5, 8, 9, 7, 11, 8, 12, 14, 9, 5]
sales2 = [3, 7, 9, 6, 4, 5, 14, 7, 6, 16, 12]
line_chart1 = plt.plot(range(1,12), sales1)
line_chart2 = plt.plot(range(1,12), sales2)
plt.title('Sample multiple line chart')
plt.xlabel('Number of Products')
plt.ylabel('Month')
plt.legend(['first year', 'second year'], loc=4)
plt.show()

values = [60, 80, 90, 55, 10, 30]
colors = ['b', 'g', 'r', 'c', 'm', 'y']
labels = ['US', 'UK', 'India', 'Germany', 'Australia', 'South Korea']
explode = (0.2, 0, 0, 0, 0, 0)
plt.pie(values, colors=colors, labels= values,explode=explode,counterclock=False, shadow=True)
plt.title('Population Density Index')
plt.legend(labels,loc=3)
plt.show()

values = [82,76,24,40,67,62,75,78,71,32,98,89,78,67,72,82,87,66,56,52]
plt.hist(values,5, histtype='step', align='mid', color='g', label='Sample Score Data')
plt.legend(loc=2)
plt.title('Histogram of score')
plt.show()

values = [82,76,24,40,67,62,75,78,71,32,98,89,78,67,72,82,87,66,56,52]
plt.hist(values,5, histtype='bar',
align='mid', color='c', label='Sample score Data',edgecolor='black')
plt.legend()
plt.title('Histogram of score')
plt.show()

weight1=[63.3,57,64.3,63,71,61.8,62.9,65.6,64.8,63.1,68.3,69.7,65.4,66.3,60.7]
height1=[156.3,100.7,114.8,156.3,237.1,123.9,151.8,164.7,105.4,136.1,175.2,137.4,164.2,151,124.3]

plt.scatter(weight1,height1,c='b',marker='o')
plt.xlabel('weight', fontsize=16)
plt.ylabel('height', fontsize=16)
plt.title('scatter plot - height vs weight',fontsize=20)
plt.show()

city=['Galle','Matara','Colombo','Kandy','Trinco']
pos = np.arange(len(city))
Happiness_Index=[60,40,70,65,85]
plt.bar(pos,Happiness_Index,color='green',edgecolor='black')
plt.xticks(pos, city)
plt.xlabel('City', fontsize=16)
plt.ylabel('Love_Index', fontsize=16)
plt.title('Barchart - Sample data',fontsize=20)
plt.show()

city=['Galle','Matara','Colombo','Kandy','Trinco']
pos = np.arange(len(city))
Happiness_Index=[60,40,70,65,85]
plt.barh(pos,Happiness_Index,color='green',edgecolor='black')
plt.yticks(pos, city)
plt.xlabel('Love_Index', fontsize=16)
plt.ylabel('City', fontsize=16)
plt.title('Barchart - Sample Data',fontsize=20)
plt.show()