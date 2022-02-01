import pandas as pd
import numpy as np
import random as rd
import matplotlib.pyplot as plt
import statistics as st
plt.figure(figsize=(10, 6)) #dimensiona a figura
data1= np.random.normal(0.000, 0.100,100000) #distribuição gaussiana
data2=np.random.uniform(-1,1,100) #distribuição uniforme
count, bins, ignored = plt.hist(data2, 50,alpha=0.8, facecolor='red')
count, bins, ignored =plt.hist(data1, bins=100, density=True, alpha=0.61, color='b')
plt.xlabel('X~U[-1,1]') #nomeia eixo x
plt.ylabel('Count') #nomeia eixo y
plt.title("Uniform and normal Distributions Histograms") #dá titulo
plt.axis([-1, 1, 0, 5]) # x_start, x_end, y_start, y_end
plt.grid(True) #grades

plt.show()
median=st.median(data1)
mean=st.mean(data1)
median2=st.median(data2)
mean2=st.mean(data2)
print("Para a distrubição gaussiana temos:")
print("Média=",mean ,"mediana=",median)
print("Para a distrubição uniforme temos:")
print("Média=",mean2 ,"mediana=",median2)


DG,DU=pd.Series(data1), pd.Series(data2)
print("Descrição do conjunto de números DG",DG.describe())
print("Descrição do conjunto de números DU",DU.describe())
