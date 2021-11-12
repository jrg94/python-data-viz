import pandas as pd
import plotly.express as px
import dash
from dash import html
from dash import dcc

df = pd.read_csv("https://raw.githubusercontent.com/curran/data/gh-pages/plotlyExamples/2014_apple_stock.csv")
fig = px.line(df, x="AAPL_x", y="AAPL_y", width=1200, height=628)

app = dash.Dash()
app.layout = html.Div(children=[
  html.H1(children='My Dashboard'),
  html.Div(children='A practice visualization dashboard.'),
  dcc.Graph(figure=fig)
])

if __name__ == '__main__':
  app.run_server(debug=True)
