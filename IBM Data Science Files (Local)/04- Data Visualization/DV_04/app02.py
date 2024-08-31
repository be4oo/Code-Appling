
# Import packages
from dash import Dash, html, dash_table, dcc  # dcc stands for Dash Core Components
import pandas as pd
import plotly.express as px

# Incorporate data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# Initialize the app
app = Dash()

# App layout
app.layout = [
    html.Div(children='My First App with Data and a Graph'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10),
    dcc.Graph(figure=px.histogram(df, x='continent', y='lifeExp', histfunc='avg', title='Life Expectancy Across Continents'))
]

# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=8052)
