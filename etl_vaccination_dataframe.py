
import pandas as pd
import os
import glob

# https://ourworldindata.org/covid-vaccinations
data_covid19_owid = pd.read_csv("./covid19_dataframes/owid-covid-data.csv")
data_covid19_owid = data_covid19_owid.query("iso_code == 'ITA'")

data_covid19_owid = data_covid19_owid[['iso_code','date', 'location', 'continent', 'new_cases', 'new_deaths', 'total_cases', 
                                        'total_deaths', 'reproduction_rate', 'icu_patients', 'aged_65_older', 'aged_70_older',
                                        'median_age', 'extreme_poverty', 'gdp_per_capita', 'cardiovasc_death_rate', 'diabetes_prevalence',
                                        'new_tests', 'total_tests','positive_rate', 'excess_mortality'
                                    ]]


# https://www.ecdc.europa.eu/en/publications-data/data-covid-19-vaccination-eu-eea
data_covid19_ecdc= pd.read_csv("./covid19_dataframes/data_covid19_vaccination.csv")
data_covid19_ecdc.drop(['NumberDosesReceived','NumberDosesExported', 'FirstDoseRefused'], axis=1, inplace=True)

splitedYearWeekISO = data_covid19_ecdc["YearWeekISO"].str.split("-", n = 1, expand = True)
data_covid19_ecdc['Year']= splitedYearWeekISO[0]
data_covid19_ecdc['Week']= splitedYearWeekISO[1]

data_covid19_ecdc = data_covid19_ecdc[data_covid19_ecdc["Population"] == data_covid19_ecdc["Denominator"]] 
data_covid19_ecdc = data_covid19_ecdc[data_covid19_ecdc["TargetGroup"]=='ALL']
 
data_covid19_ecdc_2021 = data_covid19_ecdc[data_covid19_ecdc["Year"]=='2021']
data_covid19_ecdc_2021 = data_covid19_ecdc_2021.groupby(['Year','ReportingCountry', 'Vaccine'],as_index=False).sum()
data_covid19_ecdc_2021['TotDoses']=data_covid19_ecdc_2021['FirstDose']+data_covid19_ecdc_2021['SecondDose']+data_covid19_ecdc_2021['DoseAdditional1']+data_covid19_ecdc_2021['UnknownDose']

data_covid19_ecdc_2021['TotDosesAllVaccines'] = data_covid19_ecdc_2021['TotDoses'].groupby(data_covid19_ecdc_2021['ReportingCountry']).transform('sum')



