# About

Datasets and charts created by [iMEdD Lab](https://www.imedd.org/imedd-lab/) as part of the development of [iMEdD Lab's web application that tracks the spread of COVID-19 in Greece and around the world](https://lab.imedd.org/covid19/?lang=en). 


## Folder named "charts"

Interactive charts and maps that are available on the [statistical analysis page](https://lab.imedd.org/covid19/stats?lang=en) of the web application are available here in .json files. They are updated every two hours. The charts are built with [Plotly Python Open Source Graphing Library](https://plotly.com/python/). See more at [open-data/scripts/COVID19](https://github.com/iMEdD-Lab/open-data/tree/master/scripts/COVID-19).


## Datasets

### 1. alerts.csv
Alert messages go here. 

### 2. countriesMapping.csv & countries_names.csv
Mapping countries names deriving from different sources. ISO alpha-2 and ISO alpha-3 country codes are included.

### 3. greece.csv (archived)
Cumulative data about COVID-19 cases, deaths, critically ill, and recovered patients by prefecture/regional unit in Greece. Data refer to figures known at the time this specific CSV file was published. Last publication date: June 30, 2020. 

#### Data Sources
- The [Hellenic National Public Health Organisation (EODY)](https://eody.gov.gr/) and the [Ministry of Health](https://www.moh.gov.gr/) are the main sources of data that have been released through:
    - Announcements and transcripts of the press briefings published by [EODY](https://eody.gov.gr/category/anakoinoseis/) and the [Ministry of Health](https://www.moh.gov.gr/articles/ministry/grafeio-typoy/press-releases).
    - [Reports](https://eody.gov.gr/epidimiologika-statistika-dedomena/ektheseis-covid-19/) published in PDF files by EODY.
- Deaths data have been retrieved from fact-checked news reports, published in the Greek Press, since neither EODY nor the Ministry of Health announce official data about the geographical location of each death.

#### Notes
- The "pop11" column holds the data on the resident population based on the 2011 census, as provided by the [Hellenic Statistical Authority](https://www.statistics.gr/el/statistics/-/publication/SAM03/-).
- Figures about cases and deaths by prefecture/regional unit in Greece have still been maintained in greece_cases.csv and greece_deaths.csv respectively. Please find more information on these below.

### 4. greeceTimeline.csv
Data about COVID-19 in Greece by date, from February 26, 2020, when the first case was confirmed in the country, onwards.<br/>The dataset is updated automatically. Updates have been published at least once a day. The major update usually happens at 18:00 (EEST).

The values in the "Status" column correspond to different metrics. Find below what those values mean. 
- <b>cases</b>: new confirmed cases announced on the date of reference; read in Notes below about data corrections that are included here.
- <b>cruise_ship_ElVen</b>: new confirmed cases on board announced on the date of reference; refers to the "Eleftherios Venizelos" ferryboat. Said cases on board are also included in the number of cases on the date of reference. 
- <b>Ritsona</b>: new confirmed cases at the Ritsona refugee camp announced on the date of reference. Said cases are also included in the number of cases on the date of reference.
- <b>deaths</b>: new deaths happened on the date of reference; read in Notes below why some values might differ from the number of new deaths announced by the authorities on the relevant date. 
- <b>recovered</b>: cumulative data about patients recovered by the date of reference 
- <b>hospitalized</b>: number of patients hospitalized on the date of reference 
- <b>intensive_care</b>: number of patients hospitalized in intensive care units on the date of reference 
- <b>intubated</b>: number of intubated patients on the date of reference
- <b>total_tests</b>: cumulative testing data by the date of reference 
- <b>total cases</b>: total number of cases announced by the date of reference 

#### Data Sources
EODY and the Ministry of Health are the sources of data that have been released through:
- Announcements and transcripts of the press briefings published by [EODY](https://eody.gov.gr/category/anakoinoseis/) and the [Ministry of Health](https://www.moh.gov.gr/articles/ministry/grafeio-typoy/press-releases)
- [Reports](https://eody.gov.gr/epidimiologika-statistika-dedomena/ektheseis-covid-19/) published in PDF files by EODY

#### Notes
- <b>Missing values</b>: NaN values mean that figures have not been announced by the authorities for the date of reference.<br/> 
- <b>Data correction</b>: On specific dates, the number of "<b><i>cases</i></b>" might be different than the one announced by EODY that day. That means the number of new confirmed cases has been corrected, so that it can give us the total number of cases announced on these specific dates, when being added to the number of total cases announced the previous day.<br/>This happens because EODY corrects duplicate positive results of previous days, but fails to disclose which days those duplicates refer to. For instance, let’s say that on Day 1 we have 10 total cases. On Day 2, we have 5 new cases, which means that EODY should announce 15 total cases. However, the total number of cases announced on Day 2 is 13. This means that there were 2 duplicate cases on Day 1, which are corrected on Day 2. 3 cases and 15 total cases will be recorded in our dataset on Day 2. Indicatively, corrected numbers of cases are presented in greeceTimeline.csv on May 22, May 27, May 29, May 30, June 1, June 2, June 10, June 11, June 16, June 23, June 25, June 29, June 30.<br/>If you wish to use the exact number of new cases officially announced each day, run through the pdfsDataFrame.csv for information extracted from the [official reports published in PDF files by EODY](https://eody.gov.gr/epidimiologika-statistika-dedomena/ektheseis-covid-19/). 
- <b>Deaths</b>: As mentioned above, the value "<b><i>deaths</i></b>" in the "Status" column corresponds to new deaths occurred on the calendar date of reference. That means the number of deaths is sometimes different than the one announced by EODY, or the Ministry of Health. This happens because authorities announce the daily number of new deaths that occurred in their 24-hour reporting window, which is 15:00 - 15:00 (EEST) and 18:00 - 18:00 (EEST) for EODY and the Ministry of Health respectively.<br/>If you wish to use the exact number of new deaths announced each day, run through the pdfsDataFrame.csv for information extracted from the [official reports published in PDF files by EODY](https://eody.gov.gr/epidimiologika-statistika-dedomena/ektheseis-covid-19/).

### 5. greece_cases.csv
Cumulative data about cases by prefecture/regional unit in Greece and by date of announcement. The value "<b><i>Απροσδιόριστος</b></i>" (<i>Unknown</i>) in the "county" column means that the perfecture/regional unit has not been announced by the authorities for the relevant number of cumulative cases on the date of reference. The dataset is updated automatically.

#### Data Sources
EODY and the Ministry of Health are the sources of data that have been released through:
- Announcements and transcripts of the press briefings published by [EODY](https://eody.gov.gr/category/anakoinoseis/) and the [Ministry of Health](https://www.moh.gov.gr/articles/ministry/grafeio-typoy/press-releases)
- [Reports](https://eody.gov.gr/epidimiologika-statistika-dedomena/ektheseis-covid-19/) published in PDF files by EODY

#### Notes
- The "pop11" column holds the data on the resident population based on the 2011 census, as provided by the [Hellenic Statistical Authority](https://www.statistics.gr/el/statistics/-/publication/SAM03/-).

### 6. greece_deaths.csv
Cumulative data about deaths by prefecture/regional unit in Greece and by date of the incident. The value "<b><i>Απροσδιόριστος</b></i>" (<i>Unknown</i>) in the "county" column means that the prefecture/regional unit has not been known for the relevant number of cumulative deaths on the date of reference. 

#### Data Sources
Since neither EODY nor the Ministry of Health announce official data about the geographical location of each death, this dataset has been compiled by fact-checked news reports published in the Greek press. 

#### Notes
- As mentioned above, daily cumulative deaths data corresponds to deaths that occurred by the calendar date of reference. That means the sum of deaths by prefecture/regional unit on specific dates might be different than the total number of deaths announced by EODY, or the Ministry of Health, on the same date. This happens because authorities announce the total number of deaths as a result of the number of new deaths that occurred in their 24-hour reporting window, which is 15:00 - 15:00 (EEST) and 18:00 - 18:00 (EEST) for EODY and the Ministry of Health respectively.<br/>If you wish to use the exact number of new and total deaths officially announced each day, run through the pdfsDataFrame.csv for information extracted from the [official reports published in PDF files by EODY](https://eody.gov.gr/epidimiologika-statistika-dedomena/ektheseis-covid-19/).
- The "pop11" column holds the data on the resident population based on the 2011 census, as provided by the [Hellenic Statistical Authority](https://www.statistics.gr/el/statistics/-/publication/SAM03/-).

### 7. pdfsDataFrame.csv
Content retrieved and data extracted from the reports published in PDF files by [EODY](https://eody.gov.gr/epidimiologika-statistika-dedomena/ektheseis-covid-19/). The dataset is updated automatically on a daily basis. The PDF files are read with the [Apache TIKA library](https://tika.apache.org/) and the program which extracts the data is written in Python. 

### 8. regions_greece.csv
Cumulative data on cases, deaths, critically ill patients (intubated), and recovered patients by region in Greece. The value "<b><i>No Location Provided</b></i>" in the "district_EN" column means that the region has not been known for the relevant numbers of cases, of deaths, of critically ill patients, and of people who recovered. The dataset is updated automatically. Major data updates happen daily, usually between 18:00 and 19:00 (EEST); please read further infromation in Notes below. Once news reports on a new death are cross-checked, the dataset is also updated.

#### Data Sources
- The [Hellenic National Public Health Organisation (EODY)](https://eody.gov.gr/) is the main source of data that have been released through:
    - [covid19.gov.gr](https://covid19.gov.gr/covid19-live-analytics/)
    - Announcements published by [EODY](https://eody.gov.gr/category/anakoinoseis/) and the [Ministry of Health](https://www.moh.gov.gr/articles/ministry/grafeio-typoy/press-releases).
    - [Reports](https://eody.gov.gr/epidimiologika-statistika-dedomena/ektheseis-covid-19/) published in PDF files by EODY.
- Deaths data have been retrieved from fact-checked news reports, published in the Greek Press, since neither EODY nor the Ministry of Health announce official data about the geographical location of each death.
    
#### Notes
- <b>Data updates</b>: Usually, the dataset is updated at 18:00 (EEST), once EODY announcement is out. Then, the number of new cases announced is added to correspond to "No Location Provided". By 19:00 (EEST), as soon as covid19.gov.gr updates its dashboard, the dataset is updated again and new cases are added to their respective region. 
- The "pop11" column holds the data on the resident population based on the 2011 census, as provided by the [Hellenic Statistical Authority](https://www.statistics.gr/el/statistics/-/publication/SAM03/-).

### 9. regions_greece_cases.csv
Cumulative data about cases by region in Greece and by date of announcement. The value "<b><i>No Location Provided</i></b>" in the "district_EN" column means that the region has not been announced by the authorities for the relevant number of cases on the date of reference. The data is updated automatically. 

#### Data Sources
- The [Hellenic National Public Health Organisation (EODY)](https://eody.gov.gr/) is the main source of data that have been released through:
    - [covid19.gov.gr](https://covid19.gov.gr/covid19-live-analytics/) (data from April 23, 2020, onwards)
    - Announcements published by [EODY](https://eody.gov.gr/category/anakoinoseis/) and the [Ministry of Health](https://www.moh.gov.gr/articles/ministry/grafeio-typoy/press-releases)(data by April 22, 2020)
    - [Reports](https://eody.gov.gr/epidimiologika-statistika-dedomena/ektheseis-covid-19/) published in PDF files by EODY (data by April 22, 2020)
- The "pop11" column holds the data on the resident population based on the 2011 census, as provided by the [Hellenic Statistical Authority](https://www.statistics.gr/el/statistics/-/publication/SAM03/-).

### 10. regions_greece_deaths.csv
Cumulative data about deaths by region in Greece and by date of the incident. The value "<b><i>No Location Provided</b></i>" in the "district_EN" column means that the region has not been known for the relevant number of cases on the date of reference. 

#### Data Sources
Since neither EODY nor the Ministry of Health announce official data about the geographical location of each death, this dataset has been compiled by fact-checked news reports published in the Greek press. 

#### Notes
- As mentioned above, daily cumulative deaths data corresponds to deaths that occurred by the calendar date of reference. That means the sum of deaths by prefecture/regional unit on specific dates might be different than the total number of deaths announced by EODY, or the Ministry of Health, on the same date. This happens because authorities announce the total number of deaths as a result of the number of new deaths that occurred in their 24-hour reporting window, which is 15:00 - 15:00 (EEST) and 18:00 - 18:00 (EEST) for EODY and the Ministry of Health respectively.<br/>If you wish to use the exact number of new and total deaths announced each day, run through the pdfsDataFrame.csv for information extracted from the [official reports published in PDF files by EODY](https://eody.gov.gr/epidimiologika-statistika-dedomena/ektheseis-covid-19/).
- The "pop11" column holds the data on the resident population based on the 2011 census, as provided by the [Hellenic Statistical Authority](https://www.statistics.gr/el/statistics/-/publication/SAM03/-).

### 11. wom_data.csv
International data retrieved from the [Worldometer](https://www.worldometers.info/coronavirus/). 
