
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
