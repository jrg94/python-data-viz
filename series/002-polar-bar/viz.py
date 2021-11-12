import pandas as pd
import plotly.graph_objects as go
import dash
from dash import html
from dash import dcc

THEMES_DOMAINS = {
    "Adaptability": "Relationship Building",
    "Connectedness": "Relationship Building",
    "Developer": "Relationship Building",
    "Empathy": "Relationship Building",
    "Harmony": "Relationship Building",
    "Includer": "Relationship Building",
    "Individualization": "Relationship Building",
    "Positivity": "Relationship Building",
    "Relator": "Relationship Building",
    "Activator": "Influencing",
    "Command": "Influencing",
    "Communication": "Influencing",
    "Competition": "Influencing",
    "Maximizer": "Influencing",
    "Self-Assurance": "Influencing",
    "Significance": "Influencing",
    "Woo": "Influencing",
    "Analytical": "Strategic Thinking",
    "Context": "Strategic Thinking",
    "Futuristic": "Strategic Thinking",
    "Ideation": "Strategic Thinking",
    "Input": "Strategic Thinking",
    "Intellection": "Strategic Thinking",
    "Learner": "Strategic Thinking",
    "Strategic": "Strategic Thinking",
    "Achiever": "Executing",
    "Arranger": "Executing",
    "Belief": "Executing",
    "Consistency": "Executing",
    "Deliberative": "Executing",
    "Discipline": "Executing",
    "Focus": "Executing",
    "Responsibility": "Executing",
    "Restorative": "Executing",
}

DOMAIN_COLOR = {
    "Strategic Thinking": "green",
    "Relationship Building": "blue",
    "Influencing": "orange",
    "Executing": "purple"
}

DOMAINS_THEMES = dict()
for key, value in THEMES_DOMAINS.items():
    DOMAINS_THEMES.setdefault(value, list()).append(key)


def plot_domain(fig, counts: pd.Series, domain: str):
    """
    Plots a single domain on the starburst plot.

    :param fig: The starburst plot
    :param counts: The counts of each theme in a domain
    :param domain: The domain to plot
    """
    domain_data = counts[counts.index.isin(DOMAINS_THEMES[domain])]
    fig.add_trace(go.Barpolar(
        r=domain_data.values,
        theta=domain_data.index,
        width=[1] * len(domain_data),
        marker_color=DOMAIN_COLOR[domain],
        marker_line_color="black",
        marker_line_width=2,
        opacity=0.8,
        name=domain
    ))


def plot_starburst(df: pd.DataFrame, title: str):
    """
    Creates a complete polar bar chart from the CliftonStrengths data.

    :param df: The dataframe containing the CliftonStrengths data
    :param title: The title of the plot
    """
    fig = go.Figure()
    counts = df["Theme"].value_counts()
    for domain in DOMAIN_COLOR.keys():
        plot_domain(fig, counts, domain)
    fig.update_traces(showlegend=True)
    fig.update_layout(
        title={
            'text': title,
            'y': .99
        },
        width=1000,
        height=800,
        template=None,
        legend_title="CliftonStrengths Domain",
        polar=dict(
            radialaxis=dict(range=[0, max(counts.values)], showticklabels=False, ticks="", nticks=int(
                max(counts.values))+1, showline=False),
            angularaxis=dict(categoryarray=list(
                THEMES_DOMAINS.keys()), nticks=0, tickfont=dict(size=12), ticklen=10)
        )
    )
    return fig


df = pd.read_csv("series/002-polar-bar/themes.csv")
fig = plot_starburst(df, "CliftonStrengths Starburst")

app = dash.Dash()
app.layout = html.Div(children=[
    html.H1(children='CliftonStrengths Visualization'),
    html.Div(children='A polar bar visualization dashboard.'),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)
