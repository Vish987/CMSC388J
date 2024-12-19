import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from flask import Markup

def generate_pie_charts(budgets):
    if not budgets:
        return None, None

    categories = [budget.category for budget in budgets]
    total_amounts = [budget.amount for budget in budgets]
    remaining_amounts = [budget.remaining_budget() for budget in budgets]
    used_amounts = [budget.amount - budget.remaining_budget() for budget in budgets]

    pie1 = go.Figure(
        go.Pie(
            labels=categories,
            values=total_amounts,
            textinfo='label+percent',
            hoverinfo='label+value',
            title="Budget Distribution by Category",
            titlefont=dict(size=20, weight='bold'),
            textfont=dict(size=15),
            showlegend=True,
            marker=dict(colors=px.colors.sequential.Sunset[:len(categories)]),
            titleposition='top center'
        )
    )

    used_labels = [f"{category} Used" for category in categories]
    unused_labels = [f"{category} Unused" for category in categories]
    used_and_unused_values = used_amounts + remaining_amounts
    used_and_unused_labels = used_labels + unused_labels

    pie2 = go.Figure(
        go.Pie(
            labels=used_and_unused_labels,
            values=used_and_unused_values,
            textinfo='label+percent',
            hoverinfo='label+value',
            title="Budget Overview by Category",
            titlefont=dict(size=20, weight='bold'),
            textfont=dict(size=15),
            showlegend=True,
            marker=dict(colors=px.colors.sequential.Sunset[:len(categories)]),
            titleposition='top center',
            textposition='inside'
        )
    )

    pie1.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white')
    )

    pie2.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white')
    )

    return Markup(pie1.to_html(full_html=False, include_plotlyjs=False, div_id='pie1')), Markup(pie2.to_html(full_html=False, include_plotlyjs=False, div_id='pie2'))