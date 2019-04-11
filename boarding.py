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

app.layout = html.Div([
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '25%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px',
            'display':'inline-block'
        },
        # Allow multiple files to be uploaded
        multiple=True
    ),

    html.Div(id='output-data-upload',style={'display':'none'}),

    #dcc.Input(id = 'column-name',type='text'),
    html.Div([dcc.Dropdown(id = 'colors')],style={'width':'25%','display':'inline-block'}),

    html.Div(id='check')
])



@app.callback(Output('output-data-upload','children'),[Input('upload-data','contents')])
def fun (contents):
    #print(contents[0].split(','))
    content_type, content_string = contents[0].split(',')
    decoded = base64.b64decode(content_string)
    df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
    return df.to_json()


@app.callback(Output('colors','options'),[Input('output-data-upload','children')])
def update_dropdown(x):
    data = pd.read_json(x)
    return [{'label': i, 'value': i} for i in data.columns]

@app.callback(Output('check','children'),
              [Input('output-data-upload','children'),Input('colors','value')])

def checks(x,y):
    data = pd.read_json(x)
    return str(data[y].sum())

if __name__ =='__main__':
    app.run_server(debug = True)