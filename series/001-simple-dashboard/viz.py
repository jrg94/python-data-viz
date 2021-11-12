import dash
from dash import html
from dash import dcc
import pandas as pd
import plotly.express as px

df = pd.read_csv("https://raw.githubusercontent.com/curran/data/gh-pages/plotlyExamples/2014_apple_stock.csv")
fig = px.line(df, x="AAPL_x", y="AAPL_y")

app = dash.Dash()
app.layout = html.Div(children=[
  html.H1(children='My Dashboard'),
  html.Div(children='A practice visualization dashboard.'),
  dcc.Graph(figure=fig)
])

if __name__ == '__main__':
  app.run_server(debug=True)
