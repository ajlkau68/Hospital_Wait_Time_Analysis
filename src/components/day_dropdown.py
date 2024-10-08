from dash import Dash, html, dcc, Output, Input
from components.ids import DAY_DROPDOWN, SELECT_ALL_BUTTON
from data.source import DataSource
import dash_bootstrap_components as dbc

# day_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def create_day_dropdown(app: Dash, source:DataSource) -> html.Div:

    @app.callback(Output(DAY_DROPDOWN, 'value'),
                  [Input(SELECT_ALL_BUTTON, 'n_clicks')])
    def update_days(days: list[str]) -> list[str]:
        return source.unique_days
    

    return html.Div(
        [
            html.H5('Select Day(s)', style={'textAlign': 'left', 'fontSize':15}, className='ms-2'),
            dcc.Dropdown(
                id=DAY_DROPDOWN,
                options=[{'label':day, 'value':day} for day in source.unique_days],
                multi=True,
                clearable=False,
                value=source.unique_days,  
            ),
            dbc.Button('Select All', color='primary', outline=True, 
                       id=SELECT_ALL_BUTTON, n_clicks=0, size='sm', className='ms-2')
        ], className='hstack gap-3', 
    )

        