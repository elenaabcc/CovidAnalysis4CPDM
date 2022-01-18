# import necessary libraries
import pandas as pd
import os
import glob


# CSV Aggregation to better elaboration
listNameCSV = [['pollution19Q1', 'pollution19Q2', 'pollution19Q3', 'pollution19Q4'],
               ['pollution20Q1', 'pollution20Q2', 'pollution20Q3', 'pollution20Q4'],
               ['pollution21Q1', 'pollution21Q2', 'pollution21Q3', 'pollution21Q4']]

# dfConcatList contains dataframes of each year
dfConcatList = []

for csvs in listNameCSV:
    dfList = []
    for csv in csvs:
        # print(csv)
        year = '20' + csv[9:11]
        # print(year)
        # read the csv of corresponding year
        temp_df = pd.read_csv("./PollutionData/"+csv+".csv")
        # remove tails (data from previous and next year of last and first month)
        temp_df = temp_df.query(
            "Date.str.contains('"+year+"')", engine='python')
        dfList.append(temp_df)
        # print(len(dfList))
    # Union data of all quarters of the same year
    result = pd.concat(dfList, axis=0, join="outer")
    # Save it to the list
    dfConcatList.append(result)


cityData = {}
cities = ['Rome', 'Bucharest', 'Oslo']
years = ['2019', '2020', '2021']
specie = 'pm10'

# Populate cities dictionary with corresponding dataframe
# The structure of cityData is {'Rome':{'2019':df, '2020':df, '2021':df}, ...}
for city in cities:
    yearDict = {}
    for i, year in enumerate(years):
        yearDict[year] = dfConcatList[i].query(
            "City == '"+city+"' and Specie =='"+specie+"'").sort_values(by='Date')
    cityData[city] = yearDict
