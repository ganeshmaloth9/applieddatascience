import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df= pd.read_csv('WorldHappiness_Corruption_2015_2020.csv')

#line plot
def happiness_score(df,countries):
    ''' The function is used for plotting line plot of each country from 2015 to 2020. The function takes df : dataframe and countries: [list of countries] as the input parameters'''
    for i in countries:
        c= df[df['Country'] == i]
        plt.plot(c['Year'],c['happiness_score'],label=i)
    plt.legend()
    plt.xlabel('Years')
    plt.ylabel('Happiness Score')
    plt.title('Happiness score of countries from 2015 to 2020')
    plt.show()     

#add other countries to plot line plot
country_list = ['United Kingdom','China','Russia','Germany']

happiness_score(df, countries=country_list)

# boxplot

cpi_sweden = df[df['Country'] == 'Sweden']
cpi_norway = df[df['Country'] == "Norway"]
cpi_denmark = df[df['Country'] == 'Denmark']
cpi_germany =df[df['Country'] == 'Germany']

['cpi_score']
fig, ax = plt.subplots()
ax.boxplot([cpi_sweden['cpi_score'],cpi_norway['cpi_score'],cpi_denmark['cpi_score'],cpi_germany['cpi_score']])
ax.set_xticklabels(['Sweden',"Norway",'Denmark','Germany'])
plt.title('Boxplot of Corruption perception index(CPI) score for 5 years.')
plt.xlabel('Country')
plt.xlabel('CPI score')
plt.show()

# scatter plot

x= df[['happiness_score','cpi_score','continent']]
groups = x.groupby('continent')
plt.figure(figsize=(10,6))
for name, group in groups:
    plt.plot(group.cpi_score, group.happiness_score, marker='x', linestyle='', markersize=7, label=name)
plt.title('Effect of Cpi score on Happiness score')
plt.xlabel('cpi score')
plt.ylabel('Happiness score')
plt.legend(title='Continents')
plt.show()

