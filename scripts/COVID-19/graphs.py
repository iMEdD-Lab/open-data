# -*- coding: utf-8 -*-

import requests
import datetime

import pandas as pd

import plotly.express as px
import plotly.graph_objects as go

import labels

baseHopkinsURL = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/"

TICKFONT = dict(family="Roboto", size=12, color="#114B5F")

TEXTFONT = dict(family="Roboto", size=16, color="#114B5F")

XAXIS = dict(
    showline=True,
    zeroline=True,
    showgrid=False,
    showticklabels=True,
    linecolor="#114B5F",
    linewidth=0.1,
    ticks="outside",
    tickcolor="#BBBBBB",
    gridcolor="#F8FAFA",
    tickfont=TICKFONT,
)

YAXIS = dict(
    showgrid=True,
    gridcolor="#F8FAFA",
    zeroline=False,
    showline=True,
    showticklabels=True,
    linecolor="#114B5F",
    linewidth=0.1,
    ticks="outside",
    tickcolor="#BBBBBB",
    tickfont=TICKFONT,
)

TICKFONT_STYLE = dict(family="Roboto", size=8, color="#114B5F")

TEXTFONT = dict(family="Roboto", size=16, color="#114B5F")

XAXIS_STYLE = dict(
    showline=True,
    zeroline=False,
    showgrid=True,
    showticklabels=True,
    linecolor="#114B5F",
    linewidth=0.1,
    ticks="outside",
    tickcolor="#BBBBBB",
    gridcolor="#F8FAFA",
    tickfont=TICKFONT_STYLE,
)

YAXIS_STYLE = dict(
    showgrid=True,
    gridcolor="#F8FAFA",
    zeroline=False,
    showline=True,
    showticklabels=True,
    linecolor="#114B5F",
    linewidth=0.1,
    ticks="outside",
    tickcolor="#BBBBBB",
    tickfont=TICKFONT_STYLE,
)

YAXIS_STYLE2 = dict(
    showgrid=True,
    gridcolor="#F8FAFA",
    zeroline=False,
    showline=False,
    showticklabels=False,
    linecolor="#114B5F",
    linewidth=0.1,
    tickcolor="#BBBBBB",
    tickfont=TICKFONT_STYLE,
)


def parseFloat(x):
    try:
        x = x if isinstance(x, str) else x.to_string()
        x = x.replace(",", "")
        return float(x)
    except ValueError:
        return None


def create_scatterplot_casesVStests_logx(
    name, wom_data, countries_data, show=False, lang="EL"
):
    wom = wom_data

    countries_names = countries_data
    countries_names = countries_names.rename(columns={"ADMIN": "Country,Other"})
    wom = pd.merge(wom, countries_names, on="Country,Other", how="left")
    
    wom["Tot Cases/1M pop"] = (wom["Tot Cases/1M pop"]).apply(lambda x: parseFloat(x))    
    wom["Deaths/1M pop"] = (wom["Deaths/1M pop"]).apply(lambda x: parseFloat(x))
    wom["Tests/ 1M pop"] = (wom["Tests/ 1M pop"]).apply(lambda x: parseFloat(x))
    
    wom["testing_median_diff_pct"] = (
        (wom["Tests/ 1M pop"] - wom["Tests/ 1M pop"].median())
        / wom["Tests/ 1M pop"].median()
    ) * 100
    wom["cases_rate_normalized"] = (wom["Tot Cases/1M pop"] * 100) / wom[
        "Tests/ 1M pop"
    ]
    wom["cases_rate_normalized"] = wom["cases_rate_normalized"].round(2)
    wom["cases_rate_median_diff_pct"] = (
        (wom["cases_rate_normalized"] - wom["cases_rate_normalized"].median())
        / wom["cases_rate_normalized"].median()
    ) * 100

    wom = wom[(wom['Country,Other'] != 'Sudan') & (wom['Country,Other'] != 'Yemen') & (wom['Country,Other'] != 'Burundi')]
    wom = wom[wom["Deaths/1M pop"] > 0]

    def text(row):
        if lang == "EL":
            if row["Country,Other"] == "Greece":
                return row["ADMIN_GR"]
            else:
                return ""
        else:
            if row["Country,Other"] == "Greece":
                return row["Country,Other"]
            else:
                return ""

    texts = [text(row) for index, row in wom.iterrows()]

    fig = px.scatter(
        wom,
        x=wom["Tests/ 1M pop"],
        y=wom["Tot Cases/1M pop"],
        size=wom["Deaths/1M pop"] + 150,
        hover_name=labels.scatter_country(lang),
        color=(wom["Deaths/1M pop"]),
        color_continuous_scale=[("#3f6678"), ("#BA3A0A")],
        range_color=[wom["Deaths/1M pop"].min(), wom["Deaths/1M pop"].max()],
        opacity=0.9,
        log_y=True,
        log_x=True,
        text=texts,
        labels=labels.scatter_labels(lang),
    )

    fig.update_traces(textposition="middle right", textfont=TEXTFONT)

    fig.update_layout(
        xaxis=XAXIS,
        yaxis=YAXIS,
        showlegend=True,
        paper_bgcolor="#E6ECEC",
        plot_bgcolor="#E6ECEC",
        title=dict(text=labels.scatter_title(lang), font=TEXTFONT,),
        xaxis_title=dict(text=labels.scatter_xaxis_title(lang), font=TICKFONT),
        yaxis_title=dict(text=labels.scatter_yaxis_title(lang), font=TICKFONT),
        hoverlabel=dict(font_size=10, font_family="Roboto"),
        hovermode="closest",
    )

    fig.update_layout(
        coloraxis_colorbar=dict(
            nticks=3,
            tickmode="array",
            tick0=wom["Deaths/1M pop"].min(),
            tickvals=[
                wom["Deaths/1M pop"].min(),
                wom["Deaths/1M pop"].max() / 2,
                wom["Deaths/1M pop"].max(),
            ],
            ticktext=[
                wom["Deaths/1M pop"].min(),
                wom["Deaths/1M pop"].max() / 2,
                wom["Deaths/1M pop"].max(),
            ],
        )
    )

    fig.update_layout(height=450, margin=dict(l=30, r=10, b=10, t=80, pad=0))

    if show:
        config = dict(
            {
                "displayModeBar": True,
                "scrollZoom": False,
                "displaylogo": False,
                "responsive": True,
                "staticPlot": False,
            }
        )
        fig.show(config=config)
    
    if lang == 'EL':
        fig.write_json(name + ".json")
    fig.write_json(name + "_" + lang + ".json")


def create_scatterplot_casesVStests_logy(
    name, wom_data, countries_data, show=False, lang="EL"
):
    wom = wom_data

    countries_names = countries_data
    countries_names = countries_names.rename(columns={"ADMIN": "Country,Other"})
    wom = pd.merge(wom, countries_names, on="Country,Other", how="left")

    wom["Tot Cases/1M pop"] = (wom["Tot Cases/1M pop"]).apply(lambda x: parseFloat(x))
    wom["Deaths/1M pop"] = (wom["Deaths/1M pop"]).apply(lambda x: parseFloat(x))
    wom["Tests/ 1M pop"] = (wom["Tests/ 1M pop"]).apply(lambda x: parseFloat(x))

    wom["testing_median_diff_pct"] = (
        (wom["Tests/ 1M pop"] - wom["Tests/ 1M pop"].median())
        / wom["Tests/ 1M pop"].median()
    ) * 100
    wom["cases_rate_normalized"] = (wom["Tot Cases/1M pop"] * 100) / wom[
        "Tests/ 1M pop"
    ]
    wom["cases_rate_median_diff_pct"] = (
        (wom["cases_rate_normalized"] - wom["cases_rate_normalized"].median())
        / wom["cases_rate_normalized"].median()
    ) * 100

    wom = wom[wom["Deaths/1M pop"] > 0]

    def info(row):
        if (row["testing_median_diff_pct"] > 3000) & (
            row["cases_rate_median_diff_pct"] < 0
        ):
            return row["ADMIN_GR"]
        elif row["Country,Other"] == "Greece":
            return row["ADMIN_GR"]
        elif row["Deaths/1M pop"] == wom["Deaths/1M pop"].max():
            return row["ADMIN_GR"]
        else:
            return ""

    texts = [info(row) for index, row in wom.iterrows()]

    fig = px.scatter(
        wom,
        x=wom["Tests/ 1M pop"],
        y=wom["Tot Cases/1M pop"],
        size=wom["Deaths/1M pop"] + 150,
        hover_name="ADMIN_GR",
        color=(wom["Deaths/1M pop"]),
        color_continuous_scale=[("#3f6678"), ("#BA3A0A")],
        range_color=[wom["Deaths/1M pop"].min(), wom["Deaths/1M pop"].max()],
        opacity=0.9,
        log_y=True,
        log_x=False,
        text=texts,
        labels={
            "Deaths/1M pop": "Θάνατοι/1M πληθυσμού",
            "Tests/ 1M pop": "Τεστ/1M πληθυσμού",
            "Tot Cases/1M pop": "Κρούσματα/1M πληθυσμού",
            "size": "",
            "text": "",
        },
    )

    fig.update_traces(textposition="bottom center", textfont=TEXTFONT)

    fig.update_layout(
        xaxis=XAXIS,
        yaxis=YAXIS,
        showlegend=True,
        paper_bgcolor="#E6ECEC",
        plot_bgcolor="#E6ECEC",
        title=dict(
            text="<br><b>Κρούσματα</b> και Τεστ ανά 1 εκατ. πληθυσμού<br>",
            font=TEXTFONT,
        ),
        xaxis_title=dict(text="Τεστ/1 εκατ. πληθυσμού", font=TICKFONT),
        yaxis_title=dict(text="Κρούσματα/1 εκατ. πληθυσμού", font=TICKFONT),
        hoverlabel=dict(font_size=10, font_family="Roboto"),
        hovermode="closest",
        annotations=[
            dict(
                x=0,
                y=-0.2,
                xref="paper",
                yref="paper",
                text='<br> Πηγή δεδομένων: <a href="https://www.worldometers.info/coronavirus/">Worldometer</a>',
                showarrow=False,
                visible=True,
                align="left",
                font=dict(family="Roboto", color="#114B5F", size=10),
            )
        ],
    )

    fig.update_layout(
        coloraxis_colorbar=dict(
            nticks=3,
            tickmode="array",
            tick0=wom["Deaths/1M pop"].min(),
            tickvals=[
                wom["Deaths/1M pop"].min(),
                wom["Deaths/1M pop"].max() / 2,
                wom["Deaths/1M pop"].max(),
            ],
            ticktext=[
                wom["Deaths/1M pop"].min(),
                wom["Deaths/1M pop"].max() / 2,
                wom["Deaths/1M pop"].max(),
            ],
        )
    )

    fig.update_layout(height=450, margin=dict(l=10, r=10, b=10, t=80, pad=0))

    if show:
        config = dict(
            {
                "displayModeBar": True,
                "scrollZoom": False,
                "displaylogo": False,
                "responsive": True,
                "staticPlot": False,
            }
        )
        fig.show(config=config)
    if lang == 'EL':
        fig.write_json(name + ".json")
    fig.write_json(name + "_" + lang + ".json")


def create_linechart_deaths_intubated_gr(
    name, greeceTimeline_data, show=False, lang="EL"
):
    df = greeceTimeline_data
    df = df.drop("Province/State", axis=1)
    df = df.drop("Country/Region", axis=1)
    df = df.set_index("Status")
    df = df.T
    df = df.reset_index()
    df = df.rename(columns={"index": "date"})
    df = df[15:]
    df["date"] = pd.to_datetime(df["date"])
    df["date"] = pd.to_datetime(df["date"], format="%b-%d-%y").dt.strftime("%d-%b")
    df["date_gr"] = df["date"]
    df["date_gr"] = df["date_gr"].astype(str)
    df["date_gr"] = df["date_gr"].str.replace("Feb", "Φεβ")
    df["date_gr"] = df["date_gr"].str.replace("Mar", "Μαρ")
    df["date_gr"] = df["date_gr"].str.replace("Apr", "Απρ")
    df["date_gr"] = df["date_gr"].str.replace("May", "Μάι")
    df["date_gr"] = df["date_gr"].str.replace("Jun", "Ιούν")
    df["date_gr"] = df["date_gr"].str.replace("Jul", "Ιούλ")
    df["date_gr"] = df["date_gr"].str.replace("Aug", "Ιούλ")

    def line_x():
        if lang == "EL":
            return df.date_gr
        else:
            return df.date

    # Initialize figure
    fig = go.Figure()

    # Add Traces
    fig.add_trace(
        go.Scatter(
            x=line_x(),
            y=df.deaths,
            mode="lines+markers",
            connectgaps=True,
            marker_color="#BA3A0A",
            name=labels.line_trace_deaths(lang),
            line_shape="spline",
        )
    )

    fig.add_trace(
        go.Scatter(
            x=line_x(),
            y=df.intubated,
            mode="lines+markers",
            connectgaps=True,
            marker_color="#3f6678",
            name=labels.line_trace_intub(lang),
            line_shape="spline",
        )
    )

    # Add buttons
    fig.update_layout(
        updatemenus=[
            dict(
                type="buttons",
                direction="left",
                active=0,
                buttons=list(
                    [
                        dict(
                            label=labels.line_button_all(lang),
                            method="update",
                            args=[
                                {"visible": [True, True]},
                                {"title": labels.line_button_all_title(lang)},
                            ],
                        ),
                        dict(
                            label=labels.line_button_deaths(lang),
                            method="update",
                            args=[
                                {"visible": [True, False]},
                                {"title": labels.line_button_deaths_title(lang)},
                            ],
                        ),
                        dict(
                            label=labels.line_button_intub(lang),
                            method="update",
                            args=[
                                {"visible": [False, True]},
                                {"title": labels.line_button_intub_title(lang)},
                            ],
                        ),
                    ]
                ),
                pad={"t": 0, "l": 0, "b": 0, "r": 0},
                showactive=True,
                x=0.05,
                xanchor="left",
                y=1.05,
                yanchor="top",
            )
        ]
    )

    fig.update_layout(
        xaxis=dict(
            showline=True,
            zeroline=True,
            showgrid=False,
            showticklabels=True,
            linecolor="#114B5F",
            linewidth=0.1,
            ticks="outside",
            tickcolor="#BBBBBB",
            gridcolor="#F8FAFA",
            tickfont=dict(family="Roboto", size=12, color="#114B5F",),
            dtick=10,
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor="#F8FAFA",
            zeroline=False,
            showline=True,
            showticklabels=True,
            linecolor="#114B5F",
            linewidth=0.1,
            ticks="outside",
            tickcolor="#BBBBBB",
            tickfont=dict(family="Roboto", size=12, color="#114B5F"),
        ),
        showlegend=False,
        legend=dict(font=dict(family="Roboto", size=12, color="#114B5F")),
        paper_bgcolor="#E6ECEC",
        plot_bgcolor="#E6ECEC",
        title=dict(
            text=labels.line_button_all_title(lang),
            font=dict(family="Roboto", size=16, color="#114B5F"),
        ),
        hoverlabel=dict(font_size=10, font_family="Roboto"),
        hovermode="closest",
    )

    fig.update_layout(height=450, margin=dict(l=10, r=10, b=10, t=90, pad=0))

    if show:
        config = dict(
            {
                "displayModeBar": True,
                "scrollZoom": False,
                "displaylogo": False,
                "responsive": True,
                "staticPlot": False,
            }
        )
        fig.show(config=config)
    if lang == 'EL':
        fig.write_json(name + ".json")
    fig.write_json(name + "_" + lang + ".json")


"""φορτώνουμε το αρχείο που επιθυμούμε, τον αριθμό σημείο έναρξης της οπτικοποίησης,
το όνομα της νέας στήλης που θα δημιουργηθεί από το melt, 
το όνομα του αρχείου που θέλουμε να σώσουμε"""


def after100Cases(
    data,
    countries_data,
    population,
    numberCompare,
    columnName,
    outputName,
    titleGraphic,
    keyWordHover,
    xAxis,
    yAxis,
    show=False,
    lang="EL",
):
    """ φορτώνουμε το πρώτο αρχείο από το Hopkins"""
    df = (
        data.drop(["Lat", "Long"], axis=1)
        .melt(
            id_vars=["Province/State", "Country/Region"],
            var_name="Date",
            value_name=columnName,
        )
        .astype({"Date": "datetime64[ns]", columnName: "Int64"}, errors="ignore")
    )

    """ φορτώνουμε το αρχείο με την αντιστοίχιση ελληνικών - αγγλικών ονομάτων χωρών"""
    gr = countries_data
    """ το συνδέουμε με το dataframe από το Hopkins ώστε να προστεθεί το ADMIN_GR"""
    df = pd.merge(df, gr, how="left", left_on="Country/Region", right_on="ADMIN")

    """ φορτώνουμε το αρχείο με τους πληθυσμούς"""
    pop = population
    """συνδέουμε το dataframe με τα ελληνικά ονόματα """
    gr = pd.merge(gr, pop, how="right", left_on="ADMIN", right_on="Country,Other")

    """Ενώνουμε το dataframe του Hopkins και εκείνο του population με βάση την στήλη με τα ελληνικά ονόματα"""
    df = pd.merge(df, gr, how="left", on="ADMIN_GR")

    """ υπολογίζουμε συγκεντρωτικά για κάθε χώρα τα κρούσματα και τους θανάτους ανά ημέρα"""
    df = (
        df.groupby(["Country/Region", "Date", "ADMIN_GR", "Population (2020)"])[
            columnName
        ]
        .sum()
        .reset_index()
    )

    """ ------------------- ΞΕΚΙΝΑ Η ΟΠΤΙΚΟΠΟΙΗΣΗ ------------------"""

    """ Φτιάχνουμε ένα variable που ΔΕΝ ΘΑ ΠΕΡΙΕΧΕΙ τις χώρες αναφοράς - που θα χρωματίσουμε με άλλο χρώμα"""
    cnt = df[
        (df["Country/Region"] != "Greece")
        & (df["Country/Region"] != "Germany")
        & (df["Country/Region"] != "Italy")
        & (df["Country/Region"] != "United Kingdom")
        & (df["Country/Region"] != "US")
        & (df["Country/Region"] != "Spain")
        & (df["Country/Region"] != "China")
    ]

    if lang == 'EL':
        fig = px.line(
            cnt[
                (cnt["Country/Region"] != "Diamond Princess")
                & (cnt[columnName] >= numberCompare)
            ],
            y=columnName,
            color="ADMIN_GR",
            hover_data=["ADMIN_GR"],
            labels={"Date": "Ημερομηνία", columnName: keyWordHover, "ADMIN_GR": "Χώρα"},
            title=titleGraphic,
            line_shape="spline",
            render_mode="svg",
            color_discrete_sequence=["rgb(189,189,189)"],
        )
    else:
        fig = px.line(
            cnt[
                (cnt["Country/Region"] != "Diamond Princess")
                & (cnt[columnName] >= numberCompare)
            ],
            y=columnName,
            color="Country/Region",
            hover_data=["Country/Region"],
            labels={"Date": "Date", columnName: keyWordHover, "Country/Region": "Country"},
            title=titleGraphic,
            line_shape="spline",
            render_mode="svg",
            color_discrete_sequence=["rgb(189,189,189)"]
        )

    fig.update_layout(
        paper_bgcolor="#E6ECEC",
        plot_bgcolor="#E6ECEC",
        font=dict(family="Roboto", size=11, color="#114B5F"),
    )

    fig.update_layout(
        hovermode="closest",
        hoverlabel=dict(bgcolor="white", font_size=12, font_family="Roboto"),
        hoverlabel_align="left",
    )

    fig.update_layout(showlegend=True)
    fig.update_layout(
        legend_title="Διπλό κλικ σε κάθε<br>χώρα για να την <br>απομονώσετε<br>" if lang == 'EL'
        else 'Double click<br>to select each<br>country',
        legend=dict(
            traceorder="reversed",
            font=dict(family="roboto", size=10, color="black"),
            bgcolor="#E6ECEC",
            bordercolor="#dadada",
            borderwidth=0.3,
        ),
    )

    fig.update_yaxes(
        nticks=4,
        showticklabels=True,
        showline=True,
        linewidth=2,
        linecolor="#114B5F",
        showgrid=True,
        gridwidth=0.1,
        gridcolor="#F8FAFA",
        title_text=yAxis,
        title_font={"size": 11, "color": "#114B5F"},
    )

    fig.update_xaxes(
        ticks=None,
        showticklabels=True,
        showline=False,
        linewidth=0.1,
        linecolor="#F8FAFA",
        showgrid=True,
        gridwidth=0.1,
        gridcolor="#F8FAFA",
        title_text=xAxis,
        title_font={"size": 11, "color": "#114B5F"},
    )

    fig.update_layout(xaxis_showgrid=True, yaxis_showgrid=True)

    fig.update_layout(yaxis_type="log")

    fig.update_layout(height=380)

    # Γερμανία
    if lang == 'EL':
        fig.add_trace(
            go.Scatter(
                y=df[
                    (df["Country/Region"] == "Germany") & (df[columnName] > numberCompare)
                ][columnName],
                name="Γερμανία",
                line=dict(color="black", width=2),
                hovertemplate="<b>{}</b> στην Γερμανία<extra></extra>".format(
                    "%{y:.f} " + keyWordHover 
                ),
            )
        )
    
    else:
        fig.add_trace(
        go.Scatter(
            y=df[
                (df["Country/Region"] == "Germany") & (df[columnName] > numberCompare)
            ][columnName],
            name="Germany",
            line=dict(color="black", width=2),
            hovertemplate="<b>{}</b> in Germany <extra></extra>".format(
                "%{y:.f} " + keyWordHover 
            ),
        )
    )

    # Ιταλία
    if lang == 'EL':
        fig.add_trace(
            go.Scatter(
                y=df[(df["Country/Region"] == "Italy") & (df[columnName] > numberCompare)][
                    columnName
                ],
                name="Ιταλία",
                line=dict(color="#3E82B3", width=2),
                hovertemplate="<b>{}</b> στην Ιταλία<extra></extra>".format(
                    "%{y:.f} " + keyWordHover
                ),
            )
        )
    
    else:
        fig.add_trace(
        go.Scatter(
            y=df[(df["Country/Region"] == "Italy") & (df[columnName] > numberCompare)][
                columnName
            ],
            name="Italy",
            line=dict(color="#3E82B3", width=2),
            hovertemplate="<b>{}</b> in Italy <extra></extra>".format(
                "%{y:.f} " + keyWordHover
            ),
        )
    )

    # UK
    if lang == 'EL':
        fig.add_trace(
            go.Scatter(
                y=df[
                    (df["Country/Region"] == "United Kingdom")
                    & (df[columnName] > numberCompare)
                ][columnName],
                name="Ηνωμένο Βασίλειο",
                line=dict(color="#FFD400", width=2),
                hovertemplate="<b>{}</b> στο Ηνωμένο Βασίλειο<extra></extra>".format(
                    "%{y:.f} " + keyWordHover
                ),
            )
        )
    else:
        fig.add_trace(
        go.Scatter(
            y=df[
                (df["Country/Region"] == "United Kingdom")
                & (df[columnName] > numberCompare)
            ][columnName],
            name="United Kingdom",
            line=dict(color="#FFD400", width=2),
            hovertemplate="<b>{}</b> in United Kingdom <extra></extra>".format(
                "%{y:.f} " + keyWordHover
            ),
        )
    )

    # USA
    if lang == 'EL':
        fig.add_trace(
            go.Scatter(
                y=df[(df["Country/Region"] == "US") & (df[columnName] > numberCompare)][
                    columnName
                ],
                name="ΗΠΑ",
                line=dict(color="lightgreen", width=2),
                hovertemplate="<b>{}</b> στις ΗΠΑ<extra></extra>".format(
                    "%{y:.f} " + keyWordHover
                ),
            )
        )
    else:
        fig.add_trace(
        go.Scatter(
            y=df[(df["Country/Region"] == "US") & (df[columnName] > numberCompare)][
                columnName
            ],
            name="USA",
            line=dict(color="lightgreen", width=2),
            hovertemplate="<b>{}</b> in USA <extra></extra>".format(
                "%{y:.f} " + keyWordHover
            ),
        )
    )
        
    # Spain
    if lang == 'EL':
        fig.add_trace(
            go.Scatter(
                y=df[(df["Country/Region"] == "Spain") & (df[columnName] > numberCompare)][
                    columnName
                ],
                name="Ισπανία",
                line=dict(color="purple", width=2),
                hovertemplate="<b>{}</b> στην Ισπανία<extra></extra>".format(
                    "%{y:.f} " + keyWordHover
                ),
            )
        )
        
    else:
        fig.add_trace(
        go.Scatter(
            y=df[(df["Country/Region"] == "Spain") & (df[columnName] > numberCompare)][
                columnName
            ],
            name="Spain",
            line=dict(color="purple", width=2),
            hovertemplate="<b>{}</b> in Spain <extra></extra>".format(
                "%{y:.f} " + keyWordHover
            ),
        )
    )
    
    # Greece
    
    temp = "<b>{}</b> στην Ελλάδα<extra></extra>"
    temp_en="<b>{}</b> in Greece<extra></extra>"
    
    fig.add_trace(
        go.Scatter(
            y=df[(df["Country/Region"] == "Greece") & (df[columnName] > numberCompare)][
                columnName
            ],
            name="Ελλάδα" if lang == 'EL' else 'Greece',
            line=dict(color="#BA3A0A", width=3),
            hovertemplate=(temp if lang == 'EL' else temp_en).format(
                "%{y:.f} " + keyWordHover
            ),
        )
    )

    # μέγεθος γραμμής σε κάθε χώρα στο legend, trace/constant
    fig.update_layout(
        legend={"itemsizing": "constant"},
        annotations=[
            dict(
                x=0,
                y=1,
                xref="paper",
                yref="paper",
                text="Δεν περιλαμβάνεται η Κίνα.<br><i>Λογαριθμική κλίμακα</i>" if lang == 'EL'
                else 'China is not included<br><i>Logarithmic scale',
                showarrow=False,
                align="left",
            )
        ],
    )
    fig.update_layout(height=380, margin=dict(l=10, r=10, b=10, t=65, pad=10))

    if show:
        config = dict(
            {
                "displayModeBar": True,
                "scrollZoom": False,
                "displaylogo": False,
                "responsive": True,
                "staticPlot": False,
            }
        )
        fig.show(config=config)
    if lang == 'EL':
        fig.write_json(outputName + ".json")
    fig.write_json(outputName + "_" + lang + ".json")


def heatmap(
    data,
    countries_df,
    population,
    columnName,
    outputName,
    titleGraphic,
    keyWord,
    show=False,
    lang="EL",
):
    """ φορτώνουμε το πρώτο αρχείο από το Hopkins"""
    
    df = data.drop(["Lat", "Long"], axis=1)
    #CASES CORRECTIONS
    if data==confirmed_H_df:

        #Honduras from 2100 to 2006 on 5/11
        df.loc[df['Country/Region']=='Honduras','5/11/20']=2006
    
        #Portugal - correction of dublicates
        df.loc[df['Country/Region']=='Portugal','4/30/20']=24884
        df.loc[df['Country/Region']=='Portugal','5/1/20']=25190
        df.loc[df['Country/Region']=='Portugal','5/2/20']=25190
        
    if data==deaths_H_df:
        df.loc[df['Country/Region']=='Sweden','8/6/20']-=3
        df.loc[df['Country/Region']=='Cuba','8/13/20']-=1
        df.loc[df['Country/Region']=='Austria','7/21/20']+=1

    """ υπολογίζουμε το difference από ημέρα σε ημέρα, ώστε να βγάλουμε τα ΝΕΑ κρούσματα/θάνατοι ανά ημέρα"""
    cols = df.columns.to_list()
    df_dif = df[cols[4:]].diff(axis=1)
    df = df_dif.join(df["Country/Region"])
    """ αλλάζουμε τα data από wide σε long + μετρέπουμε τη στήλη Date σε datetime"""
    df = pd.melt(
        df, id_vars=["Country/Region"], var_name="Date", value_name=columnName
    ).astype({"Date": "datetime64[ns]", columnName: "Int64"}, errors="ignore")

    """ φορτώνουμε το αρχείο με την αντιστοίχιση ελληνικών - αγγλικών ονομάτων χωρών"""
    gr = countries_df
    """ το συνδέουμε με το dataframe από το Hopkins ώστε να προστεθεί το ADMIN_GR"""
    df = pd.merge(df, gr, how="left", left_on="Country/Region", right_on="ADMIN")

    """ φορτώνουμε το αρχείο με τους πληθυσμούς"""
    pop = population
    """συνδέουμε το dataframe με τα ελληνικά ονόματα """
    gr = pd.merge(gr, pop, how="right", left_on="ADMIN", right_on="Country,Other")

    """Ενώνουμε το dataframe του Hopkins και εκείνο του population με βάση την στήλη με τα ελληνικά ονόματα"""
    df = pd.merge(df, gr, how="left", on="ADMIN_GR")

    """ υπολογίζουμε συγκεντρωτικά για κάθε χώρα τα κρούσματα και τους θανάτους ανά ημέρα"""
    df = (
        df.groupby(["Country/Region", "Date", "ADMIN_GR", "Population (2020)"])[
            columnName
        ]
        .sum()
        .reset_index()
    )

    """ ------------------- ΠΡΟΕΤΟΙΜΑΖΟΥΜΕ ΤΗ ΣΤΗΛΗ ΠΟΥ ΘΑ ΟΠΤΙΚΟΠΟΙΗΣΟΥΜΕ -----------------"""
    df[columnName + "_per_hundr"] = (df[columnName] / df["Population (2020)"]) * 100000

    """ ------------------- ΕΠΙΛΕΓΟΥΜΕ ΤΙΣ ΧΩΡΕΣ ΜΕ ΠΑΡΟΜΟΙΟ ΠΛΗΘΥΣΜΟ ΜΕ ΤΗΝ ΕΛΛΑΔΑ -----------"""

    df=df[(df['Population (2020)']>9000000)
            & (df['Population (2020)']<12000000)
            & (df['Date']>'2020-03-06')]
    
    if data==confirmed_H_df:
        df=df[(df["Country/Region"] != "Jordan")]
    
    if data==deaths_H_df:
        df=df[(df["Country/Region"] != "Czechia")]

    """ ------------------- ΞΕΚΙΝΑ Η ΟΠΤΙΚΟΠΟΙΗΣΗ ------------------"""

    countries_el = df["ADMIN_GR"]
    countries_en = df["Country/Region"]
    item = df[columnName + "_per_hundr"]
    base = datetime.datetime.today()
    dates = df["Date"]

    fig = go.Figure(
        data=go.Heatmap(
            z=item,
            x=dates,
            y=countries_el if lang == 'EL' else countries_en,
            customdata=df[columnName],
            showscale=True,
            hovertemplate="<b>%{y}</b><br>"
            + "<i>%{x}</i><br><br>"
            + "%{customdata} "
            + keyWord
            + "<extra></extra>",
            colorscale=[
                [0, "#E6ECEC"],  # 0
                [1.0 / 10000, "#dadada"],  # 10
                [1.0 / 1000, "#d7dfe3"],  # 100
                [1.0 / 100, "#b0bfc7"],  # 1000
                [1.0 / 10, "#3f6678"],  # 10000
                [1.0, "#BA3A0A"],
            ],
            colorbar=dict(
                title=keyWord + "/<br>100 χιλ " if lang == 'EL' else keyWord + "/<br>100k ",
                tick0=0,
                tickmode="auto",  # όταν το tickmode είναι array, τότε παίρνει τα values του tickvals
                tickvals=[0, 1000, 1800],
            ),
        )
    )

    fig.update_layout(title=titleGraphic)

    fig.update_layout(
        hovermode="closest",
        hoverlabel=dict(bgcolor="white", font_size=12, font_family="Roboto"),
        hoverlabel_align="left",
    )

    fig.update_layout(
        paper_bgcolor="#E6ECEC",
        plot_bgcolor="#E6ECEC",
        font=dict(family="Roboto", size=11, color="#114B5F"),
    )

    fig.update_layout(height=400, margin=dict(l=10, r=10, b=20, t=75, pad=10))

    if show:
        config = dict(
            {
                "displayModeBar": True,
                "scrollZoom": False,
                "displaylogo": False,
                "responsive": True,
                "staticPlot": False,
            }
        )
    if lang == 'EL':
        fig.write_json(outputName + ".json")
    fig.write_json(outputName + "_" + lang + ".json")


def create_chrolopleth_casesrate(
    name, wom_data, countries_data, token, show=False, lang="EL"
):
    wom = wom_data

    countries_names = countries_data
    countries_names = countries_names.rename(columns={"ADMIN": "Country,Other"})
    wom = pd.merge(wom, countries_names, on="Country,Other", how="left")

    wom = wom[(wom['Country,Other'] != 'Sudan') & (wom['Country,Other'] != 'Yemen') & (wom['Country,Other'] != 'Burundi')]
    wom = wom[wom['Country,Other'] != 'Sao Tome and Principe']
    wom = wom[wom['Country,Other'] != 'Algeria']

    wom["Tot Cases/1M pop"] = (wom["Tot Cases/1M pop"]).apply(lambda x: parseFloat(x))
    wom["Deaths/1M pop"] = (wom["Deaths/1M pop"]).apply(lambda x: parseFloat(x))
    wom["Tests/ 1M pop"] = (wom["Tests/ 1M pop"]).apply(lambda x: parseFloat(x))

    wom["testing_median_diff_pct"] = (
        (wom["Tests/ 1M pop"] - wom["Tests/ 1M pop"].median())
        / wom["Tests/ 1M pop"].median()
    ) * 100
    wom["cases_rate_normalized"] = (wom["Tot Cases/1M pop"] * 100) / wom[
        "Tests/ 1M pop"
    ]
    wom["cases_rate_normalized"] = wom["cases_rate_normalized"].round(2)
    wom["cases_rate_median_diff_pct"] = (
        (wom["cases_rate_normalized"] - wom["cases_rate_normalized"].median())
        / wom["cases_rate_normalized"].median()
    ) * 100

    res = requests.get(
        "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data/world-countries.json"
    )
    countries = res.json()

    def choropleth_casesrate_text():
        if lang == "EL":
            return wom.ADMIN_GR
        else:
            return wom["Country,Other"]

    fig = go.Figure(
        go.Choroplethmapbox(
            geojson=countries,
            locations=wom.iso_alpha_3,
            z=wom.cases_rate_normalized.astype(float),
            colorscale=[("#3f6678"), ("#BA3A0A")],
            zmin=wom.cases_rate_normalized.min(),
            zmax=60,
            text=choropleth_casesrate_text(),
            marker_line_width=0.5,
            colorbar_title="%",
            colorbar=dict(tick0=0, dtick=20),
        )
    )

    fig.update_layout(
        mapbox_style="mapbox://styles/trilikis/ck916mr2y0wox1iozbu71xkw6",
        mapbox_accesstoken=token,
        mapbox_zoom=-1,
        mapbox_center={"lat": 41.902782, "lon": 12.496366},
    )

    fig.update_layout(
        paper_bgcolor="#E6ECEC",
        plot_bgcolor="#E6ECEC",
        margin=dict(l=20, r=0, t=50, b=50),
        title=dict(
            text=labels.choropleth_casesrate_title(lang),
            y=0.98,
            x=0.02,
            xanchor="left",
            yanchor="top",
            font=dict(family="Roboto", size=16, color="#114B5F"),
        ),
        annotations=[
            dict(
                x=0,
                y=-0.1,
                xref="paper",
                yref="paper",
                text=labels.choropleth_casesrate_annot(lang),
                showarrow=False,
                visible=True,
                align="left",
                font=dict(family="Roboto", color="#114B5F", size=10),
            )
        ],
    )

    if show:
        config = dict(
            {
                "displayModeBar": True,
                "scrollZoom": False,
                "displaylogo": False,
                "responsive": True,
                "staticPlot": False,
            }
        )
        fig.show(config=config)
    if lang == 'EL':
        fig.write_json(name + ".json")
    fig.write_json(name + "_" + lang + ".json")


def create_chrolopleth_recoveredrate(
    name, wom_data, countries_data, token, show=False, lang="EL"
):
    wom = wom_data

    countries_names = countries_data
    countries_names = countries_names.rename(columns={"ADMIN": "Country,Other"})
    wom = pd.merge(wom, countries_names, on="Country,Other", how="left")

    wom["Tot Cases/1M pop"] = (wom["Tot Cases/1M pop"]).apply(lambda x: parseFloat(x))
    wom["Deaths/1M pop"] = (wom["Deaths/1M pop"]).apply(lambda x: parseFloat(x))
    wom["Tests/ 1M pop"] = (wom["Tests/ 1M pop"]).apply(lambda x: parseFloat(x))

    wom["TotalCases"] = (wom["TotalCases"]).apply(lambda x: parseFloat(x))
    wom["TotalRecovered"] = (wom["TotalRecovered"]).apply(lambda x: parseFloat(x))

    wom["testing_median_diff_pct"] = (
        (wom["Tests/ 1M pop"] - wom["Tests/ 1M pop"].median())
        / wom["Tests/ 1M pop"].median()
    ) * 100
    wom["cases_rate_normalized"] = (wom["Tot Cases/1M pop"] * 100) / wom[
        "Tests/ 1M pop"
    ]
    wom["cases_rate_normalized"] = wom["cases_rate_normalized"].round(2)
    wom["cases_rate_median_diff_pct"] = (
        (wom["cases_rate_normalized"] - wom["cases_rate_normalized"].median())
        / wom["cases_rate_normalized"].median()
    ) * 100
    wom["recovered_rate"] = (wom["TotalRecovered"] * 100) / wom["TotalCases"]
    wom["recovered_rate"] = wom["recovered_rate"].round(2)

    res = requests.get(
        "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data/world-countries.json"
    )
    countries = res.json()

    def choropleth_recoveredrate_text():
        if lang == "EL":
            return wom.ADMIN_GR
        else:
            return wom["Country,Other"]

    fig = go.Figure(
        go.Choroplethmapbox(
            geojson=countries,
            locations=wom.iso_alpha_3,
            z=wom.recovered_rate.astype(float),
            colorscale=["#3f6678", "#FFC100"],
            zmin=wom.recovered_rate.min(),
            zmax=wom.recovered_rate.max(),
            text=choropleth_recoveredrate_text(),
            marker_line_width=0.5,
            colorbar_title="%",
            colorbar=dict(tick0=0, dtick=20),
        )
    )

    fig.update_layout(
        mapbox_style="mapbox://styles/trilikis/ck916mr2y0wox1iozbu71xkw6",
        mapbox_accesstoken=token,
        mapbox_zoom=-1,
        mapbox_center={"lat": 41.902782, "lon": 12.496366},
    )

    fig.update_layout(
        paper_bgcolor="#E6ECEC",
        plot_bgcolor="#E6ECEC",
        margin=dict(l=20, r=0, t=50, b=50),
        title=dict(
            text=labels.choropleth_recoveredrate_title(lang),
            y=0.98,
            x=0.02,
            xanchor="left",
            yanchor="top",
            font=dict(family="Roboto", size=16, color="#114B5F"),
        ),
        annotations=[
            dict(
                x=0,
                y=-0.1,
                xref="paper",
                yref="paper",
                text=labels.choropleth_recoveredrate_annot(lang),
                showarrow=False,
                visible=True,
                align="left",
                font=dict(family="Roboto", color="#114B5F", size=10),
            )
        ],
    )

    if show:
        config = dict(
            {
                "displayModeBar": True,
                "scrollZoom": False,
                "displaylogo": False,
                "responsive": True,
                "staticPlot": False,
            }
        )
        fig.show(config=config)
    if lang == 'EL':
        fig.write_json(name + ".json")
    fig.write_json(name + "_" + lang + ".json")


def create_regions_facets(name, regions_greece_deaths_data, show=False, lang="EL"):
    deaths = regions_greece_deaths_data
    deaths = deaths.drop(["pop_11", "district_EN"], axis=1)
    deaths["district"] = deaths.district.str.replace("Περιφέρεια", "")
    deaths["district"] = deaths.district.str.replace(
        "Μακεδονίας Θράκης", "Μακεδονίας & Θράκης"
    )
    deaths = deaths[
        (deaths.district != "Χωρίς Μόνιμη Κατοικία στην Ελλάδα")
        & (deaths.district != "Χωρίς Γεωγραφικό Προσδιορισμό")
    ]
    deaths = deaths.melt(
        id_vars=["district"], var_name="Date", value_name="deaths"
    ).astype({"Date": "datetime64[ns]", "deaths": "Int64"})
    deaths = pd.DataFrame(
        deaths.groupby(["district", "Date"]).deaths.sum().reset_index()
    )
    deaths = deaths[deaths.deaths > 0]

    if lang == "EL":
        deaths["district"] = deaths.district
    else:
        deaths["district"] = deaths.district.str.replace("Αττικής", "Attica")
        deaths["district"] = deaths.district.str.replace("Άγιον Όρος", "Mount Athos")
        deaths["district"] = deaths.district.str.replace(
            "Ανατολικής Μακεδονίας & Θράκης", "East Macedonia-Thrace"
        )
        deaths["district"] = deaths.district.str.replace(
            "Βορείου Αιγαίου", "North Aegean"
        )
        deaths["district"] = deaths.district.str.replace(
            "Δυτικής Ελλάδας", "Western Greece"
        )
        deaths["district"] = deaths.district.str.replace(
            "Δυτικής Μακεδονίας", "Western Macedonia"
        )
        deaths["district"] = deaths.district.str.replace("Ηπείρου", "Epirus")
        deaths["district"] = deaths.district.str.replace("Θεσσαλίας", "Thessaly")
        deaths["district"] = deaths.district.str.replace(
            "Ιονίων Νήσων", "Ionian Islands"
        )
        deaths["district"] = deaths.district.str.replace(
            "Κεντρικής Μακεδονίας", "Central Macedonia"
        )
        deaths["district"] = deaths.district.str.replace("Κρήτης", "Crete")
        deaths["district"] = deaths.district.str.replace(
            "Νοτίου Αιγαίου", "South Aegean"
        )
        deaths["district"] = deaths.district.str.replace("Πελοποννήσου", "Peloponnese")
        deaths["district"] = deaths.district.str.replace(
            "Στερεάς Ελλάδας και Εύβοιας", "Cenral Greece"
        )

    fig = px.area(
        deaths,
        y="deaths",
        x="Date",
        facet_col="district",
        facet_col_wrap=3,
        labels=labels.regions_facets_labels(lang),
    )

    fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
    fig.for_each_annotation(lambda a: a.update(text=a.text.replace("Περιφέρεια", "")))

    fig["layout"]["yaxis"]["title"]["text"] = ""
    fig["layout"]["yaxis3"]["title"]["text"] = ""
    fig["layout"]["yaxis5"]["title"]["text"] = ""
    fig["layout"]["yaxis7"]["title"]["text"] = ""
    fig["layout"]["xaxis2"]["title"]["text"] = ""
    fig["layout"]["xaxis1"]["title"]["text"] = ""
    fig["layout"]["xaxis3"]["title"]["text"] = ""

    fig.update_layout(
        height=450,
        xaxis=XAXIS_STYLE,
        xaxis2=XAXIS_STYLE,
        xaxis3=XAXIS_STYLE,
        yaxis=YAXIS_STYLE,
#         yaxis3=YAXIS_STYLE2,
#         yaxis5=YAXIS_STYLE2,
        yaxis7=YAXIS_STYLE,
#         yaxis9=YAXIS_STYLE2,
#         yaxis2=YAXIS_STYLE,
        yaxis4=YAXIS_STYLE,
#         yaxis6=YAXIS_STYLE2,
#         yaxis8=YAXIS_STYLE2,
        yaxis10=YAXIS_STYLE,
        showlegend=False,
        paper_bgcolor="#E6ECEC",
        plot_bgcolor="#E6ECEC",
        title=dict(text=labels.regions_facets_title(lang), font=TEXTFONT),
        # margin=dict(l=10, r=10, b=10, t=90, pad=0),
        hoverlabel=dict(font_size=8, font_family="Roboto"),
        yaxis4_title=dict(
            text="", font=dict(family="Roboto", size=8, color="#114B5F"),
        ),
        yaxis10_title=dict(
            text="", font=dict(family="Roboto", size=8, color="#114B5F"),
        ),
        xaxis_title=dict(
            text=labels.regions_facets_xaxis_note(lang),
            font=dict(family="Roboto", size=8, color="#114B5F"),
        ),
        hovermode="closest",
    )

    for annot in fig.layout.annotations:
        annot.update(font=dict(family="Roboto", size=8, color="#114B5F"))

    fig.update_traces(line=dict(color="#BA3A0A"))

    fig.update_layout(height=450, margin=dict(l=10, r=10, b=10, t=90, pad=0))

    if show:
        config = dict(
            {
                "displayModeBar": True,
                "scrollZoom": False,
                "displaylogo": False,
                "responsive": True,
                "staticPlot": False,
            }
        )

        fig.show(config=config)
    if lang == 'EL':
        fig.write_json(name + ".json")
    fig.write_json(name + "_" + lang + ".json")


def growth_rate(
    data,
    countries_data,
    population,
    numberCompare,
    columnName,
    outputName,
    titleGraphic,
    keyWordHover,
    xAxis,
    yAxis,
    show=False,
    lang="EL",
):
    """ φορτώνουμε το πρώτο αρχείο από το Hopkins"""
    df = (
        data.drop(["Lat", "Long"], axis=1)
        .melt(
            id_vars=["Province/State", "Country/Region"],
            var_name="Date",
            value_name=columnName,
        )
        .astype({"Date": "datetime64[ns]", columnName: "Int64"}, errors="ignore")
    )

    """ φορτώνουμε το αρχείο με την αντιστοίχιση ελληνικών - αγγλικών ονομάτων χωρών"""
    gr = countries_data
    """ το συνδέουμε με το dataframe από το Hopkins ώστε να προστεθεί το ADMIN_GR"""
    df = pd.merge(df, gr, how="left", left_on="Country/Region", right_on="ADMIN")

    """ φορτώνουμε το αρχείο με τους πληθυσμούς"""
    pop = population
    """συνδέουμε το dataframe με τα ελληνικά ονόματα """
    gr = pd.merge(gr, pop, how="right", left_on="ADMIN", right_on="Country,Other")

    """Ενώνουμε το dataframe του Hopkins και εκείνο του population με βάση την στήλη με τα ελληνικά ονόματα"""
    df = pd.merge(df, gr, how="left", on="ADMIN_GR")

    """ υπολογίζουμε συγκεντρωτικά για κάθε χώρα τα κρούσματα και τους θανάτους ανά ημέρα"""
    df = (
        df.groupby(["Country/Region", "Date", "ADMIN_GR", "Population (2020)"])[
            columnName
        ]
        .sum()
        .reset_index()
    )

    df["7_day_avg_growth"] = (
        df.groupby(["Country/Region"])[columnName].pct_change().rolling(window=7).mean()
        * 100
    ).round(1)

    """ ------------------- ΞΕΚΙΝΑ Η ΟΠΤΙΚΟΠΟΙΗΣΗ ------------------"""

    """ Φτιάχνουμε ένα variable που ΔΕΝ ΘΑ ΠΕΡΙΕΧΕΙ τις χώρες αναφοράς - που θα χρωματίσουμε με άλλο χρώμα"""
    cnt = df[
        (df["Country/Region"] != "Greece")
        & (df["Country/Region"] != "Germany")
        & (df["Country/Region"] != "Italy")
        & (df["Country/Region"] != "United Kingdom")
        & (df["Country/Region"] != "US")
        & (df["Country/Region"] != "Spain")
        & (df["Country/Region"] != "China")
    ]

    fig = go.Figure()
    fig.update_layout(
        paper_bgcolor="#E6ECEC",
        title=titleGraphic,
        plot_bgcolor="#E6ECEC",
        font=dict(family="Roboto", size=11, color="#114B5F"),
    )

    fig.update_layout(
        hovermode="closest",
        hoverlabel=dict(bgcolor="white", font_size=12, font_family="Roboto"),
        hoverlabel_align="left",
    )

    fig.update_layout(showlegend=True)
    fig.update_layout(
        legend_title="Διπλό κλικ σε κάθε<br>χώρα για να την <br>απομονώσετε<br>"
        if lang == "EL"
        else "Double click<br>to select each<br>country",
        legend=dict(
            traceorder="reversed",
            font=dict(family="roboto", size=10, color="black"),
            bgcolor="#E6ECEC",
            bordercolor="#dadada",
            borderwidth=0.3,
        ),
    )

    fig.update_yaxes(
        nticks=8,
        rangemode="tozero",
        showticklabels=True,
        showline=True,
        linewidth=2,
        linecolor="#114B5F",
        showgrid=True,
        gridwidth=0.1,
        gridcolor="#F8FAFA",
        title_text=yAxis,
        title_font={"size": 11, "color": "#114B5F"},
    )

    fig.update_xaxes(
        ticks=None,
        rangemode="tozero",
        showticklabels=True,
        showline=False,
        linewidth=0.1,
        linecolor="#F8FAFA",
        showgrid=True,
        gridwidth=0.1,
        gridcolor="#F8FAFA",
        title_text=xAxis,
        title_font={"size": 11, "color": "#114B5F"},
    )

    fig.update_layout(yaxis_type="log")

    fig.update_layout(height=380)

    # world - Dataframe για μετά την 1η Μαρτίου
    world = df[(df["Date"] > "2020-03-01")]
    last_day = world["Date"].max()
    countries_with_increased = world[
        (world.Date == last_day) & (world["7_day_avg_growth"] > numberCompare)
    ]["Country/Region"].tolist()

    # DataFrame με τις χώρες που έχουν ρυθμό αύξησης άνω του numberCompare
    world_df = world[world["Country/Region"].isin(countries_with_increased)]

    if lang == "EL":
        fig.add_trace(
            go.Scatter(
                y=world_df["7_day_avg_growth"],
                x=world_df["Date"],
                name="<i>Χώρες με<br>>{}% αύξηση<br> {}<br>τις τελευταίες<br>7 ημέρες</i>".format(
                    numberCompare, keyWordHover
                ),
                text=[i for i in world_df["ADMIN_GR"]],
                hovertemplate="<b>{}</b><br><i>{}</i><br>{} αύξηση {} <extra></extra>".format(
                    "%{text}", "%{x}", "%{y:.f}% ", keyWordHover
                ),
                line=dict(color="gray", width=0.2),
                showlegend=True,
            )
        )
    else:
        fig.add_trace(
            go.Scatter(
                y=world_df["7_day_avg_growth"],
                x=world_df["Date"],
                name="<i>Countries with<br>>{}% increase<br> {}<br>in the last<br>7 days</i>".format(
                    numberCompare, keyWordHover
                ),
                text=[i for i in world_df["Country/Region"]],
                hovertemplate="<b>{}</b><br><i>{}</i><br>{} increase {} <extra></extra>".format(
                    "%{text}", "%{x}", "%{y:.f}% ", keyWordHover
                ),
                line=dict(color="gray", width=0.2),
                showlegend=True,
            )
        )

    # Γερμανία
    if lang == "EL":
        fig.add_trace(
            go.Scatter(
                y=world[(world["Country/Region"] == "Germany")]["7_day_avg_growth"],
                x=world["Date"],
                name="Γερμανία",
                line=dict(color="black", width=2),
                hovertemplate="<b>{}</b><br>{}αύξηση {} στην Γερμανία <extra></extra>".format(
                    "%{x}", "%{y:.f}% ", keyWordHover
                ),
            )
        )
    else:
        fig.add_trace(
            go.Scatter(
                y=world[(world["Country/Region"] == "Germany")]["7_day_avg_growth"],
                x=world["Date"],
                name="Germany",
                line=dict(color="black", width=2),
                hovertemplate="<b>{}</b><br>{}increase {} in Germany<extra></extra>".format(
                    "%{x}", "%{y:.f}% ", keyWordHover
                ),
            )
        )

    # Ιταλία
    if lang == "EL":
        fig.add_trace(
            go.Scatter(
                y=world[(world["Country/Region"] == "Italy")]["7_day_avg_growth"],
                x=world["Date"],
                name="Ιταλία" if lang == "el" else "Italy",
                line=dict(color="#3E82B3", width=2),
                hovertemplate="<b>{}</b><br>{}αύξηση {} στην Ιταλία<extra></extra>".format(
                    "%{x}", "%{y:.f}% ", keyWordHover
                ),
            )
        )
    else:
        # UK
        fig.add_trace(
            go.Scatter(
                y=world[(world["Country/Region"] == "United Kingdom")][
                    "7_day_avg_growth"
                ],
                x=world["Date"],
                name="United Kingdom",
                line=dict(color="#FFD400", width=2),
                hovertemplate="<b>{}</b><br>{}increase {} in UK <extra></extra>".format(
                    "%{x}", "%{y:.f}% ", keyWordHover
                ),
            )
        )

    # USA
    if lang == "EL":
        fig.add_trace(
            go.Scatter(
                y=world[(world["Country/Region"] == "US")]["7_day_avg_growth"],
                x=world["Date"],
                name="ΗΠΑ",
                line=dict(color="lightgreen", width=2),
                hovertemplate="<b>{}</b><br>{}αύξηση {} στις ΗΠΑ<extra></extra>".format(
                    "%{x}", "%{y:.f}% ", keyWordHover
                ),
            )
        )
    else:
        fig.add_trace(
            go.Scatter(
                y=world[(world["Country/Region"] == "US")]["7_day_avg_growth"],
                x=world["Date"],
                name="USA",
                line=dict(color="lightgreen", width=2),
                hovertemplate="<b>{}</b><br>{}increase {} in USA <extra></extra>".format(
                    "%{x}", "%{y:.f}% ", keyWordHover
                ),
            )
        )

    # Spain
    if lang == "EL":
        fig.add_trace(
            go.Scatter(
                y=world[(world["Country/Region"] == "Spain")]["7_day_avg_growth"],
                x=world["Date"],
                name="Ισπανία",
                line=dict(color="purple", width=2),
                hovertemplate="<b>{}</b><br>{} αύξηση {} στην Ισπανία<extra></extra>".format(
                    "%{x}", "%{y:.f}% ", keyWordHover
                ),
            )
        )
    else:
        fig.add_trace(
            go.Scatter(
                y=world[(world["Country/Region"] == "Spain")]["7_day_avg_growth"],
                x=world["Date"],
                name="Spain",
                line=dict(color="purple", width=2),
                hovertemplate="<b>{}</b><br>{} increase {} in Spain<extra></extra>".format(
                    "%{x}", "%{y:.f}% ", keyWordHover
                ),
            )
        )

    # Greece
    if lang == "EL":
        fig.add_trace(
            go.Scatter(
                y=world[(world["Country/Region"] == "Greece")]["7_day_avg_growth"],
                x=world["Date"],
                name="Ελλάδα",
                line=dict(color="#BA3A0A", width=3),
                hovertemplate="<b>{}</b><br>{} αύξηση {} στην Ελλάδα<extra></extra>".format(
                    "%{x}", "%{y:.f}% ", keyWordHover
                ),
                line_shape="spline",
            )
        )
    else:
        fig.add_trace(
            go.Scatter(
                y=world[(world["Country/Region"] == "Greece")]["7_day_avg_growth"],
                x=world["Date"],
                name="Greece",
                line=dict(color="#BA3A0A", width=3),
                hovertemplate="<b>{}</b><br>{} increase {} in Greece<extra></extra>".format(
                    "%{x}", "%{y:.f}% ", keyWordHover
                ),
                line_shape="spline",
            )
        )

    # μέγεθος γραμμής σε κάθε χώρα στο legend, trace/constant
    fig.update_layout(
        legend={"itemsizing": "constant"},
        annotations=[
            dict(
                x=0,
                y=1.1,
                xref="paper",
                yref="paper",
                text='<i>Η τιμή κάθε ημέρας είναι ο μέσος όρος <br>των ρυθμών μεταβολής των τελευταίων επτά ημερών</i>' if lang == 'EL'
                          else 'Average daily change in deaths,<br>over the previous 7 days',
                showarrow=False,
                align="left",
            )
        ],
    )
    fig.update_layout(height=450, margin=dict(l=10, r=10, b=10, t=80, pad=0))

    if show:
        config = dict(
            {
                "displayModeBar": True,
                "scrollZoom": False,
                "displaylogo": False,
                "responsive": True,
                "staticPlot": False,
            }
        )
    if lang == 'EL':
        fig.write_json(outputName + ".json")
    fig.write_json(outputName + "_" + lang + ".json")


def create_non_residents_line(
name, regions_greece_cases, show=False, lang="EL"
):

    rgc = regions_greece_cases
    rgc = rgc[rgc.district=='Χωρίς Μόνιμη Κατοικία στην Ελλάδα']
    rgc = rgc.drop(['district','district_EN','pop_11'],axis=1)
    rgc = rgc.T
    rgc = rgc.rename(columns={rgc.columns[0]:'cases'})
    rgc = rgc.reset_index()[57:]
    rgc1 = rgc.reset_index()
    rgc1 = rgc1.rename(columns={'level_0':'index_previous','index':'date'})
    rgc1["date"] = pd.to_datetime(rgc1["date"])
    rgc1["date"] = pd.to_datetime(rgc1["date"], format="%b-%d-%y").dt.strftime("%d-%b")
    rgc1["date_gr"] = rgc1["date"]
    rgc1["date_gr"] = rgc1["date_gr"].astype(str)
    rgc1["date_gr"] = rgc1["date_gr"].str.replace("Feb", "Φεβ")
    rgc1["date_gr"] = rgc1["date_gr"].str.replace("Mar", "Μαρ")
    rgc1["date_gr"] = rgc1["date_gr"].str.replace("Apr", "Απρ")
    rgc1["date_gr"] = rgc1["date_gr"].str.replace("May", "Μάι")
    rgc1["date_gr"] = rgc1["date_gr"].str.replace("Jun", "Ιούν")
    rgc1["date_gr"] = rgc1["date_gr"].str.replace("Jul", "Ιούλ")
    rgc1["cases"] = rgc1["cases"].astype(float)
    rgc1['mvavg_cases'] = rgc1['cases'].rolling(window=7).mean().round()

    def line_xaxis():
        if lang == "EL":
            return rgc1[6:].date_gr
        else:
            return rgc1[6:].date

    # Initialize figure
    fig = go.Figure()

    # Add Traces
    fig.add_trace(
        go.Scatter(
            x=line_xaxis(),
            y=rgc1[6:].mvavg_cases,
            mode="lines",
            connectgaps=True,
            marker_color="#BA3A0A",
    #             name= 'Title',
            line_shape="spline",
            line=dict(width=4)
        )
    )

    fig.update_layout(
        xaxis=dict(
                showline=True,
                zeroline=True,
                showgrid=False,
                showticklabels=True,
                linecolor="#114B5F",
                linewidth=0.1,
                ticks="outside",
                tickcolor="#BBBBBB",
                gridcolor="#F8FAFA",
                tickfont=TICKFONT,
                dtick = 10
            ),
        yaxis=YAXIS,
        showlegend=False,
        legend=dict(font=dict(family="Roboto", size=12, color="#114B5F")),
        paper_bgcolor="#E6ECEC",
        plot_bgcolor="#E6ECEC",
        title=dict(
            text= labels.non_residents_line_title(lang),
            font=dict(family="Roboto", size=16, color="#114B5F"),
        ),
        hoverlabel=dict(font_size=10, font_family="Roboto"),
        hovermode="closest",
        xaxis_title=dict(
            text= labels.non_residents_line_xaxis_note(lang),
            font=dict(family="Roboto", size=8, color="#114B5F"),
            ),
        yaxis_title=dict(text=labels.non_residents_line_yaxis_title(lang), font=TICKFONT),
    )

    fig.update_layout(height=450, margin=dict(l=10, r=10, b=10, t=90, pad=0))

    if show:
        config = dict(
            {
                "displayModeBar": True,
                "scrollZoom": False,
                "displaylogo": False,
                "responsive": True,
                "staticPlot": False,
            }
        )
    fig.show()
    if lang == 'EL':
        fig.write_json(name + ".json")
    fig.write_json(name + "_" + lang + ".json")