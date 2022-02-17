import altair as alt
import pandas as pd
from dash import Dash, dcc, html, Input, Output

gm = pd.read_csv('https://raw.githubusercontent.com/UofTCoders/workshops-dc-py/master/data/processed/world-data-gapminder.csv', parse_dates = ['year']) # Dataframe for Gapminder data

def plot_altair(xcol):
    chart = alt.Chart(gm[(gm.year=='2015-01-01')]).mark_bar().encode(
        x=xcol,
        y='region',
        color='region',
        tooltip='population'
    ).interactive()
    return chart.to_html()

app = Dash(__name__)
app.layout = html.Div([
        dcc.Dropdown(
            id='xcol', value='population',
            options=[{'label': i, 'value': i} for i in gm.columns]),
        html.Iframe(
            id='scatter',
            srcDoc=plot_altair(xcol='population'),
            style={'border-width': '0', 'width': '100%', 'height': '400px'})])

@app.callback(
    Output('scatter', 'srcDoc'),
    Input('xcol', 'value'))

def update_output(xcol):
    return plot_altair(xcol)

if __name__ == '__main__':
    app.run_server(debug=True)