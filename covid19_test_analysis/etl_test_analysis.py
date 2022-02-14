import pandas as pd
#load the file 
testing=pd.read_csv(r'testing_data.csv')
testing
#create a datframe with data only for Italy
test_ita=testing[testing['country']=='Italy'].reset_index()


#create a function to convert the date from the yearweek format
from datetime import datetime
from datetime import date
def convert_from_ISO_to_date(d):
    return datetime.strptime(d + '-1', "%Y-W%W-%w")

if test_ita['year_week'][0][5]=='W':
    result=[]
    for i in test_ita['year_week']:
        print(i)
        i=convert_from_ISO_to_date(i)
        string=str(i)[0:7]
        result.append(string)
    test_ita['year_week']=result

#rename the region name
test_ita.replace("ITH3", "Veneto", inplace=True)
test_ita.replace("ITH4", "Friuli-Venezia Giulia", inplace=True)
test_ita.replace("ITH5", "Emilia-Romagna", inplace=True)
test_ita.replace("ITH1", "Trentino-Alto Adige", inplace=True)
test_ita.replace("ITH2", "Trentino-Alto Adige", inplace=True)
test_ita.replace("ITI1", "Toscana", inplace=True)
test_ita.replace("ITI2", "Umbria", inplace=True)
test_ita.replace("ITI3", "Marche", inplace=True)
test_ita.replace("ITI4", "Lazio", inplace=True)
test_ita.replace("ITC1", "Piemonte", inplace=True)
test_ita.replace("ITC2", "Valle d'Aosta", inplace=True)
test_ita.replace("ITC3", "Liguria", inplace=True)
test_ita.replace("ITC4", "Lombardia", inplace=True)
test_ita.replace("ITF1", "Abruzzo", inplace=True)
test_ita.replace("ITF2", "Molise", inplace=True)
test_ita.replace("ITF3", "Campania", inplace=True)
test_ita.replace("ITF4", "Puglia", inplace=True)
test_ita.replace("ITF5", "Basilicata", inplace=True)
test_ita.replace("ITF6", "Calabria", inplace=True)
test_ita.replace("ITG1", "Sicilia", inplace=True)
test_ita.replace("ITG2", "Sardegna", inplace=True)
test_ita.replace("IT", "Nazionale", inplace=True)

#split the yearweek in two column
test_ita[['Year', 'Month']]=test_ita['year_week'].str.split('-', expand=True)

#drop column 
test_ita.drop(['year_week', 'region', 'population', 'testing_data_source'], axis=1, inplace=True)

#create a df with only national data
ita_overall=test_ita[test_ita.level=='national']

#dataframe for nes cases and tests done
tot_ita=ita_overall.pivot_table(index=['Year', 'Month'], values=['new_cases', 'tests_done'], aggfunc='sum').reset_index()

#add rows for the month without values
tot_ita=tot_ita[tot_ita.Year!='2022']
top_rows=pd.DataFrame({'Year':['2020','2020', '2020', '2020'], 'Month':['01', '02', '07', '08'], 'new_cases':[0.0,0.0, 0.0,0.0], 'tests_done':[0.0,0.0,0.0,0.0]})
df_ita=pd.concat([top_rows, tot_ita]).reset_index(drop = True)
df_sort=df_ita.sort_values(by=['Year', 'Month'])

#change the value from '01' to 'Jan'
df_sort.replace("01", "Jan", inplace=True)
df_sort.replace("02", "Feb", inplace=True)
df_sort.replace("03", "Mar", inplace=True)
df_sort.replace("04", "Apr", inplace=True)
df_sort.replace("05", "May", inplace=True)
df_sort.replace("06", "Jun", inplace=True)
df_sort.replace("07", "Jul", inplace=True)
df_sort.replace("08", "Aug", inplace=True)
df_sort.replace("09", "Sep", inplace=True)
df_sort.replace("10", "Oct", inplace=True)
df_sort.replace("11", "Nov", inplace=True)
df_sort.replace("12", "Dec", inplace=True)

