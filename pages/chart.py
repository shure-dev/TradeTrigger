from dash import html, dcc
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from component.style import BORDER_STYLE,FIGURE_STYLE,border_style
from component.layout import row

chart_layout = html.Div(children=[

    html.H2(children='Chart Page', style={'color': 'white'}),

])