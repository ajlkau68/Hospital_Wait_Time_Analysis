from dash import Dash, html, dcc, Output, Input
import plotly.express as px
from components.ids import PATIENT_BAR_CHART, DAY_DROPDOWN
from data.source import DataSource, DataSchema


def create_patient_bar_chart(app: Dash, source:DataSource) -> html.Div:

    @app.callback(Output(PATIENT_BAR_CHART, 'children'),
                   Input(DAY_DROPDOWN, 'value'))
    def update_bar_chart(days: list[str]) -> html.Div:
        filtered_source = source.filter(days)

        if not filtered_source.row_count:
            return html.Div('No data selected', id=PATIENT_BAR_CHART)

        fig = px.bar(filtered_source.get_patient_day_data(), x=DataSchema.PATIENT_ID, y=DataSchema.DAY_OF_WEEK,
                     title='Patient Count per Day',
                     labels={
                         DataSchema.PATIENT_ID: 'No. of Patients',
                         DataSchema.DAY_OF_WEEK: ''},
                         orientation='h',
                         text_auto=True,
                         height=500)
        fig.update_traces(marker_color = 'cornflowerblue', textfont=dict(color='white'))
        fig.update_layout(title_font=dict(size=16, family="Arial", color='grey'),
                        xaxis=dict(
                            showgrid=False,
                            showline=False,
                            tickfont=dict(size=11)),
                        yaxis=dict(
                            showgrid=False,
                            showline=True,
                            tickfont=dict(size=11))
                            )
        return html.Div(dcc.Graph(figure=fig), id=PATIENT_BAR_CHART)

    return html.Div(dcc.Graph(),id=PATIENT_BAR_CHART)
