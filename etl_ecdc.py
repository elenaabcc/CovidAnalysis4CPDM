import pandas as pd

ecdc_iniziale=pd.read_csv(r'C:\Users\strag\Documents\GitHub\CovidAnalysis4CPDM\PROGETTO\ECDC dataset iniziale.csv')
ecdc_iniziale.head(30)

ecdc_iniziale.drop(['NumberDosesReceived','NumberDosesExported', 'FirstDoseRefused'], axis=1, inplace=True)

italy_df=ecdc_iniziale.copy()
group=['IT']
italy_df = italy_df[italy_df['ReportingCountry'].isin(group)]

italy_df['tot doses']= italy_df['FirstDose']+italy_df['SecondDose']+ italy_df['DoseAdditional1']+italy_df['UnknownDose']

italy_df[['Year', 'Week']]=italy_df['YearWeekISO'].str.split('-', expand=True)

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

italy_df.drop(['ReportingCountry'], axis=1, inplace=True)

italy_df.head(30)
italy_df.rename(columns = {'tot doses':'Doses'}, inplace = True)

italy_df=italy_df[(italy_df.TargetGroup!='LTCF') & (italy_df.TargetGroup!='HCW')]

region_df=italy_df[(italy_df.Region!='Nazionale')]

region_df_21=region_df[region_df["Year"]=='2021']

group_reg=region_df_21.pivot_table(index='Region', values='Doses', aggfunc='sum').reset_index()

italy_fasce=italy_df[(italy_df.Region=='Nazionale')]
italy_fasce=italy_fasce[italy_fasce.TargetGroup!='ALL']

df_doses_age=pd.pivot_table(italy_fasce, values=['FirstDose', 'SecondDose', 'DoseAdditional1'],index=['TargetGroup'],aggfunc='sum').reset_index()

total_italy=italy_df[(italy_df.Region=='Nazionale') & (italy_df.TargetGroup=='ALL') | (italy_df.TargetGroup=='Age<18')]
total_italy.groupby(['Year'])['Doses'].sum()

vaccine_type=italy_df[(italy_df.Region=='Nazionale')]
vaccine_type=vaccine_type[vaccine_type.TargetGroup=='ALL']
vaccine_type

df_vaccine=vaccine_type.pivot_table(index=['YearWeekISO','Vaccine'], values='Doses', aggfunc='sum').reset_index()
df_vaccine

from datetime import datetime
from datetime import date

def convert_from_ISO_to_date(d):
    return datetime.strptime(d + '-1', "%Y-W%W-%w")

if df_vaccine['YearWeekISO'][0][5]=='W':
    result=[]
    for i in df_vaccine['YearWeekISO']:
        i=convert_from_ISO_to_date(i)
        string=str(i)[0:7]
        result.append(string)
    df_vaccine['YearWeekISO']=result

    df_vaccine[['Year', 'Month']]=df_vaccine['YearWeekISO'].str.split('-', expand=True)

df_vaccine_2021=df_vaccine[df_vaccine.Year!='2020']

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
