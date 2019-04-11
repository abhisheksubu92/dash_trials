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
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=True
    ),

    html.Div(id='output-data-upload',style={'display':'none'}),

    dcc.Input(id = 'column-name',type='text'),
    html.Div(id='output-data')
])



@app.callback(Output('output-data-upload','children'),[Input('upload-data','contents')])
def fun (contents):
    content_type, content_string = contents[0].split(',')
    decoded = base64.b64decode(content_string)
    df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
    return df.to_json()

@app.callback(Output('output-data','children'),
              [Input('output-data-upload','children'),Input('column-name','value')]

              )
def fun1(data,column):
    df =pd.read_json(data)
    value = df[column].sum()
    return str(value)


if __name__ =='__main__':
    app.run_server(debug=True)