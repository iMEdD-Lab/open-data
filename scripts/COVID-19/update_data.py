# -*- coding: utf-8 -*-

import sys
import re
import argparse
import requests
from datetime import datetime

import pandas as pd
from bs4 import BeautifulSoup
from pytz import timezone

import graphs


def normalize_keyword(s):
    """
    Remove accents from input string
    """
    if s is None or len(s) == 0:
        return ''
    text = ''.join(s)

    text = re.sub('[!@#$<>|]', '', text)
    text = text.strip()
    text = text.replace('\n', ' ')
    text = text.replace('+', '')
    text = text.replace('\xc2\xa0', ' ')
    # remove html forgotten tags
    text = re.sub(re.compile('<.*?>'), '', text)
    # remove double space
    text = re.sub(' +', ' ', text)

    return text


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='COVID-19 Data Builder')
    parser.add_argument('root_path', help='Project Root', default='./')
    args = parser.parse_args()

    root_path = args.root_path

    page = requests.get('https://www.worldometers.info/coronavirus/', headers={
        'User-Agent': 'Mozilla/5.0 (compatible; CVCIOBot/1.0; +https://mediawatch.io/)',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    })
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find('table', attrs={'id': 'main_table_countries_today'})

    t_headers = [normalize_keyword(header.text.encode(
        'utf-8', 'ignore')) for header in table.find_all('th')]

    t_rows = []
    for row in table.find_all('tr'):
        t_rows.append([normalize_keyword(val.text.encode('utf-8', 'ignore'))
                       for val in row.find_all('td')])

    required_headers = [
        'Country,Other', 'TotalCases', 'NewCases',
        'TotalDeaths', 'NewDeaths', 'TotalRecovered',
        'ActiveCases', 'Serious,Critical', 'Tot Cases/1M pop',
        'Deaths/1M pop', 'TotalTests', 'Tests/ 1M pop', 'Continent'
    ]
    if not all([i in t_headers for i in required_headers]):
        print('Required columns missing. Exiting script.')
        sys.exit(1)

    # save the last row (totals, we need it in the front-end)
    last_row_df = pd.DataFrame([t_rows[-1]], columns=t_headers)
    # load country names
    countries_df = pd.read_csv(root_path + '/COVID-19/countries_names.csv')
    wom_data_df = pd.DataFrame(t_rows, columns=t_headers)
    # check if row exists
    wom_data_df = wom_data_df[wom_data_df['Country,Other'].isin(
        countries_df.ADMIN).astype(int) > 0].reset_index(drop=True)
    # append last row
    wom_data_df = wom_data_df.append(last_row_df, ignore_index=True)
    # save the new csv
    wom_data_df.to_csv(root_path + '/COVID-19/wom_data-auto.csv', index=False)

    greeceTimeline_df = pd.read_csv(root_path + '/COVID-19/greeceTimeline.csv')

    graphs.create_scatterplot_casesVStests_logx(root_path + '/COVID-19/charts/create_scatterplot_casesVStests_logx', wom_data_df[:-1], countries_df)
    graphs.create_scatterplot_casesVStests_logy(root_path + '/COVID-19/charts/create_scatterplot_casesVStests_logy', wom_data_df[:-1], countries_df)
    graphs.create_linechart_deaths_intubated_gr(root_path + '/COVID-19/charts/linechart_deaths_intubated_gr', greeceTimeline_df)
    
    alerts = pd.read_csv(root_path + '/COVID-19/alerts.csv')
    lastUpdatedAt = timezone('Europe/Athens').localize(datetime.now())
    alerts.value[0] = lastUpdatedAt.strftime('%d/%m/%Y %H:%M:%S')
    alerts.to_csv(root_path + '/COVID-19/alerts-auto.csv', index=False)
    
    sys.exit(0)
