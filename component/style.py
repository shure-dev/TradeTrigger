SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#080124",
}

CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

NAVLINK_STILE = {
    'color': 'white', 'fontSize': 20
}


BORDER_STYLE = {"border": "2px white transparent",
                'margin': 20, 'border-radius': 10, 'background': '#181240',
                'width': '90%','color': 'white'}

FIGURE_STYLE = {
    'plot_bgcolor': 'rgba(0, 0, 0, 0)',
    'paper_bgcolor': 'rgba(0, 0, 0, 0)',
    "legend_font_color": "white",
    "title_font_color": "white"
}

TEXT_STYLE ={
    'color': 'white', 'margin': 20
}

INPUT_STYLE ={
    'color': 'black', 'margin-left': 30,'margin-bottom': 20,'width': '80%'
}

def border_style(percent):
    return {"border": "2px white transparent",
            'margin': 20, 'border-radius': 10, 'background': '#181240',
            'width': f'{percent}%'}
