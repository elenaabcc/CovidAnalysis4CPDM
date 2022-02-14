import pandas as pd

#import the csv file
ecdc_iniziale=pd.read_csv(r'C:\Users\strag\Documents\GitHub\CovidAnalysis4CPDM\PROGETTO\ECDC dataset iniziale.csv')
ecdc_iniziale.head(30)

#drop columns useless
ecdc_iniziale.drop(['NumberDosesReceived','NumberDosesExported', 'FirstDoseRefused'], axis=1, inplace=True)

#create a copy of the dataframe and work only with Italy as country
italy_df=ecdc_iniziale.copy()
group=['IT']
italy_df = italy_df[italy_df['ReportingCountry'].isin(group)]

#create a new column where i sum up all the doses administered per week
italy_df['tot doses']= italy_df['FirstDose']+italy_df['SecondDose']+ italy_df['DoseAdditional1']+italy_df['UnknownDose']

#split the column YearWeekISO in two columns 
italy_df[['Year', 'Week']]=italy_df['YearWeekISO'].str.split('-', expand=True)

#rename all the region 
italy_df.replace("ITH3", "Veneto", inplace=True)
italy_df.replace("ITH4", "Friuli-Venezia Giulia", inplace=True)
italy_df.replace("ITH5", "Emilia-Romagna", inplace=True)
italy_df.replace("ITH1", "Trentino-Alto Adige", inplace=True)
italy_df.replace("ITH2", "Trentino-Alto Adige", inplace=True)
italy_df.replace("ITI1", "Toscana", inplace=True)
italy_df.replace("ITI2", "Umbria", inplace=True)
italy_df.replace("ITI3", "Marche", inplace=True)
italy_df.replace("ITI4", "Lazio", inplace=True)
italy_df.replace("ITC1", "Piemonte", inplace=True)
italy_df.replace("ITC2", "Valle d'Aosta", inplace=True)
italy_df.replace("ITC3", "Liguria", inplace=True)
italy_df.replace("ITC4", "Lombardia", inplace=True)
italy_df.replace("ITF1", "Abruzzo", inplace=True)
italy_df.replace("ITF2", "Molise", inplace=True)
italy_df.replace("ITF3", "Campania", inplace=True)
italy_df.replace("ITF4", "Puglia", inplace=True)
italy_df.replace("ITF5", "Basilicata", inplace=True)
italy_df.replace("ITF6", "Calabria", inplace=True)
italy_df.replace("ITG1", "Sicilia", inplace=True)
italy_df.replace("ITG2", "Sardegna", inplace=True)
italy_df.replace("IT", "Nazionale", inplace=True)

#delete the column reportiong country
italy_df.drop(['ReportingCountry'], axis=1, inplace=True)

italy_df.head(30)

#rename the column 'tot doses'
italy_df.rename(columns = {'tot doses':'Doses'}, inplace = True)

#select all the values in 'TargetGroup' except 'LTF' and 'HCW'
italy_df=italy_df[(italy_df.TargetGroup!='LTCF') & (italy_df.TargetGroup!='HCW')]

#select all the values for the 'Region' except 'Nazionale'
region_df=italy_df[(italy_df.Region!='Nazionale')]

#select values only for the year 2021 
region_df_21=region_df[region_df["Year"]=='2021']

#create a pivot table and then a dataframe  
group_reg=region_df_21.pivot_table(index='Region', values='Doses', aggfunc='sum').reset_index()

#select only 'Nazionale' for the column 'Region' and 'ALL' for the 'TargetGroup' 
italy_fasce=italy_df[(italy_df.Region=='Nazionale')]
italy_fasce=italy_fasce[italy_fasce.TargetGroup!='ALL']

#from a pivot table create a dataframe
df_doses_age=pd.pivot_table(italy_fasce, values=['FirstDose', 'SecondDose', 'DoseAdditional1'],index=['TargetGroup'],aggfunc='sum').reset_index()

#create a dataframe for 'Region' corresponding to 'Nazionale' and as 'Target Group' the entire population (Age<18 and ALL)
total_italy=italy_df[(italy_df.Region=='Nazionale') & (italy_df.TargetGroup=='ALL') | (italy_df.TargetGroup=='Age<18')]
#see the total doses administered in Italy per Year with this groupby
total_italy.groupby(['Year'])['Doses'].sum()

#create a df only for the values 'Region' equal to 'Nazionale' and a new df including only 'TargetGroup' equal to 'ALL'
vaccine_type=italy_df[(italy_df.Region=='Nazionale')]
vaccine_type=vaccine_type[vaccine_type.TargetGroup=='ALL']
vaccine_type

#create a df from a pivot table 
df_vaccine=vaccine_type.pivot_table(index=['YearWeekISO','Vaccine'], values='Doses', aggfunc='sum').reset_index()
df_vaccine


from datetime import datetime
from datetime import date
#cretae a fucntion to convert the YearWeek format
def convert_from_ISO_to_date(d):
    return datetime.strptime(d + '-1', "%Y-W%W-%w")

#if the character at position 5 of the column YearWeekISO at index 0 is equal to 'W' then
if df_vaccine['YearWeekISO'][0][5]=='W':
    result=[]
    for i in df_vaccine['YearWeekISO']:
        i=convert_from_ISO_to_date(i)
        string=str(i)[0:7]
        result.append(string)
    df_vaccine['YearWeekISO']=result #put the result list into the column YearWeekISO

#split the column in two columns
    df_vaccine[['Year', 'Month']]=df_vaccine['YearWeekISO'].str.split('-', expand=True)

#select only the value different from 2020 and create a copy to avoid problem (SettingWithCopyWarning: A value is trying to be set on a copy of a slice from a DataFrame.)
#If you modify values in df later you will find that the modifications do not propagate back to the original data, and that Pandas does warning
df_vaccine_2021=df_vaccine[df_vaccine.Year!='2020'].copy()

#rename the value for the Month column
df_vaccine_2021.replace("01", "Jan", inplace=True)
df_vaccine_2021.replace("02", "Feb", inplace=True)
df_vaccine_2021.replace("03", "Mar", inplace=True)
df_vaccine_2021.replace("04", "Apr", inplace=True)
df_vaccine_2021.replace("05", "May", inplace=True)
df_vaccine_2021.replace("06", "Jun", inplace=True)
df_vaccine_2021.replace("07", "Jul", inplace=True)
df_vaccine_2021.replace("08", "Aug", inplace=True)
df_vaccine_2021.replace("09", "Sep", inplace=True)
df_vaccine_2021.replace("10", "Oct", inplace=True)
df_vaccine_2021.replace("11", "Nov", inplace=True)
df_vaccine_2021.replace("12", "Dec", inplace=True)
