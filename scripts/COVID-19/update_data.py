# -*- coding: utf-8 -*-

import os
import sys
import re
import argparse
from datetime import datetime
import requests

import pandas as pd
from bs4 import BeautifulSoup
from pytz import timezone

import graphs


def normalize_keyword(s):
    """
    Normalize String
    """
    if s is None or len(s) == 0:
        return ''
    text = ''.join(s)

    text = re.sub('[!@#$<>|]', '', text)
    text = text.strip()
    text = text.replace('\n', ' ')
    text = text.replace('+', '')
    # text = text.replace('\xc2\xa0', ' ')
    # remove html forgotten tags
    text = re.sub(re.compile('<.*?>'), '', text)
    # remove double space
    text = re.sub(' +', ' ', text)

    return text


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='COVID-19 Data Builder')
    parser.add_argument('root_path', help='Project Root', default='./')

    parser.add_argument('--mapbox_token', default=os.environ.get('MAPBOX_TOKEN'))

    args = parser.parse_args()
    root_path = args.root_path
    mapbox_token = args.mapbox_token

    page = requests.get('https://www.worldometers.info/coronavirus/', headers={
        'User-Agent': 'Mozilla/5.0 (compatible; CVCIOBot/1.0; +https://mediawatch.io/)',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    })
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find('table', attrs={'id': 'main_table_countries_today'})

    t_headers = [normalize_keyword(header.text.encode(
        'utf-8', 'ignore')) for header in table.find_all('th')]
    
    t_headers = [i if i is not '' else 'Tot Cases/1M pop' for i in t_headers]
    
    t_rows = []
    for row in table.find_all('tr'):
        t_rows.append([normalize_keyword(val.text.encode('utf-8', 'ignore'))
                       for val in row.find_all('td')])
    
    required_headers = [
        'Country,Other', 'TotalCases', 'NewCases',
        'TotalDeaths', 'NewDeaths', 'TotalRecovered',
        'ActiveCases', 'Serious,Critical', 'Tot Cases/1M pop',
        'Deaths/1M pop', 'TotalTests', 'Tests/ 1M pop', 'Continent'
    ]
    if not all([i in t_headers for i in required_headers]):
        print('Required columns missing. Exiting script.')
        sys.exit(1)

    # save the last row (totals, we need it in the front-end)
    last_row_df = pd.DataFrame([t_rows[-1]], columns=t_headers)
    # load country names
    # (root_path + '/COVID-19/countries_names.csv')
    countries_df = pd.read_csv(
        'https://docs.google.com/spreadsheets/d/e/2PACX-1vRpR8AOJaRsB5by7H3R_GijtaY06J8srELipebO5B0jYEg9pKugT3C6Rk2RSQ5eyerQl7LolshamK27/pub?gid=906157277&single=true&output=csv')
    wom_data_df = pd.DataFrame(t_rows, columns=t_headers)
    
    # check if row exists
    # wom_data_df = wom_data_df[wom_data_df['Country,Other'].isin(
    #     countries_df.ADMIN).astype(int) > 0].reset_index(drop=True)
    
    wom_data_df = wom_data_df[wom_data_df['Country,Other'].isin([
        '', None, 'North America', 'Europe', 'Asia', 'South America', 'Oceania', 'Africa', 'World', 'Total:'
        ]) == False].reset_index(drop=True)
    
    # append last row
    wom_data_df = wom_data_df.append(last_row_df, ignore_index=True)
    # save the new csv
    wom_data_df.to_csv(root_path + '/COVID-19/wom_data.csv', index=False)

    greeceTimeline_df = pd.read_csv(root_path + '/COVID-19/greeceTimeline.csv')

    baseHopkinsURL = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/'
    confirmed_H_df = pd.read_csv(
        baseHopkinsURL + 'time_series_covid19_confirmed_global.csv')
    deaths_H_df = pd.read_csv(
        baseHopkinsURL + 'time_series_covid19_deaths_global.csv')
    population_df = pd.read_csv('https://app.workbenchdata.com/public/moduledata/live/302569.csv',
                                usecols=['Country,Other', 'Population (2020)'])

    graphs.create_scatterplot_casesVStests_logx(
        root_path + '/COVID-19/charts/create_scatterplot_casesVStests_logx', wom_data_df[:-1], countries_df)
    graphs.create_scatterplot_casesVStests_logy(
        root_path + '/COVID-19/charts/create_scatterplot_casesVStests_logy', wom_data_df[:-1], countries_df)
    graphs.create_linechart_deaths_intubated_gr(
        root_path + '/COVID-19/charts/linechart_deaths_intubated_gr', greeceTimeline_df)
    graphs.create_chrolopleth_casesrate(
        root_path + '/COVID-19/charts/create_chrolopleth_casesrate', wom_data_df[:-1], countries_df, mapbox_token)
    graphs.create_chrolopleth_recoveredrate(
        root_path + '/COVID-19/charts/create_chrolopleth_recoveredrate', wom_data_df[:-1], countries_df, mapbox_token)
    graphs.after100Cases(
        deaths_H_df,
        countries_df,
        population_df,
        10,
        'deaths',
        root_path + '/COVID-19/charts/10_deaths.json',
        'Εξέλιξη <b>θανάτων</b> μετά τους πρώτους 10',
        'θάνατοι',
        'Ημέρες από τον 10ο θάνατο',
        'Αριθμός θανάτων',
    )
    graphs.after100Cases(
        confirmed_H_df,
        countries_df,
        population_df,
        100,
        'cases',
        root_path + '/COVID-19/charts/100_cases.json',
        'Εξέλιξη <b>κρουσμάτων</b> μετά τα πρώτα 100',
        'κρούσματα',
        'Ημέρες από το 100ο κρούσμα',
        'Αριθμός κρουσμάτων'
    )
    graphs.heatmap(
        deaths_H_df,
        countries_df,
        population_df,
        'deaths',
        root_path + '/COVID-19/charts/death_heat.json',
        '<b>Θάνατοι</b> ανά 100 χιλ. πληθυσμού σε χώρες<br>με παρόμοιο πληθυσμό με την Ελλάδα',
        'θάνατοι'
    )
    graphs.heatmap(
        confirmed_H_df,
        countries_df,
        population_df,
        'cases',
        root_path + '/COVID-19/charts/cases_heat.json',
        '<b>Κρούσματα</b> ανά 100 χιλ. πληθυσμού σε χώρες<br>με παρόμοιο πληθυσμό με την Ελλάδα',
        'κρούσματα'
    )
    alerts = pd.read_csv(root_path + '/COVID-19/alerts.csv')
    lastUpdatedAt = timezone('Europe/Athens').localize(datetime.now())
    alerts.value[0] = lastUpdatedAt.strftime('%d/%m/%Y %H:%M:%S')
    alerts.to_csv(root_path + '/COVID-19/alerts.csv', index=False)

    sys.exit(0)
