## How the project is structured
Every foldes was create to make an analysis of an argument. Each of them contains:
1. the datasets
2. .py file for ETL process
4. .ipynb file chart generator (sometimes even the .ipynb file for chart function) 
## The folders
1. ***vaccination_ue_analysis***: there are an short analysis of vaccination campaing in UE.
2. ***vaccination_it_analysis***: here the analysis of the vaccination campaign is more specific to italy
3. ***covid19_test_analysis***: for comprehensiveness; the results of the tests have been analyzed 
4. ***icu_analysis***: here we analyzed the effect of vaccination campaing to icu
5. ***death_analysis***: here we analyzed the effect of vaccination campaing to death
6. ***drug_company_analysis***: for each drug companies was made a stock analysis
7. ***drug_company_analysis***: A stock market analysis was made for the main index
8. ***pollution_analysis***: to give to the project an environment aspect we studies the main pollution index over 2019,2020 and 2021
9. ***dashboard***: to raise the level we have implemented a dashboard. 

        NB: Keep in mind that we put only the 'vaccination_ue_analys' and 'pollution_analysis' on the dashboard.  
        The goal was to learn how to make a dashboard from a technical standpoint.

## The source

The datasets use for this project are:
- https://www.ecdc.europa.eu/en/publications-data/covid-19-testing
- https://www.ecdc.europa.eu/en/publications-data/data-covid-19-vaccination-eu-eea
- https://ourworldindata.org/covid-vaccinations
- https://aqicn.org/data-platform/covid19/

## The libraries 
We use the following libraries to make our analysis:
- [matplotlib](https://matplotlib.org/)
- [pandas](https://pandas.pydata.org/docs/) 
- [plotly](https://plotly.com/python/)
- [yfinance](https://pypi.org/project/yfinance/)
- [datetime](https://docs.python.org/3/library/datetime.html)
- [ipywidges](https://ipywidgets.readthedocs.io/en/latest/)
- [glob](https://docs.python.org/3/library/glob.html)
- [dash](https://dash.plotly.com/)
- [os](https://docs.python.org/3/library/os.html)

# How to run project
Before running a single file make sure you are inside the project folder. 
No other caution is necessary
## Running the local dashboard

The dashboard will run only in **localhost** so, on port [localhost:8050](localhost:8050) your computer will be the server.

We create a ***Makefile*** which contains some command that will run in your terminal.

Thanks to it; initialize the dashboard is super easy :)

Run the following command on you terminal
```
make run
```



