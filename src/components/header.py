from dash import Dash, html
import dash_bootstrap_components as dbc 


def create_header(app:Dash) -> html.Div:

    return html.Div(
        [
            html.Img(src='assets/hospital-logo.jpeg', height='50px'),
            html.H5('Blue Hart Hospital', style={'textAlign':'left', 'color':'white'}, className='ms-1'),
            html.H3(app.title, style={'textAlign':'center', 'color':'white'}, className='ms-auto'),
            dbc.Button('Learn More', color='secondary', outline=True, className='ms-auto')
        ], className='hstack gap-3'
    )