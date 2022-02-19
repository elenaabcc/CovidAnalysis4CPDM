from plotly.subplots import make_subplots
import plotly.graph_objects as go

# [[df1,df2, ... ], [dfa,dfb, ...]]
def generateTimeSeriesChartOverYears(dataframesMatrix, xaxis, yaxis, palette):
    fig = make_subplots(rows=len(dataframesMatrix),
                        cols=1, vertical_spacing=0.1)
    for i, dfs in enumerate(dataframesMatrix):
        for j, df in enumerate(dfs):
            fig.add_trace(go.Scatter(x=df[xaxis], y=df[yaxis], line=dict(
                width=2, color=palette[j]), stackgroup=str(j)), row=i+1, col=1)
    return fig

def generateTimeSeriesChartWithSubplots(dataFrames, titles, xaxisLabel, yaxisLabel):
    fig = make_subplots(rows=len(dataFrames), cols=1, vertical_spacing=0.1)
    for i, df in enumerate(dataFrames):
        fig.add_trace(go.Scatter(
            x=df[xaxisLabel], y=df[yaxisLabel], line=dict(width=2)), row=i+1, col=1)
    return fig

'''
Limits to be consider:

- Daily Limit 	50 µg/m³ (not to be exceeded for more than 35 days per year)
- Annual Limit	40 µg/m³ (annual average)
'''

'''
city = Rome, Bucharest, ...
yearDict = {'2019':df, '2020':df, '2021':df}
'''
def generatePm10EvaluationTable(city, yearsDict):
    header = dict(values=['Year','Day count where Pm10>50µg/m³', 'rate of exceeding legal limits', 'Pm10 Annual Average', 'Variance of Pm10'])

    yearColumnList = []
    dayCountWherePm10ExceedList = []
    rateExceedingLegalLimitList = []
    pm10AnnualAverageList = []
    varianceOfPm10List = []

    for year, df in yearsDict.items():
        yearColumnList.append(city + ' ' + year)
        dayCountWherePm10ExceedList.append(len(df[df['max'] > 50]))
        rateExceedingLegalLimitList.append(str(round(len(df[df['max']>50]) / len(df['max']) * 100, 2)))
        pm10AnnualAverageList.append(round(df['max'].mean(), 2))
        varianceOfPm10List.append(round(df.var()['max'], 2))

    cells = dict(values=[
        yearColumnList,
        dayCountWherePm10ExceedList,
        rateExceedingLegalLimitList,
        pm10AnnualAverageList,
        varianceOfPm10List
    ])

    return go.Figure(data=[go.Table(
        header = header,
        cells = cells
    )])