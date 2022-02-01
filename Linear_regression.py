import pandas as pd
import plotly.express as px
import numpy as np
import csv

dp = pd.read_csv("data_114.csv")

TOEFL_score = dp["TOEFL Score"].tolist()

Chance_of_Admit = dp["Chance of Admit "].tolist()

fig = px.scatter(x = TOEFL_score , y = Chance_of_Admit)
#fig.show()

#------------------------ finding m & c using hit and trial ------------------------------------

m = 0.018
c = -1.27
y = []

for x in TOEFL_score:
    y2 = (m*x) + c
    y.append(y2)


fig = px.scatter(x = TOEFL_score, y = Chance_of_Admit)
fig.update_layout(shapes = [
    dict(
        type = 'line',
        y0 = min(y),
        y1 = max(y),
        x0 = min(TOEFL_score),
        x1 = max(TOEFL_score) 
    )
])

#fig.show()
 
x = 650
y = m*x +c
#print("Chances of admit if the TOEFL score using Hit & Trial" , y)

#------------------------ finding m & c using Algorithm  ------------------------------------

TOEFL_score_a = np.array(TOEFL_score)
Chance_of_Admit_a = np.array(Chance_of_Admit)

m,c = np.polyfit(TOEFL_score_a,Chance_of_Admit_a,1)

y = []

for x in TOEFL_score:
    y2 = (m*x) + c
    y.append(y2)


fig = px.scatter(x = TOEFL_score, y = Chance_of_Admit)
fig.update_layout(shapes = [
    dict(
        type = 'line',
        y0 = min(y),
        y1 = max(y),
        x0 = min(TOEFL_score),
        x1 = max(TOEFL_score) 
    )
])

#fig.show()
 
x = 650
y = m*x +c

print(y)