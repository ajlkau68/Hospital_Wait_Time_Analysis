from dash import Dash, html, dcc, Output, Input
import plotly.express as px
from components.ids import HEAT_MAP_CHART, DAY_DROPDOWN
from data.source import DataSource, DataSchema


px.defaults.template = 'plotly_white'

def create_heatmap_chart(app: Dash, source:DataSource) -> html.Div:

    @app.callback(Output(HEAT_MAP_CHART, 'children'),
                   Input(DAY_DROPDOWN, 'value'))
    def update_heat_map(days: list[str]) -> html.Div:
        filtered_source = source.filter(days)

        if not filtered_source.row_count:
            return html.Div('No data selected', id=HEAT_MAP_CHART)

        fig = px.imshow(filtered_source.get_entry_hour_minutes(),
                        labels=dict(x='', y=DataSchema.ENTRY_HOUR),
                        title='Daily Wait Minutes per Entry Hour',
                        x=sorted(days),
                        y=list(range(8, 24)),
                        text_auto=True,
                        height=500,
                        color_continuous_scale='blues',
                        color_continuous_midpoint=44)
        fig.update_xaxes(side='top')
        fig.update_traces(textfont=dict(size=10))
        fig.update_layout(title_font=dict(size=16, family="Arial", color='grey'),
                        xaxis=dict(
                            showgrid=False,
                            showline=False,
                            tickfont=dict(size=11)),
                        yaxis=dict(
                            showgrid=False,
                            showline=True,
                            tickfont=dict(size=11),
                            tickmode='linear',
                            tick0=1)
                            )
        return html.Div(dcc.Graph(figure=fig), id=HEAT_MAP_CHART)

    return html.Div(dcc.Graph(),id=HEAT_MAP_CHART)
