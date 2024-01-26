import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import datetime


# Initialize the Dash app
app = dash.Dash(__name__)

# Layout of the app

app.layout = html.Div([
    html.Div(className='container', children=[

        html.Div(className="clock", children=[
            html.Div(className="date", children=[
                dcc.Interval(id='date-interval', interval=60*1000, n_intervals=0),
                html.Div(id='date-container', className='dashboard-item'),
            ]),
            html.Div(className="time", children=[
                dcc.Interval(id='time-interval', interval=1*1000, n_intervals=0),
                html.Div(id='time-container', className='dashboard-item'),
            ])
        ])
    ])
])


@app.callback(Output('date-container', 'children'),
              [Input('date-interval', 'n_intervals')])
def update_date(n):
    now = datetime.datetime.now()
    formatted_date = now.strftime("%A %d %B")
    return formatted_date

@app.callback(Output('time-container', 'children'),
              [Input('time-interval', 'n_intervals')])
def update_time(n):
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M")
    return current_time


# Run the app
if __name__ == '__main__':
    app.run_server(debug=False, host="0.0.0.0")
