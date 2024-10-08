from dash import Dash, html, Input, Output
import dash_bootstrap_components as dbc
from components.ids import PATIENTS_CARD, CONSULTATION_CARD, FINANCIAL_CARD, PROCESS_CARD, WAIT_MINUTES_CARD
from components.ids import DAY_DROPDOWN, TEXT_CARDS
from data.source import DataSource


def create_metrics_cards(app:Dash, source:DataSource) -> html.Div:

    @app.callback([Output(PATIENTS_CARD, 'children'),
                   Output(WAIT_MINUTES_CARD, 'children'),
                   Output(CONSULTATION_CARD, 'children'),
                   Output(PROCESS_CARD, 'children'),
                   Output(FINANCIAL_CARD, 'children')],
                   [Input(DAY_DROPDOWN, 'value')])
    def update_text_cards(days: list[str]) -> html.Div:
        filtered_source = source.filter(days)
        
        if not filtered_source.row_count:
            return ['0', '0', '0', '0', '0']
        else:
            return filtered_source.get_text_data()


    return html.Div(
        [
            dbc.Col([
                dbc.Card([
                    # Patients Card
                    dbc.CardBody([
                        html.H6('No. of Patients', style={'fontSize':15}),
                        html.H2(id=PATIENTS_CARD, children="000")
                    ], style={'textAlign':'center', 'color':'white'})
                ], style={'backgroundColor':'cornflowerblue', 'padding':'2px'}),
            ], class_name='two columns'),
            dbc.Col([
                dbc.Card([
                    # Avg Wait Minutes Card
                    dbc.CardBody([
                        html.H6('Average Wait Minutes', style={'fontSize':15}),
                        html.H2(id=WAIT_MINUTES_CARD, children="000")
                    ], style={'textAlign':'center', 'color':'white'})
                ], style={'backgroundColor':'cornflowerblue', 'padding':'2px'}),
            ], class_name='two columns'),
            dbc.Col([
                dbc.Card([
                    # Consultation Period %
                    dbc.CardBody([
                        html.H6('Consultation Period %', style={'fontSize':15}),
                        html.H2(id=CONSULTATION_CARD, children="000")
                    ], style={'textAlign':'center', 'color':'white'})
                ], style={'backgroundColor':'cornflowerblue', 'padding':'2px'}),
            ], class_name='two columns'),
            dbc.Col([
                dbc.Card([
                    # Process Period %
                    dbc.CardBody([
                        html.H6('Process Period %', style={'fontSize':15}),
                        html.H2(id=PROCESS_CARD, children="000")
                    ], style={'textAlign':'center', 'color':'white'})
                ], style={'backgroundColor':'cornflowerblue', 'padding':'2px'}),
            ], class_name='two columns'),
            dbc.Col([
                dbc.Card([
                    # Financial Class
                    dbc.CardBody([
                        html.H6('Financial Class', style={'fontSize':15}),
                        html.H2(id=FINANCIAL_CARD, children="000")
                    ], style={'textAlign':'center', 'color':'white'})
                ], style={'backgroundColor':'cornflowerblue', 'padding':'2px'}),
            ], class_name='two columns'),
        ], className='row ms-0', id=TEXT_CARDS
    )