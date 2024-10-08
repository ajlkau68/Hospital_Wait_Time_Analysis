from dash import Dash, html, dcc, Output, Input
import plotly.express as px
from components.ids import WAIT_TIME_BAR_CHART, DAY_DROPDOWN
from data.source import DataSource, DataSchema


def create_wait_time_bar_chart(app: Dash, source:DataSource) -> html.Div:

    @app.callback(Output(WAIT_TIME_BAR_CHART, 'children'),
                   Input(DAY_DROPDOWN, 'value'))
    def update_chart(days: list[str]) -> html.Div:
        filtered_source = source.filter(days)

        if not filtered_source.row_count:
            return html.Div('No data selected', id=WAIT_TIME_BAR_CHART)

        fig = px.scatter(filtered_source.get_day_wait_data(), y=DataSchema.WAIT_MINUTES, x=DataSchema.DAY_OF_WEEK,
                     size=DataSchema.PATIENT_ID,
                    #  color=DataSchema.PATIENT_ID,
                     title='Effect of Patient Count on Wait Time per Day',
                     labels={
                         DataSchema.PATIENT_ID: 'No. of Patients',
                         DataSchema.DAY_OF_WEEK: '',
                         DataSchema.WAIT_MINUTES:'Wait Time'},
                         color_continuous_scale=['lightblue', 'skyblue', 'blue'],
                         height=500)
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
        return html.Div(dcc.Graph(figure=fig), id=WAIT_TIME_BAR_CHART)

    return html.Div(dcc.Graph(),id=WAIT_TIME_BAR_CHART)
