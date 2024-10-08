from dash import Dash, html, dcc, Output, Input
import plotly.express as px
from components.ids import DAY_TYPE_BAR_CHART, DAY_DROPDOWN
from data.source import DataSource, DataSchema


def create_minutes_line_chart(app: Dash, source:DataSource) -> html.Div:

    @app.callback(Output(DAY_TYPE_BAR_CHART, 'children'),
                   Input(DAY_DROPDOWN, 'value'))
    def update_bar_chart(days: list[str]) -> html.Div:
        filtered_source = source.filter(days)

        if not filtered_source.row_count:
            return html.Div('No data selected', id=DAY_TYPE_BAR_CHART)

        fig = px.line(filtered_source.get_minutes_per_day_data(), y=DataSchema.WAIT_MINUTES, x=DataSchema.DAY_OF_WEEK,
                     title='Average Wait Minutes per Weekday ',
                     labels={
                         DataSchema.WAIT_MINUTES: 'Wait Minutes',
                         DataSchema.DAY_OF_WEEK: ''},
                         height=500)
        fig.update_traces(line_color = 'cornflowerblue', textfont=dict(color='white'))
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
        return html.Div(dcc.Graph(figure=fig), id=DAY_TYPE_BAR_CHART)

    return html.Div(dcc.Graph(),id=DAY_TYPE_BAR_CHART)
