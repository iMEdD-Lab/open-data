# -*- coding: utf-8 -*-

import requests
import datetime

import pandas as pd

import plotly.express as px
import plotly.graph_objects as go

TICKFONT = dict(
    family='Roboto',
    size=12,
    color='#114B5F'
)

TEXTFONT = dict(
    family='Roboto',
    size=16,
    color='#114B5F'
)

XAXIS = dict(
    showline=True,
    zeroline=True,
    showgrid=False,
    showticklabels=True,
    linecolor='#114B5F',
    linewidth=.1,
    ticks='outside',
    tickcolor='#BBBBBB',
    gridcolor='#F8FAFA',
    tickfont=TICKFONT
)

YAXIS = dict(
    showgrid=True,
    gridcolor='#F8FAFA',
    zeroline=False,
    showline=True,
    showticklabels=True,
    linecolor='#114B5F',
    linewidth=.1,
    ticks='outside',
    tickcolor='#BBBBBB',
    tickfont=TICKFONT
)


def parseFloat(x):
    try:
        x = x.replace(',', '')
        return float(x)
    except ValueError:
        return None


def create_scatterplot_casesVStests_logx(name, wom_data, countries_data, show=False):
    wom = wom_data
    wom = wom.rename(columns={wom.columns[8]: 'Total Cases/1M pop'})

    countries_names = countries_data
    countries_names = countries_names.rename(columns={'ADMIN': 'Country,Other'})
    wom = pd.merge(wom, countries_names, on='Country,Other', how='left')

    wom['Total Cases/1M pop'] = (wom['Total Cases/1M pop']).apply(lambda x: parseFloat(x))
    wom['Deaths/1M pop'] = (wom['Deaths/1M pop']).apply(lambda x: parseFloat(x))
    wom['Tests/ 1M pop'] = (wom['Tests/ 1M pop']).apply(lambda x: parseFloat(x))
    
    wom = wom.fillna(0)

    wom['testing_median_diff_pct'] = ((wom['Tests/ 1M pop']-wom['Tests/ 1M pop'].median())/wom['Tests/ 1M pop'].median())*100
    wom['cases_rate_normalized'] = (wom['Total Cases/1M pop']*100)/wom['Tests/ 1M pop']
    wom['cases_rate_median_diff_pct'] = ((wom['cases_rate_normalized']-wom['cases_rate_normalized'].median())/wom['cases_rate_normalized'].median())*100

    wom = wom[wom['Deaths/1M pop'] > 0]

    def text(row):
        if row['Country,Other'] == 'Greece':
            return (row['ADMIN_GR'])
        else:
            return ''

    texts = [text(row) for index, row in wom.iterrows()]

    fig = px.scatter(
        wom,
        x=wom['Tests/ 1M pop'],
        y=wom['Total Cases/1M pop'],
        size=wom['Deaths/1M pop']+150,
        hover_name='ADMIN_GR',
        color=(wom['Deaths/1M pop']),
        color_continuous_scale=[('#3f6678'), ('#BA3A0A')],
        range_color=[
            wom['Deaths/1M pop'].min(),
            wom['Deaths/1M pop'].max()
        ],
        opacity=.9,
        log_y=True,
        log_x=True,
        text=texts,
        labels={
            'Deaths/1M pop': 'Θάνατοι/1M πληθυσμού',
            'Tests/ 1M pop': 'Τεστ/1M πληθυσμού',
            'Total Cases/1M pop': 'Κρούσματα/1M πληθυσμού',
            'size': '',
            'text': ''
        }
    )

    fig.update_traces(textposition='middle right', textfont=TEXTFONT)

    fig.update_layout(
        xaxis=XAXIS,
        yaxis=YAXIS,
        showlegend=True,
        paper_bgcolor='#E6ECEC',
        plot_bgcolor='#E6ECEC',
        title=dict(
            text='<br>Κρούσματα και Τεστ ανά 1 εκατ. πληθυσμού<br>',
            font=TEXTFONT
        ),
        xaxis_title=dict(
            text='Τεστ/1 εκατ. πληθυσμού',
            font=TICKFONT
        ),
        yaxis_title=dict(
            text='Κρούσματα/1 εκατ. πληθυσμού',
            font=TICKFONT
        ),
        hoverlabel=dict(
            font_size=10,
            font_family='Roboto'
        ),
        hovermode='closest',
        annotations=[dict(
            x=0,
            y=-.2,
            xref='paper',
            yref='paper',
            text='Πηγή δεδομένων: <a href="https://www.worldometers.info/coronavirus/">Worldometer</a>',
            showarrow=False,
            visible=True,
            font=dict(
                family='Roboto',
                color='#114B5F',
                size=10
            )
        )]
    )

    fig.update_layout(coloraxis_colorbar=dict(
            nticks=3,
            tickmode='array',
            tick0=wom['Deaths/1M pop'].min(),
            tickvals=[
                wom['Deaths/1M pop'].min(), wom['Deaths/1M pop'].max() / 2, 
                wom['Deaths/1M pop'].max()
            ],
            ticktext=[
                wom['Deaths/1M pop'].min(), wom['Deaths/1M pop'].max() / 2, 
                wom['Deaths/1M pop'].max()
            ]
        )
    )
    if show:
        config = dict(
            {
                'displayModeBar': True,
                'scrollZoom': False,
                'displaylogo': False,
                'responsive': True,
                'staticPlot': False
            }
        )
        fig.show(config=config)
    fig.write_json(name + '.json')


def create_scatterplot_casesVStests_logy(name, wom_data, countries_data, show = False):
    wom = wom_data
    wom = wom.rename(columns={wom.columns[8]: 'Total Cases/1M pop'})

    countries_names = countries_data
    countries_names = countries_names.rename(columns={'ADMIN': 'Country,Other'})
    wom = pd.merge(wom, countries_names, on='Country,Other', how='left')

    wom['Total Cases/1M pop'] = (wom['Total Cases/1M pop']).apply(lambda x: parseFloat(x))
    wom['Deaths/1M pop'] = (wom['Deaths/1M pop']).apply(lambda x: parseFloat(x))
    wom['Tests/ 1M pop'] = (wom['Tests/ 1M pop']).apply(lambda x: parseFloat(x))
    
    wom = wom.fillna(0)
    
    wom['testing_median_diff_pct'] = ((wom['Tests/ 1M pop']-wom['Tests/ 1M pop'].median())/wom['Tests/ 1M pop'].median())*100
    wom['cases_rate_normalized'] = (wom['Total Cases/1M pop']*100)/wom['Tests/ 1M pop']
    wom['cases_rate_median_diff_pct'] = ((wom['cases_rate_normalized']-wom['cases_rate_normalized'].median())/wom['cases_rate_normalized'].median())*100

    wom = wom[wom['Deaths/1M pop'] > 0]

    def info(row):
        if (row['testing_median_diff_pct'] > 3000) & (row['cases_rate_median_diff_pct'] < 0):
            return (row['ADMIN_GR'])
        elif row['Country,Other'] == 'Greece':
            return (row['ADMIN_GR'])
        elif row['Deaths/1M pop'] == wom['Deaths/1M pop'].max():
            return (row['ADMIN_GR'])
        else:
            return ''

    texts = [info(row) for index, row in wom.iterrows()]

    fig = px.scatter(
        wom, 
        x=wom['Tests/ 1M pop'], 
        y=wom['Total Cases/1M pop'],
        size=wom['Deaths/1M pop']+150,
        hover_name='ADMIN_GR', 
        color=(wom['Deaths/1M pop']),
        color_continuous_scale=[('#3f6678'), ('#BA3A0A')],
        range_color=[
            wom['Deaths/1M pop'].min(),
            wom['Deaths/1M pop'].max()
        ],
        opacity=.9, log_y=True, log_x=False,
        text=texts,
        labels={
            'Deaths/1M pop': 'Θάνατοι/1M πληθυσμού',
            'Tests/ 1M pop': 'Τεστ/1M πληθυσμού',
            'Total Cases/1M pop': 'Κρούσματα/1M πληθυσμού',
            'size': '',
            'text': ''
        }
    )
    
    fig.update_traces(textposition='bottom center', textfont=TEXTFONT)

    fig.update_layout(
        xaxis=XAXIS,
        yaxis=YAXIS,
        showlegend=True,
        paper_bgcolor='#E6ECEC',
        plot_bgcolor='#E6ECEC',
        title=dict(
            text='<br>Κρούσματα και Τεστ ανά 1 εκατ. πληθυσμού<br>',
            font=TEXTFONT
        ),
        xaxis_title=dict(
            text='Τεστ/1 εκατ. πληθυσμού',
            font=TICKFONT
        ),
        yaxis_title=dict(
            text='Κρούσματα/1 εκατ. πληθυσμού',
            font=TICKFONT
        ),
        hoverlabel=dict(
            font_size=10,
            font_family='Roboto'
        ),
        hovermode='closest',
        annotations=[dict(
            x=0,
            y=-.2,
            xref='paper',
            yref='paper',
            text='Πηγή δεδομένων: <a href="https://www.worldometers.info/coronavirus/">Worldometer</a>',
            showarrow=False,
            visible=True,
            font=dict(
                family='Roboto',
                color='#114B5F',
                size=10
            )
        )]
    )

    fig.update_layout(coloraxis_colorbar=dict(
            nticks=3,
            tickmode='array',
            tick0=wom['Deaths/1M pop'].min(),
            tickvals=[
                wom['Deaths/1M pop'].min(), wom['Deaths/1M pop'].max() / 2,
                wom['Deaths/1M pop'].max()
            ],
            ticktext=[
                wom['Deaths/1M pop'].min(), wom['Deaths/1M pop'].max() / 2,
                wom['Deaths/1M pop'].max()
            ]
        )
    )
    
    if show:
        config = dict(
            {
                'displayModeBar': True,
                'scrollZoom': False,
                'displaylogo': False,
                'responsive': True,
                'staticPlot': False
            }
        )
        fig.show(config=config)

    fig.write_json(name + '.json')


def create_linechart_deaths_intubated_gr(name, greeceTimeline_data, show = False):
    df = greeceTimeline_data
    df = df.drop('Province/State', axis=1)
    df = df.drop('Country/Region', axis=1)
    df = df.set_index('Status')
    df = df.T
    df = df.reset_index()
    df = df.rename(columns={'index':'date'})
    df['date']= pd.to_datetime(df['date'])
    df['date']= pd.to_datetime(df['date'] , format='%b-%d-%y').dt.strftime('%d-%b')
    df['date_gr'] = df['date']
    df['date_gr'] = df['date_gr'].astype(str)
    df['date_gr'] = df['date_gr'].str.replace('Feb','Φεβ')
    df['date_gr'] = df['date_gr'].str.replace('Mar','Μαρ')
    df['date_gr'] = df['date_gr'].str.replace('Apr','Απρ')
    df['date_gr'] = df['date_gr'].str.replace('May','Μάι')
    
    # Initialize figure
    fig = go.Figure() 

    # Add Traces
    fig.add_trace(
        go.Scatter(
            x=df.date_gr, 
            y=df.deaths,
            mode='lines+markers',
            connectgaps=True,
            marker_color='#BA3A0A',
            name='θάνατοι',
            line_shape='spline'
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df.date_gr, 
            y=df.intubated,
            mode='lines+markers',
            connectgaps=True,
            marker_color='#3f6678',
            name='διασωληνωμένοι',
            line_shape='spline'
        )
    )

    # Add buttons
    fig.update_layout(
        updatemenus=[
            dict(
                type='buttons',
                direction='right',
                active=0,
                x=0.6,
                y=1,
                buttons=list(
                    [
                        dict(
                            label='ΟΛΑ',
                            method='update',
                            args=[
                                { 'visible': [True, True] },
                                { 'title': 'Θάνατοι και διασωληνωμένοι ασθενείς ανά ημέρα στην Ελλάδα'}
                            ]
                        ),
                        dict(
                            label='Θάνατοι',
                             method='update',
                             args=[
                                    {'visible': [True, False]},
                                    {'title': 'Θάνατοι ανά ημέρα στην Ελλάδα'}
                             ]
                        ),
                        dict(
                            label='Διασωληνωμένοι',
                             method='update',
                             args=[
                                {'visible': [False, True]},
                                {'title': 'Διασωληνωμένοι ασθενείς ανά ημέρα στην Ελλάδα'}
                             ]
                        )
                    ]
                )
            )
        ]
    )

    fig.update_layout(
        xaxis=dict(
            showline=True,
            zeroline=True,
            showgrid=False,
            showticklabels=True,
            linecolor='#114B5F',
            linewidth=.1,
            ticks='outside',
            tickcolor='#BBBBBB',
            gridcolor='#F8FAFA',
            tickfont=dict(
                family='Roboto',
                size=12,
                color='#114B5F',
            ),
            dtick = 5
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor='#F8FAFA',
            zeroline=False,
            showline=True,
            showticklabels=True,
            linecolor='#114B5F',
            linewidth=.1,
            ticks='outside',
            tickcolor='#BBBBBB',
            tickfont=dict(
                family='Roboto',
                size=12,
                color='#114B5F'
            ),
        ),
        showlegend=True,
        legend=dict(
                font=dict(
                family='Roboto',
                size=12,
                color='#114B5F'
            )
        ),
        paper_bgcolor='#E6ECEC',
        plot_bgcolor='#E6ECEC',
        title=dict(
                text='<br>Θάνατοι και διασωληνωμένοι ασθενείς ανά ημέρα στην Ελλάδα<br>',
                font=dict(
                family='Roboto',
                size=16,
                color='#114B5F'
            )
        ),

        hoverlabel=dict(
            font_size=10,
            font_family='Roboto'
        ),

        hovermode='closest'
    )
    
    if show:
        config = dict(
            {
                'displayModeBar': True, 
                'scrollZoom': False,
                'displaylogo': False,
                'responsive': True,
                'staticPlot': False
            }
        )
        fig.show(config=config)
    fig.write_json(name + '.json')
