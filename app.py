# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc

from pages.overview import overview_layout
from pages.automate import automate_layout
from pages.chart import chart_layout
from pages.setting import setting_layout

from component.style import SIDEBAR_STYLE,CONTENT_STYLE,NAVLINK_STILE
from __dash import app

sidebar = html.Div(
    [
        html.H3("TradeTrigger", style={'color': 'white', 'fontSize': 40}),
        html.P(
            "Automate Trade based on many resources", style={'color': 'white', 'fontSize': 15}
        ),
        html.Hr(style={'color': 'white', 'fontSize': 30}),
        dbc.Nav(
            [
                dbc.NavLink("Overview", href="/",
                            active="exact", style=NAVLINK_STILE),
                dbc.NavLink("Automate", href="/automate",
                            active="exact", style=NAVLINK_STILE),
                dbc.NavLink("Chart", href="/chart",
                            active="exact", style=NAVLINK_STILE),
                dbc.NavLink("Setting", href="/setting",
                            active="exact", style=NAVLINK_STILE),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content], style={'background': '#060030'})


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return overview_layout
    elif pathname == "/automate":
        return automate_layout
    elif pathname == "/chart":
        return chart_layout
    elif pathname == "/setting":
        return setting_layout

    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )


if __name__ == '__main__':
    app.run_server(debug=True)