from dash import Dash, html, dcc, Output, Input
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from components.ids import COMBO_CHART, DAY_DROPDOWN
from data.source import DataSource, DataSchema


def create_combo_chart(app: Dash, source:DataSource) -> html.Div:

    @app.callback(Output(COMBO_CHART, 'children'),
                   Input(DAY_DROPDOWN, 'value'))
    def update_combo_chart(days: list[str]) -> html.Div:
        filtered_source = source.filter(days)

        if not filtered_source.row_count:
            return html.Div('No data selected', id=COMBO_CHART)

        filtered_data = filtered_source.get_combo_chart_data()
        fig = make_subplots(specs=[[{'secondary_y':True}]])
        fig.add_trace(
            go.Scatter(
                x=filtered_data[DataSchema.ENTRY_HOUR], y=filtered_data[DataSchema.PATIENT_ID],
                name='No. of Patients', marker={'color':'darkorange'}, mode='lines+markers',
            ), secondary_y=True
        )
        fig.add_trace(
            go.Bar(
                x=filtered_data[DataSchema.ENTRY_HOUR], y=filtered_data[DataSchema.WAIT_MINUTES],
                name='Wait Minutes', marker={'color':'steelblue'}
            ), secondary_y=False
        )
        fig.update_layout(title_text='Effect of Entry Hour on Wait Time',
                          height=500,
                          template='plotly_white',
                          title_font=dict(size=16, family="Arial", color='grey'),
                          legend=dict(x=0, y=1.1, xanchor='left', yanchor='top'),
                          legend_orientation='h', legend_font_size=10)
        fig.update_xaxes(title_text='Entry Hour',
                            showgrid=False,
                            showline=False,
                            tickfont=dict(size=10),
                            tickmode='linear',
                            tick0=1),
        fig.update_yaxes(title_text=DataSchema.WAIT_MINUTES,
                            showgrid=True,
                            showline=False,
                            secondary_y=False,
                            tickfont=dict(size=10))
        fig.update_yaxes(title_text=DataSchema.PATIENT_ID,
                            showgrid=False,
                            showline=False,
                            secondary_y=True,
                            tickfont=dict(size=10))
        return html.Div(dcc.Graph(figure=fig), id=COMBO_CHART)

    return html.Div(dcc.Graph(), id=COMBO_CHART)
