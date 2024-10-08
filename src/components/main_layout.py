from dash import html, Dash 
import dash_bootstrap_components as dbc 
from components.day_dropdown import create_day_dropdown
from components.header import create_header
from components.text_cards import create_metrics_cards
from components.heatmap_chart import create_heatmap_chart
from components.combo_chart import create_combo_chart
from components.minutes_line_chart import create_minutes_line_chart
from components.patient_bar_chart import create_patient_bar_chart
from components.wait_time_bar_chart import create_wait_time_bar_chart
from data.source import DataSource



def create_layout(app: Dash, source:DataSource):
    return dbc.Container([
    # Header row
    dbc.Row([
        dbc.Col(create_header(app))
    ],className='mb-3 mt-2', 
    style={'backgroundColor':'cornflowerblue', 'padding':'5px'}),
    # Dropdowns
    dbc.Row([
        dbc.Col([create_day_dropdown(app, source)], width=12),
    ],className='mb-3'),
    # Metrics Cards
    dbc.Row([
        create_metrics_cards(app, source)
    ],className='mb-3'),
    # Graphs
    dbc.Row([
        dbc.Col([
            dbc.Card([
                html.Div([
                    create_patient_bar_chart(app, source),
                ])
            ]),
        ], width=5),
        dbc.Col([
            dbc.Card([
                html.Div([
                    create_wait_time_bar_chart(app, source),
                ])
            ]),
        ], width=7),
    ],className='mb-3'),
    # Graph
    dbc.Row([
        dbc.Col([
            dbc.Card([
                html.Div([
                    create_minutes_line_chart(app, source),
                ])
            ]),
        ], width=5),
        dbc.Col([
            dbc.Card([
                html.Div([
                    create_heatmap_chart(app, source),
                ])
            ]),
        ], width=7),
        
    ],className='mb-3'),

    # Combo Chart
    dbc.Row([
        dbc.Col([
            dbc.Card([
                html.Div([
                    create_combo_chart(app, source),
                ])
            ]),
        ])
        
    ],className='mb-3'),
    
    ], fluid=True, style={'backgroundColor':'whitesmoke'})
