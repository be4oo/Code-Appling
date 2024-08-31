import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Sample Data
df = pd.DataFrame({
    'year': [2020, 2021, 2022, 2023],
    'feature_x': [1, 2, 3, 4],
    'feature_y': [4, 3, 2, 1],
    'feature_z': [2, 3, 4, 5]
})

# Initialize the Dash app
external_stylesheets = [
    'https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css',
    'https://use.fontawesome.com/releases/v5.8.1/css/all.css',
    'https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500&display=swap'
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Custom CSS styling
app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <style>
            body {
                font-family: 'Roboto', sans-serif;
                background-color: #f8f9fa;
            }
            .container {
                margin: 0 auto;
                max-width: 1200px;
                padding: 20px;
            }
            .header {
                text-align: center;
                padding: 20px 0;
            }
            .header-title {
                font-size: 2.5em;
                margin-bottom: 10px;
            }
            .header-description {
                font-size: 1.2em;
                color: #6c757d;
            }
            .dropdown-label {
                font-weight: 500;
                margin-bottom: 5px;
                display: block;
            }
            .dropdown {
                margin-bottom: 20px;
            }
            .slider-label {
                font-weight: 500;
                margin-bottom: 10px;
                display: block;
                text-align: center;
            }
            .slider-container {
                padding: 0 20px;
                margin-bottom: 40px;
            }
            .scatter-plot {
                margin-top: 20px;
            }
            .row {
                display: flex;
                flex-wrap: wrap;
                margin-right: -15px;
                margin-left: -15px;
            }
            .six.columns {
                width: 50%;
                padding-right: 15px;
                padding-left: 15px;
            }
            @media (max-width: 768px) {
                .six.columns {
                    width: 100%;
                    padding-right: 15px;
                    padding-left: 15px;
                }
            }
        </style>
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

# Layout of the app
app.layout = html.Div([
    html.Div([
        html.H1("Fancy Dashboard", className="header-title"),
        html.P("This is a short description of the dashboard.", className="header-description"),
    ], className="header container"),
    
    html.Div([
        html.Div([
            html.Label("Select Feature X:", className="dropdown-label"),
            dcc.Dropdown(
                id='dropdown-x',
                options=[
                    {'label': 'Feature X', 'value': 'feature_x'},
                    {'label': 'Feature Y', 'value': 'feature_y'},
                    {'label': 'Feature Z', 'value': 'feature_z'}
                ],
                value='feature_x',
                className="dropdown"
            ),
        ], className="six columns"),
        
        html.Div([
            html.Label("Select Feature Y:", className="dropdown-label"),
            dcc.Dropdown(
                id='dropdown-y',
                options=[
                    {'label': 'Feature X', 'value': 'feature_x'},
                    {'label': 'Feature Y', 'value': 'feature_y'},
                    {'label': 'Feature Z', 'value': 'feature_z'}
                ],
                value='feature_y',
                className="dropdown"
            ),
        ], className="six columns")
    ], className="row container"),
    
    html.Div([
        html.Label("Select Year:", className="slider-label"),
        dcc.Slider(
            id='year-slider',
            min=df['year'].min(),
            max=df['year'].max(),
            value=df['year'].min(),
            marks={str(year): str(year) for year in df['year'].unique()},
            step=None,
            className="slider"
        ),
    ], className="row slider-container container"),
    
    html.Div([
        dcc.Graph(id='scatter-plot', className="scatter-plot")
    ], className="row container")
], className="container")

# Callback to update the scatter plot
@app.callback(
    Output('scatter-plot', 'figure'),
    [Input('dropdown-x', 'value'),
     Input('dropdown-y', 'value'),
     Input('year-slider', 'value')]
)
def update_graph(selected_x, selected_y, selected_year):
    filtered_df = df[df['year'] == selected_year]
    fig = px.scatter(
        filtered_df,
        x=selected_x,
        y=selected_y,
        title=f'Scatter Plot of {selected_x} vs {selected_y} for Year {selected_year}',
        template='plotly_dark'
    )
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
