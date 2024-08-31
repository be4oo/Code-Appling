import dash
from dash import dcc, html, callback, Input, Output
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
app = dash.Dash(__name__)

# Layout of the app
app.layout = html.Div([
    html.H1("Dashboard Title"),
    html.P("This is a short description of the dashboard."),
    
    html.Label("Select Feature X:"),
    dcc.Dropdown(
        id='dropdown-x',
        options=[
            {'label': 'Feature X', 'value': 'feature_x'},
            {'label': 'Feature Y', 'value': 'feature_y'},
            {'label': 'Feature Z', 'value': 'feature_z'}
        ],
        value='feature_x'
    ),
    
    html.Label("Select Feature Y:"),
    dcc.Dropdown(
        id='dropdown-y',
        options=[
            {'label': 'Feature X', 'value': 'feature_x'},
            {'label': 'Feature Y', 'value': 'feature_y'},
            {'label': 'Feature Z', 'value': 'feature_z'}
        ],
        value='feature_y'
    ),
    
    html.Label("Select Year:"),
    dcc.Slider(
        id='year-slider',
        min=df['year'].min(),
        max=df['year'].max(),
        value=df['year'].min(),
        marks={str(year): str(year) for year in df['year'].unique()},
        step=None
    ),
    
    dcc.Graph(id='scatter-plot')
])

# Callback to update the scatter plot
@callback(
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
        title=f'Scatter Plot of {selected_x} vs {selected_y} for Year {selected_year}'
    )
    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
