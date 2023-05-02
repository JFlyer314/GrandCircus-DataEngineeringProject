# -*- coding: utf-8 -*-
"""Animated Top 5 Max Salary

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZdBkX1AFKDdjvrQ5rU7im54uZ2YHaS2K
"""

import pandas as pd
import plotly.graph_objs as go

df = pd.read_csv('Combined_Version_3.csv')

state_keywords = {
    'AL': 'Alabama', 'AK': 'Alaska', 'AZ': 'Arizona', 'AR': 'Arkansas', 'CA': 'California',
    'CO': 'Colorado', 'CT': 'Connecticut', 'DE': 'Delaware', 'FL': 'Florida', 'GA': 'Georgia',
    'HI': 'Hawaii', 'ID': 'Idaho', 'IL': 'Illinois', 'IN': 'Indiana', 'IA': 'Iowa',
    'KS': 'Kansas', 'KY': 'Kentucky', 'LA': 'Louisiana', 'ME': 'Maine', 'MD': 'Maryland',
    'MA': 'Massachusetts', 'MI': 'Michigan', 'MN': 'Minnesota', 'MS': 'Mississippi', 'MO': 'Missouri',
    'MT': 'Montana', 'NE': 'Nebraska', 'NV': 'Nevada', 'NH': 'New Hampshire', 'NJ': 'New Jersey',
    'NM': 'New Mexico', 'NY': 'New York', 'NC': 'North Carolina', 'ND': 'North Dakota', 'OH': 'Ohio',
    'OK': 'Oklahoma', 'OR': 'Oregon', 'PA': 'Pennsylvania', 'RI': 'Rhode Island', 'SC': 'South Carolina',
    'SD': 'South Dakota', 'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah', 'VT': 'Vermont',
    'VA': 'Virginia', 'WA': 'Washington', 'WV': 'West Virginia', 'WI': 'Wisconsin', 'WY': 'Wyoming', 'DC': 'Washington DC'
}

state_salary = df.groupby('State Code')['Yearly Max'].max()
top_states = state_salary.sort_values(ascending=False)[:5]
state_names = [state_keywords[state_code] for state_code in top_states.index]

frames = []  #establishes the frame of the graph during the animation
for i in range(1, len(top_states) + 1):
    frame = go.Frame(
        data=[go.Bar(
            x=state_names[:i+1],
            y=top_states[:i+1],
            marker_color='rgb(158, 202, 225)',
        )],
        layout=go.Layout(
            xaxis_title='State',
            yaxis_title='Yearly Max Salary ($)',
            title='Top 5 States by Yearly Max Salary'
        )
    )
    frames.append(frame)

fig = go.Figure(
    data=[go.Bar(
        x=state_names,
        y=top_states,
        marker_color='rgb(158, 202, 225)',
    )],
    frames=frames
)



fig.update_layout(
    xaxis_title='State',
    yaxis_title='Yearly Max Salary ($)',
    title='Top 5 States by Yearly Max Salary',
    updatemenus=[  #start of the play button and animation
        dict(
            type='buttons',
            buttons=[
                dict(
                    label='Play',
                    method='animate',
                    args=[None, {'frame': {'duration': 500, 'redraw': True}, 'fromcurrent': True}]
                ),
                dict(
                    label='Pause',
                    method='animate',
                    args=[[None], {'frame': {'duration': 0, 'redraw': True}, 'mode': 'immediate'}]
                )
            ],
            showactive=False,
            x=1,
            y=1.5,
            pad=dict(t=30, r=10),
        )
    ]
)