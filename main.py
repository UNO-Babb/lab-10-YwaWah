#MapPlot.py
#Name:
#Date:
#Assignment:

import coffee
import pandas
import matplotlib.pyplot as plt
coffee = coffee.get_coffee()

years = []
scores = []
for bean in coffee:
    y = bean["Year"]
    score = bean["Data"]["Scores"]["Total"]
    if score != 0:
        years.append(y)
        scores.append(score)
    #print(y, score)
df = pandas.DataFrame({"Year": years, "Score": scores})

print(df)
df.plot(kind = 'scatter', x = 'Year', y = 'Score')
#plt.plot(years, scores, 'ro')

# The data goes to the year the coffee was produced and find the scores of specific coffess from the year which comes from the total of 9 factors

plt.savefig("output")