import base64
import datetime
import io

import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_table

import pandas as pd


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


data = pd.read_csv('iris.csv')
app.layout = html.Div([


    dcc.Input(id = 'inputs', type='text'),
    html.Div(id='output-data-upload'),
])


@app.callback(Output('output-data-upload', 'children'),[Input('inputs','value')])
def output_Content(s):
    return str(data[s].sum())



if __name__ == '__main__':
    app.run_server(debug=True)