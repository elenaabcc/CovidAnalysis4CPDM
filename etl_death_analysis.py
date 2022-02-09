import pandas as pd

deaths=pd.read_csv(r'C:\Users\strag\Documents\GitHub\CovidAnalysis4CPDM\PROGETTO\deaths and new cases 2.0.csv')

#After importing the dataset i decided to create a smaller dataset with a focus on Italy.
#Then i excluded the year 2022 from my analysis.

deaths_ita=deaths[deaths.countriesAndTerritories=='Italy']
deaths_ita_upd=deaths_ita[deaths_ita.year!=2022]

#Below i created a pivot table to group the data for each year, each month and to sum the number of deaths and then i converted it into a dataframe.
#I created a new row and i included it to the dataframe. 
#I renamed all the month by changing from integer number to charachter name.

df=deaths_ita_upd.pivot_table(index=['year', 'month'], values='deaths', aggfunc='sum').reset_index()
top_row = pd.DataFrame({'year':[2020],'month':[1],'deaths':[0.0]})

df = pd.concat([top_row, df]).reset_index(drop = True)
df.replace(1, "Jan", inplace=True)
df.replace(2, "Feb", inplace=True)
df.replace(3, "Mar", inplace=True)
df.replace(4, "Apr", inplace=True)
df.replace(5, "May", inplace=True)
df.replace(6, "Jun", inplace=True)
df.replace(7, "Jul", inplace=True)
df.replace(8, "Aug", inplace=True)
df.replace(9, "Sep", inplace=True)
df.replace(10, "Oct", inplace=True)
df.replace(11, "Nov", inplace=True)
df.replace(12, "Dec", inplace=True)

#Below i created a pivot table to group the data for each year, each month and to sum the number of cases and then i converted it into a dataframe.
#I created a new row and i included it to the dataframe. 
#I renamed all the month by changing from integer number to charachter name.

df1=deaths_ita_upd.pivot_table(index=['year', 'month'], values='cases', aggfunc='sum').reset_index()
top_row_1 = pd.DataFrame({'year':[2020],'month':[1],'cases':[0.0]})

df1 = pd.concat([top_row_1, df1]).reset_index(drop = True)
df1.replace(1, "Jan", inplace=True)
df1.replace(2, "Feb", inplace=True)
df1.replace(3, "Mar", inplace=True)
df1.replace(4, "Apr", inplace=True)
df1.replace(5, "May", inplace=True)
df1.replace(6, "Jun", inplace=True)
df1.replace(7, "Jul", inplace=True)
df1.replace(8, "Aug", inplace=True)
df1.replace(9, "Sep", inplace=True)
df1.replace(10, "Oct", inplace=True)
df1.replace(11, "Nov", inplace=True)
df1.replace(12, "Dec", inplace=True)
df1

#The number of positive cases is higher for almost all the year 2021. Only October and November 2020 are higher and this was an effect due to the spread ofthe virus after the summer (at that time vaccination campaign hadn't started yet). In December 2021 i can see an higher number of positive cases, this is due to the high number of test produced and to the high transmissibility of the variant Omicron.