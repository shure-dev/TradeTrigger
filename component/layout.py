import dash_bootstrap_components as dbc
from component.style import BORDER_STYLE

def row_background(components: list):
    return dbc.Row([dbc.Col(component) for component in components],style=BORDER_STYLE)

def row_simple(components: list):
    return dbc.Row([dbc.Col(component) for component in components])