from dash import Dash
from dash_bootstrap_components.themes import BOOTSTRAP
from components.main_layout import create_layout
from data.loader import load_data
from data.source import DataSource


DATA_PATH = "hospital_data_full.csv"

data = load_data(DATA_PATH)
data = DataSource(data)

app = Dash(__name__, external_stylesheets=[BOOTSTRAP])
server = app.server
app.title = 'Wait Time Dashboard'
app.layout = create_layout(app, data)


if __name__ == '__main__':
    app.run_server(debug=False)

    