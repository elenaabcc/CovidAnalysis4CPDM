from plotly.subplots import make_subplots
import plotly.graph_objects as go

def generateTimeSeriesChartOverYears(dataframesMatrix, xaxis, yaxis, palette):
    fig = make_subplots(rows=len(dataframesMatrix), cols=1,vertical_spacing=0.1)
    for i, dfs in enumerate(dataframesMatrix):
        for j, df in enumerate(dfs):
            fig.add_trace(go.Scatter(x = df[xaxis], y=df[yaxis], line = dict(width=2, color = palette[j]), stackgroup=str(j)), row=i+1, col=1)
    return fig