import pandas as pd
icu_data=pd.read_csv(r'C:\Users\strag\Documents\GitHub\CovidAnalysis4CPDM\PROGETTO\icu dataframe.csv')


#MEAN NUMBER OF COVID PATIENTS IN HOSPITAL AND ICU OCCUPANCY FROM THE BEGINNING TO NOW
icu_italy=icu_data[icu_data['country']=='Italy']
my_cond=['Daily ICU occupancy', 'Daily hospital occupancy']
icu_italy=icu_italy[icu_italy['indicator'].isin(my_cond)]
icu_italy[['Year', 'Month', 'Day']]=icu_italy['date'].str.split('-', expand=True)

df_icu=icu_italy.pivot_table(index=['Year', 'Month'], columns='indicator', values='value', aggfunc='mean').reset_index()
df_icu=df_icu.round(2)
df_icu.replace("01", "Jan", inplace=True)
df_icu.replace("02", "Feb", inplace=True)
df_icu.replace("03", "Mar", inplace=True)
df_icu.replace("04", "Apr", inplace=True)
df_icu.replace("05", "May", inplace=True)
df_icu.replace("06", "Jun", inplace=True)
df_icu.replace("07", "Jul", inplace=True)
df_icu.replace("08", "Aug", inplace=True)
df_icu.replace("09", "Sep", inplace=True)
df_icu.replace("10", "Oct", inplace=True)
df_icu.replace("11", "Nov", inplace=True)
df_icu.replace("12", "Dec", inplace=True)
df_icu.rename(columns = {'Daily ICU occupancy':'ICU occupancy', 'Daily hospital occupancy':'Hospital occupancy'}, inplace = True)

df_icu.loc[-1] = ['2020', 'Jan', 0, 0]
df_icu.index= df_icu.index + 1 #shifting index
df_icu.sort_index(inplace=True) #sorting

#remove year 2022
df_icu.drop(df_icu.tail(1).index,inplace=True) #drop last row
df_icu