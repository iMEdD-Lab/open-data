# COVID&ndash;19 API

> last updated at Mar 08, 2021

COVID&ndash;19 API is an [iMEdD's](https://imedd.org) open-source initiative, which was developed to provide the public, journalists and academics with machine readable data on Covid 19. The Greek State doesn't provide this information to the public. The API was developed by [Civic Information Office](https://cvcio.org/) for [iMEdD Lab](https://lab.imedd.org). 

In general, we collect data from [Johns Hopkins CSSE]((https://github.com/CSSEGISandData/COVID-19)) ~~and [WoldOMeter](https://www.worldometers.info/coronavirus/)~~ for the global collection, and from [iMEdD](https://github.com/iMEdD-Lab) for data related to Greece. Additionally, we retrieve vaccines related data from [Data GOV](https://data.gov.gr/datasets/mdg_emvolio/). Data updates run approximately every two hours, and every 15 minutes during 17:00-21:00 +2. You can read more about the data in [iMEdD](https://imedd.org/)'s [open-data relevant repository](https://github.com/iMEdD-Lab/open-data) or see in action the [COVID&ndash;19 Data Visualization Dashboard](https://lab.imedd.org/covid19/). If you are interested in the data collection mechanism you can refer to [COVID&ndash;19 automation](https://github.com/cvcio/covid-19-automation) service.

## Public Endpoints

We provide a public url for the API, but keep in mind that we limit up to **300 requests per minute** (read [Rate Limits](#rate-limiting)).

- https://covid.imedd.org/

## Data Format

Data format may vary accross documents as we enrich data related to Greece. In general we serve 3 different endpoints -raw, total and aggregared- for 3 different levels -global, greece and vaccines. We are working to introducing even more.

###### Raw Global Data

Retrieve raw data from the **global** collection. If no `:from` it will return the last saved date. Keep a note that data retrieved from iMedD are up-to current date (now), whilst data retrieved from JHU are always one date behind.

```json
// GET /global/all/all/2020-12-01
[
    {
        "active": 710515,
        "case_fatality_ratio": 3.4878,
        "cases": 1770149,
        "country": "Italy",
        "date": "2020-12-09T00:00:00Z",
        "deaths": 61739,
        "incidence_rate": 2927.7133,
        "iso2": "IT",
        "iso3": "ITA",
        "last_updated_at": "2020-12-10T10:00:42.301Z",
        "loc": {
            "coordinates": [
                12.56738,
                41.87194
            ],
            "type": "Point"
        },
        "new_cases": 12755,
        "new_deaths": 499,
        "new_recovered": 39266,
        "population": 60461828,
        "recovered": 997895,
        "source": "jhu",
        "uid": 380
    },
    {
        "active": 16539,
        "case_fatality_ratio": 2.7057,
        "cases": 118045,
        "country": "Greece",
        "critical": 579,
        "date": "2020-12-09T00:00:00Z",
        "deaths": 3194,
        "incidence_rate": 1132.5373,
        "intensive_care": 0,
        "iso2": "GR",
        "iso3": "GRC",
        "last_updated_at": "2020-12-10T10:01:01.994Z",
        "loc": {
            "coordinates": [
                21.8243,
                39.0742
            ],
            "type": "Point"
        },
        "new_cases": 0,
        "new_deaths": 0,
        "new_hospitalized": 0,
        "new_recovered": 0,
        "new_tests": 30050,
        "new_tests_rapid": 0,
        "new_tests_rtpcr": 0,
        "population": 10423056,
        "recovered": 98312,
        "source": "imedd",
        "tests": 2814280,
        "tests_rapid": 279523,
        "tests_rtpcr": 2504704,
        "uid": 300
    }
    (...)
]
```

###### Raw Greece Local Data

Retrieve raw data from the **greece** collection. If no `:from` it will return the last saved date.

```json
// GET /greece/all/all/2020-12-01
[
    {
        "case_fatality_ratio": 0,
        "cases": 554,
        "date": "2020-12-09T00:00:00Z",
        "deaths": 0,
        "geo_unit": "-",
        "incidence_rate": 0,
        "last_updated_at": "2020-12-10T10:00:56.557Z",
        "new_cases": 2,
        "new_deaths": 0,
        "population": 0,
        "region": "Imported (They asked to be tested)",
        "source": "imedd",
        "state": "-",
        "uid": "EL002"
    },
    {
        "case_fatality_ratio": 1.3782,
        "cases": 1814,
        "date": "2020-12-09T00:00:00Z",
        "deaths": 25,
        "geo_unit": "Thrace",
        "incidence_rate": 1226.1148,
        "last_updated_at": "2020-12-10T10:00:56.557Z",
        "loc": {
            "coordinates": [
                26.135943100000002,
                41.2443761
            ],
            "type": "Point"
        },
        "new_cases": 57,
        "new_deaths": 0,
        "population": 147947,
        "region": "Evros",
        "source": "imedd",
        "state": "East Macedonia-Thrace",
        "uid": "EL111"
    },
    (...)
]
```

###### Raw Vaccines (Greece Only) Data

Retrieve raw data from the **vaccines** collection. If no `:from` it will return the last saved date.

```json
// GET /vaccines/greece/all/all/2020-12-01
[
    {
        "area": "ΑΡΓΟΛΙΔΑΣ",
        "areaid": 1001,
        "daily_dose_1": 0, // as provided by govgr
        "daily_dose_2": 0, // as provided by govgr
        "date": "2020-12-27T02:00:00+02:00",
        "day_diff": 0, // as provided by govgr
        "day_total": 0, // as provided by govgr
        "geo_unit": "Peloponnese",
        "last_updated_at": "2021-03-08T14:07:00.68+02:00",
        "loc": {
            "coordinates": [
                22.858217,
                37.6525404
            ],
            "type": "Point"
        },
        "new_total_distinct_persons": 0,
        "new_total_dose_1": 0,
        "new_total_dose_2": 0,
        "new_total_vaccinations": 0,
        "population": 97044,
        "region": "Argolis",
        "source": "govgr",
        "state": "Peloponnese",
        "total_distinct_persons": 0, // as provided by govgr
        "total_dose_1": 0, // as provided by govgr
        "total_dose_2": 0, // as provided by govgr
        "total_vaccinations": 0, // as provided by govgr
        "uid": "PE1001"
    },
    (...)
]
```

###### Global Total Data

The `total` endpoint is still in active development and may change without further notice.

```json
// GET /total/global
[
    {
        "cases": 17,
        "country": "Equatorial Guinea",
        "deaths": 0,
        "iso2": "GQ",
        "iso3": "GNQ",
        "last_updated_at": "2020-12-10T18:00:57.843Z",
        "loc": {
            "coordinates": [
                10.2679,
                1.6508
            ],
            "type": "Point"
        },
        "population": 1402985,
        "recovered": 12,
        "sources": [
            "jhu"
        ],
        "tests": 0,
        "total_active": 50,
        "total_cases": 5183,
        "total_critical": null,
        "total_deaths": 85,
        "total_recovered": 5048,
        "total_tests": null,
        "uid": 226
    },
    {
        "cases": 3209,
        "country": "Greece",
        "deaths": 176,
        "iso2": "GR",
        "iso3": "GRC",
        "last_updated_at": "2020-12-10T18:01:15.881Z",
        "loc": {
            "coordinates": [
                21.8243,
                39.0742
            ],
            "type": "Point"
        },
        "population": 10423056,
        "recovered": 0,
        "sources": [
            "imedd"
        ],
        "tests": 62786,
        "total_active": 19571,
        "total_cases": 121253,
        "total_critical": 571,
        "total_deaths": 3370,
        "total_recovered": 98312,
        "total_tests": 2847016,
        "uid": 300
    },
    (...)
]
```

###### Greece Total Data

```json
// GET /total/greece
[
    {
        "cases": 634,
        "deaths": 0,
        "geo_unit": "Macedonia",
        "last_updated_at": "2020-12-10T18:01:10.532Z",
        "loc": {
            "coordinates": [
                22.9444191,
                40.6400629
            ],
            "type": "Point"
        },
        "population": 1110551,
        "recovered": 0,
        "region": "Thessaloniki",
        "sources": [
            "imedd"
        ],
        "state": "Central Macedonia",
        "total_active": null,
        "total_cases": 26145,
        "total_critical": null,
        "total_deaths": 184,
        "total_recovered": null,
        "uid": "EL122"
    },
    (...)
]
```

###### Vaccines (Greece Only) Total Data (Beta)

```json
// GET /total/vaccines/greece/all/2020-12-27
[
    {
        "daily_dose_1": 176, // as provided by govgr
        "daily_dose_2": 143, // as provided by govgr
        "day_diff": 0, // as provided by govgr
        "day_total": 319, // as provided by govgr
        "from": "2020-12-27T02:00:00+02:00",
        "geo_unit": "Aegean",
        "last_updated_at": "2021-03-08T14:07:00.68+02:00",
        "loc": {
            "coordinates": [
                25.3268288,
                37.444458000000004
            ],
            "type": "Point"
        },
        "new_total_distinct_persons": 176,
        "new_total_vaccinations": 319,
        "population": 10134,
        "region": "Mykonos",
        "sources": [
            "govgr"
        ],
        "state": "South Aegean",
        "to": "2021-03-06T02:00:00+02:00",
        "total_distinct_persons": 176, // as provided by govgr
        "total_dose_1": 176, // as provided by govgr
        "total_dose_2": 143, // as provided by govgr
        "total_vaccinations": 319, // as provided by govgr
        "uid": "PE1208"
    },
    (...)
]
```

###### Global Aggragated Data (Beta)

The `agg` endpoint is still in active development and may change without further notice.

```json
// GET /agg/global/all/all/2020-11-22
[
    {
        "active": [62119, 63422, 65452, 67516, 69435, 21151, 22777, 23872,  24831, 26919, 29015, 29015],
        "cases": [91619, 93006, 95137, 97288, 99306, 101287, 103034, 104227, 105271, 107470, 109655, 109655],
        "country": "Greece",
        "critical": [540, 549, 562, 597, 608, 607, 606, 607, 600, 596, 613, 0],
        "deaths": [1630, 1714, 1815, 1902, 2001, 2102, 2223, 2321, 2406, 2517, 2606, 2606],
        "from": "2020-11-22T02:00:00+02:00",
        "iso2": "GR",
        "iso3": "GRC",
        "last_updated_at": "2020-12-03T14:35:09.394+02:00",
        "loc": {
            "coordinates": [
                21.8243,
                39.0742
            ],
            "type": "Point"
        },
        "new_cases": [1498, 1387, 2131, 2151, 2018, 1981, 1747, 1193, 1044, 2199, 2185, 0],
        "new_deaths": [103, 84, 101, 87, 99, 101, 121, 98, 85, 111, 89, 0],
        "population": 10423056,
        "recovered": [27870, 27870, 27870, 27870, 27870, 78034, 78034, 78034, 78034, 78034, 78034, 78034],
        "sources": [
            "imedd"
        ],
        "to": "2020-12-03T02:00:00+02:00",
        "uid": 300
    },
    (...)
]
```

###### Greece Aggregated Data (Beta)

```json
// GET /agg/greece/all/all/2020-11-22
[
    {
        "active": [],
        "cases": [162, 167, 170, 182, 189, 201, 204, 205, 211, 215, 220, 220],
        "critical": [],
        "deaths": [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        "from": "2020-11-22T02:00:00+02:00",
        "geo_unit": "Epirus",
        "last_updated_at": "2020-12-03T14:35:03.245+02:00",
        "loc": {
            "coordinates": [
                20.987683899999997,
                39.1582421
            ],
            "type": "Point"
        },
        "new_cases": [8, 5, 3, 12, 7, 12, 3, 1, 6, 4, 5, 5],
        "new_deaths": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        "population": 67877,
        "recovered": [],
        "region": "Arta",
        "sources": [
            "imedd"
        ],
        "state": "Epirus",
        "to": "2020-12-03T02:00:00+02:00",
        "uid": "EL211"
    },
    (...)
]
```

###### Vaccines (Greece Only) Aggregated Data (Beta)

```json
// GET /agg/vaccines/greece/all/all/2020-11-22
[
    {
        "daily_dose_1": [0, 0], // as provided by govgr
        "daily_dose_2": [0, 0], // as provided by govgr
        "day_diff": [0, 0], // as provided by govgr
        "day_total": [0, 0], // as provided by govgr
        "from": "2021-01-13T02:00:00+02:00",
        "geo_unit": "Aegean",
        "last_updated_at": "2021-01-15T12:18:34.752+02:00",
        "loc": {
            "coordinates": [
                25.125567999999998,
                37.0651291
            ],
            "type": "Point"
        },
        "new_total_distinct_persons": [0, 0],
        "new_total_vaccinations": [0, 0],
        "population": 14926,
        "region": "Paros",
        "sources": [
            "govgr"
        ],
        "state": "South Aegean",
        "to": "2021-01-14T02:00:00+02:00",
        "total_distinct_persons": [0, 0], // as provided by govgr
        "total_dose_1": [0, 0], // as provided by govgr
        "total_dose_2": [0, 0], // as provided by govgr
        "total_vaccinations": [0, 0], // as provided by govgr
        "uid": "PE1210"
    },
    (...)
]
```

## Endpoints

All endpoints accept various parameters. We store country level information on `global` collection and region level information on `greece` collection. 

Country and region parameter refer to country specific iso3 code or nuts codes, for global and greece collections accordingly. Accepted `:country` and `:region` params are either `all` to get data for all countries / regions, or iso3 country codes / nuts codes to get specific country or regional data. You can refer to this file [countries-mapping-jhu-wom.csv](https://github.com/cvcio/covid-19-automation/blob/main/data/countries-mapping-jhu-wom.csv), that will help you understand how we map [JHU](https://github.com/CSSEGISandData/COVID-19) ~~and [WoldOMeter](https://www.worldometers.info/coronavirus/)~~ data (column `iso3`) and to this file [region-mapping-imedd.csv](https://github.com/cvcio/covid-19-automation/blob/main/data/region-mapping-imedd.csv) for mapping data from [iMedD](https://github.com/iMEdD-Lab/open-data) (column `uid`, and `"PE"+areaid` for vaccines).

Accepted `:keys` are either `all`, which will retrieve all the defaults, or document specific keys, single or comma seperated. This parameter is not included in the aggregated data endpoint.

Finally, `:from` and `:to` parameters will retrieve data in the specified date range in `YYYY-MM-DD` format. If no `:from` parameter  provided, we will only return tha last date. If no `:to` parameter  provided, we will return up-to current date.

Please, if you think that we are missing some countries, or any other data related issues, open an issue on [COVID&ndash;19 automation](https://github.com/cvcio/covid-19-automation) repository.

Accepted keys, available for all countries are:

- **all**: default, will return all available
- **cases**: cumulative cases
- **deaths**: cumulative deaths
- **recovered**: cumulative recovered cases 
- **active**: daily active cases (cases - deaths - recovered)
- **critical**: daily critical cases available only for current date
- **tests**: daily tests available only for current date
- **new_cases**: daily cases
- **new_deaths**: daily deaths
- **new_recovered**: daily recovered cases
- **case_fatality_ratio**: daily case fatality ratio ((death / cases) * 100)
- **incidence_rate**: daily incidence ratio per 100K population ((cases * 100000) / population)

and for Greece (country:grc) only:

- **tests**: cumulative total tests
- **tests_rtpcr**: cumulative rt-pcr tests
- **tests_rapid**: cumulative rapid tests
- **new_tests_rtpcr**: daily rt-pcr tests
- **new_tests_rapid**: daily rapid tests
- **new_tests**: daily total tests

For regioanal data (Greece) available keys are:

- **all**: default, will return all available
- **cases**: cumulative cases
- **deaths**: cumulative deaths
- **new_cases**: daily cases
- **new_deaths**: daily deaths
- **case_fatality_ratio**: daily case fatality ratio ((death / cases) * 100)
- **incidence_rate**: daily incidence ratio per 100K population ((cases * 100000) / population)

Vaccines related data (Greece Only), available keys are:

- **all**: default, will return all available
- **total_distinct_persons**: cumulative distinct persons vaccinated (as provided by govgr)
- **total_vaccinations**: cumulative vaccinations (as provided by govgr)
- **total_dose_1**: cumulative vaccinations / dose 1 (as provided by govgr)
- **total_dose_2**: cumulative vaccinations / dose 2 (as provided by govgr)
- **day_total**: daily vaccinations (as provided by govgr)
- **daily_dose_1**: daily vaccinations / dose 1 (as provided by govgr)
- **daily_dose_2**: daily vaccinations / dose 2 (as provided by govgr)
- **day_diff**: daily difference (as provided by govgr)
- **new_total_distinct_persons**: daily distinct persons vaccinated
- **new_total_vaccinations**: daily vaccinations

###### Raw Global Data

```bash
GET /global/:country/:keys/:from/:to

# ex. get all data, for all countries, from the begining
# of the pandemic.
curl -XGET https://covid.imedd.org/global/all/all/2020-01-01

# ex. get all data, for all countries just for today
# in this scenario :country and :keys are optional
# the following requests will return the same response
curl -XGET https://covid.imedd.org/global
curl -XGET https://covid.imedd.org/global/all
curl -XGET https://covid.imedd.org/global/all/all

# ex. get only the new_cases key for Greece
curl -XGET https://covid.imedd.org/global/grc/new_cases

# ex. get only the new_cases and cases keys for all countries
# just for today
curl -XGET https://covid.imedd.org/global/all/new_cases,cases
```

###### Raw Greece Data

```bash
GET /greece/:region/:keys/:from/:to

# ex. get all data, for all regions in greece, from the begining 
# of the pandemic.
curl -XGET https://covid.imedd.org/greece/all/all/2020-01-01

# get all cases for Thessaloniki region between Oct and Nov
curl -XGET https://covid.imedd.org/greece/EL122/cases/2020-10-01/2020-11-31
```

###### Raw Vaccines (Greece Only) Data

```bash
GET /vaccines/greece/:region/:keys/:from/:to

# ex. get all data, for all regions in greece, from 2020-12-27
curl -XGET https://covid.imedd.org/vaccines/greece/all/all/2020-12-27

# get all cases for Thessaloniki region from the begining until the end of the year
curl -XGET https://covid.imedd.org/vaccines/greece/PE202/cases/2020-12-27/2020-12-31
```

###### Global Total Data

```bash
GET /total/global/:country/:from/:to

# ex. get total recovered cases for all countries,
# from the begining of the pandemic.
curl -XGET https://covid.imedd.org/total/global/all/2020-10-01
```

###### Greece Total Data

```bash
GET /total/greece/:region/:from/:to

# ex. get total imported (detected at the entry points) cases just for today
curl -XGET https://covid.imedd.org/total/greece/EL001
```

###### Vaccines (Greece Only) Total Data

```bash
GET /total/vaccines/greece/:region/:from/:to

# ex. get total Thessaloniki region cases just for today
curl -XGET https://covid.imedd.org/total/greece/PE202
```

###### Global Aggregated Data (Beta)

```bash
GET /agg/global/:country/:keys/:from/:to

# ex. get all aggregated data for Greece, from
# the begining of the pandemic
curl -XGET https://covid.imedd.org/agg/global/GRC/all/2020-01-01
```

###### Greece Aggregated Data (Beta)

```bash
GET /agg/greece/:region/:keys/:from/:to

# ex. get all aggregated data for Attica region, from
# the begining of the pandemic
curl -XGET https://covid.imedd.org/agg/greece/EL300/all/2020-01-01
```

###### Vaccines (Greece Only) Aggregated Data (Beta)

```bash
GET /agg/vaccines/greece/:region/:keys/:from/:to

# ex. get all aggregated data for Thessaloniki region, from
# the begining of the pandemic
curl -XGET https://covid.imedd.org/agg/vaccines/greece/PE202/all/2020-01-01
```

*Note: the `total` endpoint doesn't include the `:keys` parameter*

## Rate Limiting

We introduced rate limiting from the begining as it is a critical aspect of the API's performance, and/or prevent abuse by automated system and humans. The global rate limit is set to **300 requests per minute**, but this may change without direct notice. We plan to introduce a token based authentication to bypass the limiting in the near future.


## Related Repositories

- [COVID&ndash;19 Open Data](https://github.com/iMEdD-Lab/open-data) (iMEdD)
- [COVID&ndash;19 Automation](https://github.com/cvcio/covid-19-automation)
- [COVID&ndash;19 API](https://github.com/cvcio/covid-19-api)
- [COVID&ndash;19 Application](https://github.com/cvcio/covid-19)

## Contributors

- Ilias Dimos ([@dosko64](https://github.com/dosko64))
- Dimitris Papaevagelou ([@andefined](https://github.com/andefined)).
