# How the project is structured

## Type of filesystem
The files for the ETL process of the datasets are:
1. *etl_ecdc.py* 
2. *etl_death_analysis.py*
3. *etl_icu_dataframe.py*
4. *etl_vaccination_dataframe.py*
5. *etl_pollution_dataframe.py*

The files for the chart generation are:
1. *ecdc_analysis_charts_generator.ipynb* 
2. *deaths_analysis_charts_generator.ipynb*
3. *etl_icu_dataframe.py*
4. *vaccination_charts_generator.ipynb.py*
5. *pollution_charts_generator.ipynb*


The datasets use for this project are:
- https://aqicn.org/data-platform/covid19/
- ...
- ...

## How to run the Dashboard

The dashboard will run only in localhost so, run it and open the browser to [localhost:8050](localhost:8050).
Run the following command on you terminal
```
make run
```



