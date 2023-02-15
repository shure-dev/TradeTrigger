from dash import html, dcc
import plotly.express as px
import pandas as pd
from sklearn.decomposition import PCA
import dash_bootstrap_components as dbc
from component.style import BORDER_STYLE,FIGURE_STYLE,border_style,TEXT_STYLE,INPUT_STYLE
from component.layout import row_background


def ts_plot():
    df = pd.read_csv(
        'https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

    fig = px.line(df, x='Date', y='AAPL.High',
                  title='Time Series with Range Slider and Selectors')

    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(count=6, label="6m", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(step="all")
            ])
        )
    )

    fig.update_layout(FIGURE_STYLE)

    return dcc.Graph(
        figure=fig,
    )


def twitter_user_select():
    return html.Div(dbc.Row([

        html.H6("User", style=TEXT_STYLE),
        dcc.Input(
            id="input_userid",
            type="search",
            placeholder="UserId",
            style=INPUT_STYLE
        )
    ]))

def twitter_keyword():
    return html.Div(dbc.Row([

        html.H6("Keyword", style=TEXT_STYLE),
        dcc.Input(
            id="input_keyword",
            type="search",
            placeholder="Keyword", 
            style=INPUT_STYLE
        )
    ]))


def stock_ticker():
    return html.Div(dbc.Row([

        html.H6("Stock, ETF or Crypto", style=TEXT_STYLE),
        dcc.Input(
            id="input_ticker",
            type="search",
            placeholder="Ticker", 
            style=INPUT_STYLE
        )
    ]))

# def time_start():
#     return html.Div(dbc.Row([

#         html.H6("Time start", style=TEXT_STYLE),
#         dcc.Input(
#             id="input_ticker",
#             type="search",
#             placeholder="Ticker", 
#             style=INPUT_STYLE
#         )
#     ]))

def order_amount():
    return html.Div(dbc.Row([

        html.H6("Time end", style=TEXT_STYLE),
        dcc.Input(
            id="input_ticker",
            type="search",
            placeholder="Ticker", 
            style=INPUT_STYLE
        )
    ]))



automate_layout = html.Div(children=[


    row_background([
        twitter_user_select(),
        twitter_keyword(),
        stock_ticker(),
    ]),

    html.Div(ts_plot(), style=border_style(100)),

    row_background([
        twitter_user_select(),
        twitter_keyword(),
        stock_ticker(),
    ]),


])