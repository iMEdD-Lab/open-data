# About

Datasets and charts created by [iMEdD Lab](https://www.imedd.org/imedd-lab/) as part of the development of [iMEdD Lab's web application that tracks the spread of COVID-19 in Greece and around the world](https://lab.imedd.org/covid19/?lang=en). The detailed methodology for the creation of the application has been published on iMEdD Lab, under the title ["How the application monitoring the spread of the disease was created"](https://lab.imedd.org/en/how-application-monitoring-spread-covid19/).

## Folder named "ARCHIVED"
Contains the datasets that we aren't updating any longer. 

## Folder named "charts"

Interactive charts and maps that are available on the [statistical analysis page](https://lab.imedd.org/covid19/stats?lang=en) of the web application are available here in .json files. They are updated every two hours. The charts are built with [Plotly Python Open Source Graphing Library](https://plotly.com/python/). See more at [open-data/scripts/COVID19](https://github.com/iMEdD-Lab/open-data/tree/master/scripts/COVID-19).


## Datasets

### 1. alerts.csv (ARCHIVED)
Alert messages go here. 

### 2. countriesMapping.csv & countries_names.csv
Mapping countries names deriving from different sources. ISO alpha-2 and ISO alpha-3 country codes are included.

### 3. greece.csv (ARCHIVED)
Cumulative data about COVID-19 cases, deaths, critically ill, and recovered patients by prefecture/regional unit in Greece. Data refer to figures known at the time this specific CSV file was published. Last publication date: June 30, 2020. Figures about cases and deaths by prefecture/regional unit in Greece have still been maintained in greece_v2.csv, greece_cases_v2.csv and greece_deaths_v2.csv respectively. Please find more information on these below.

#### Data Sources
- The [Hellenic National Public Health Organisation (EODY)](https://eody.gov.gr/) and the [Ministry of Health](https://www.moh.gov.gr/) are the main sources of data that have been released through:
    - Announcements and transcripts of the press briefings published by [EODY](https://eody.gov.gr/category/anakoinoseis/) and the [Ministry of Health](https://www.moh.gov.gr/articles/ministry/grafeio-typoy/press-releases).
    - [Reports](https://eody.gov.gr/epidimiologika-statistika-dedomena/ektheseis-covid-19/) published in PDF files by EODY.
- Deaths data have been retrieved from fact-checked news reports, published in the Greek Press, since neither EODY nor the Ministry of Health announce official data about the geographical location of each death.

#### Notes
- The "pop11" column holds the data on the resident population based on the 2011 census, as provided by the [Hellenic Statistical Authority](https://www.statistics.gr/el/statistics/-/publication/SAM03/-).

### 4. greece_v2.csv (ARCHIVED)
Cumulative data about COVID-19 cases, deaths, critically ill, and recovered patients by prefecture/regional unit in Greece. Data refer to figures known at the time this specific CSV file was published. The value "<b><i>No Location Provided</b></i>" in the "county_en" column means that the prefecture/regional unit has not been known for the relevant estimated number of cases, of deaths, of critically ill patients, and of people who recovered. 

#### Data Sources
- The [Hellenic National Public Health Organisation (EODY)](https://eody.gov.gr/) and the [Ministry of Health](https://www.moh.gov.gr/) are the main sources of data that have been released through:
    - Announcements and transcripts of the press briefings published by [EODY](https://eody.gov.gr/category/anakoinoseis/) and the [Ministry of Health](https://www.moh.gov.gr/articles/ministry/grafeio-typoy/press-releases).
    - [Reports](https://eody.gov.gr/epidimiologika-statistika-dedomena/ektheseis-covid-19/) published in PDF files by EODY.
    - Daily announcements to the Press about the geographical distribution of new cases reported daily, from June 15 2020 onwards. 
- Deaths data have been retrieved from fact-checked news reports, published in the Greek Press, since neither EODY nor the Ministry of Health announce official data about the geographical location of each death.

#### Notes
- The "pop11" column holds the data on the resident population based on the 2011 census, as provided by the [Hellenic Statistical Authority](https://www.statistics.gr/el/statistics/-/publication/SAM03/-).
- <b>Cases with no location provided</b>: Corresponds to the estimated number of cumulative cases with no location provided at the time this specific dataset was published. Explanation about the estimation of this number is provided in the "Notes" section for the greece_cases_v2.csv file. 

### 5. greeceTimeline.csv
Data about COVID-19 in Greece by date, from February 26, 2020, when the first case was confirmed in the country, onwards.<br/>The dataset is updated automatically. Updates have been published at least once a day. The major update usually happens at 18:00 (EEST).

The values in the "Status" column correspond to different metrics. Find below what those values mean. 
- <b>cases</b>: new confirmed cases announced on the date of reference; read in Notes below about data corrections that are included here.
- <b>deaths</b>: new deaths happened on the date of reference; read in Notes below why some values might differ from the number of new deaths announced by the authorities on the relevant date. 
- <b>deaths_cum</b>: cummulative number of deaths deaths.
- <b>hospitalized</b>: total number of patients hospitalized on the date of reference. 
- <b>hospital_admissions</b>: new daily admissions. Data by https://covid19.gov.gr/covid19-live-analytics/
- <b>hospital_discharges</b>: new daily hospital discharges. Data by https://covid19.gov.gr/covid19-live-analytics/
- <b>intensive_care</b>: number of patients hospitalized in intensive care units on the date of reference 
- <b>icu_discharges</b>: total number of icu discharges per day.
- <b>new_icu_discharges</b>: difference of daily total number of discharges.
- <b>intubated</b>: number of intubated patients on the date of reference
- <b>intubated_unvac</b>: number of intubated patients who are unvaccinated
- <b>intubated_unvac</b>: number of intubated patients who are vaccinated
- <b>icu_occupancy</b>: percentage of icus occupied
- <b>beds_occupancy</b>: percentage of hospital beds occupied
- <b>cumulative_rtpcr_tests_raw</b>: cumulative pcr tests by the date of reference 
- <b>estimated_new_rtpcr_tests</b>: new pcr tests by the date of reference 
- <b>cumulative_rapid_tests_raw</b>: cumulative Rapid Ag testing data by the date of reference 
- <b>esitmated_new_rapid_tests</b>: new Rapid Ag testing data by the date of reference 
- <b>estimated_new_total_tests</b>: estimated number of daily tests in total, including laboratory testing samples and Rapid Ag tests. We estimate the number of daily tests by calculating the difference between the sum of "estimated_new_rtpcr_tests" (laboratory) and "esitmated_new_rapid_tests" (Rapid Ag) each day and the said sum the previous day. On specific dates, authorities didn't announced the total number of tests by then. When that happens, we divide the calculated difference between latest total tests announced and the previous total number of tests known by the number of days in between. This way, we fill missing values with the daily mean of total tests within specific time periods.
- <b>total cases</b>: total number of cases announced by the date of reference 

#### Data Sources
EODY and the Ministry of Health are the sources of data that have been released through:
- Announcements and transcripts of the press briefings published by [EODY](https://eody.gov.gr/category/anakoinoseis/) and the [Ministry of Health](https://www.moh.gov.gr/articles/ministry/grafeio-typoy/press-releases)
- [Reports](https://eody.gov.gr/epidimiologika-statistika-dedomena/ektheseis-covid-19/) published in PDF files by EODY
- Official covid data dashboard https://covid19.gov.gr/covid19-live-analytics/

#### Notes
- <b>Missing values</b>: NaN values mean that figures have not been announced by the authorities for the date of reference.<br/> 
- <b>Data correction</b>: On specific dates, the number of "<b><i>cases</i></b>" might be different than the one announced by EODY that day. That means the number of new confirmed cases has been corrected, so that it can give us the total number of cases announced on these specific dates, when being added to the number of total cases announced the previous day.<br/>This happens because EODY corrects duplicate positive results of previous days, but fails to disclose which days those duplicates refer to. For instance, let’s say that on Day 1 we have 10 total cases. On Day 2, we have 5 new cases, which means that EODY should announce 15 total cases. However, the total number of cases announced on Day 2 is 13. This means that there were 2 duplicate cases on Day 1, which are corrected on Day 2. 3 cases and 15 total cases will be recorded in our dataset on Day 2. Indicatively, corrected numbers of cases are presented in greeceTimeline.csv on May 22, May 27, May 29, May 30, June 1, June 2, June 10, June 11, June 16, June 23, June 25, June 29, June 30, July 2, July 5.<br/>If you wish to use the exact number of new cases officially announced each day, run through the pdfsDataFrame.csv for information extracted from the [official reports published in PDF files by EODY](https://eody.gov.gr/epidimiologika-statistika-dedomena/ektheseis-covid-19/). 
- <b>Deaths</b>: As mentioned above, the value "<b><i>deaths</i></b>" in the "Status" column corresponds to new deaths occurred on the calendar date of reference. That means the number of deaths is sometimes different than the one announced by EODY, or the Ministry of Health. This happens because authorities announce the daily number of new deaths that occurred in their 24-hour reporting window, which is 15:00 - 15:00 (EEST) and 18:00 - 18:00 (EEST) for EODY and the Ministry of Health respectively.<br>Also, EODY sometimes includes in the total number of deaths in its daily report losses that occurred at an earlier time, without specifying to which dates the deaths that are counted retrospectively correspond. In this case, these losses are "attributed" to the day of announcement in the dataset. Then, the new daily deaths in the dataset appear to be more than the new daily deaths announced on the same day by EODY. For example, this is the case on June 2021, 12, 14, 24, 28.<br/>If you wish to use the exact number of new deaths announced each day, run through the pdfsDataFrame.csv for information extracted from the [official reports published in PDF files by EODY](https://eody.gov.gr/epidimiologika-statistika-dedomena/ektheseis-covid-19/).

### 6. greece_cases.csv (ARCHIVED)
Cumulative data about cases by prefecture/regional unit in Greece and by date of announcement. The value "<b><i>Απροσδιόριστος</b></i>" (<i>Unknown</i>) in the "county" column means that the perfecture/regional unit has not been announced by the authorities for the relevant number of cumulative cases on the date of reference. The dataset is archived. Relevant figures about cases have still been maintained in greece_cases_v2.csv. Please find more information on this below.

#### Data Sources
EODY and the Ministry of Health are the sources of data that have been released through:
- Announcements and transcripts of the press briefings published by [EODY](https://eody.gov.gr/category/anakoinoseis/) and the [Ministry of Health](https://www.moh.gov.gr/articles/ministry/grafeio-typoy/press-releases)
- [Reports](https://eody.gov.gr/epidimiologika-statistika-dedomena/ektheseis-covid-19/) published in PDF files by EODY

#### Notes
- The "pop11" column holds the data on the resident population based on the 2011 census, as provided by the [Hellenic Statistical Authority](https://www.statistics.gr/el/statistics/-/publication/SAM03/-).

### 7. greece_cases_v2.csv
Cumulative data about cases by prefecture/regional unit in Greece and by date of announcement. The value "<b><i>Χωρίς Γεωγραφικό Προσδιορισμό</b></i>" in the "county" column means that the perfecture/regional unit has not been announced by the authorities for the relevant estimated number of cumulative cases on the date of reference. Please read more about this estimation in the "Notes" section below. The dataset is being updated on a daily basis.

#### Data Sources
EODY and the Ministry of Health are the sources of data that have been released through:
- Announcements and transcripts of the press briefings published by [EODY](https://eody.gov.gr/category/anakoinoseis/) and the [Ministry of Health](https://www.moh.gov.gr/articles/ministry/grafeio-typoy/press-releases)
- [Reports](https://eody.gov.gr/epidimiologika-statistika-dedomena/ektheseis-covid-19/) published in PDF files by EODY
- Daily announcements to the Press about the geographical distribution of new cases reported daily, from June 15 2020 onwards. 

#### Notes
- The "pop11" column holds the data on the resident population based on the 2011 census, as provided by the [Hellenic Statistical Authority](https://www.statistics.gr/el/statistics/-/publication/SAM03/-).
- <b>Estimated number of cumulative cases with no location provided</b>:<br>Authories were announcing cumulative numbers of cases by prefecture/regional unit from time to time. Those numbers are maintained in our dataset up to June 14 2020, when no location is provided for 647 cumulative cases in our dataset. Authorities haven't released information about cumulative cases broken down by prefecture/regional unit for couple of months.<br>However, new confirmed daily cases broken down by regional unit and in Attica region have been being released since June 15, 2020. We maintain those records and we add new reported cases in each prefecture/regional unit to those of the previous day each time in the same prefecture/regional unit. That way, this dataset, which provides data on cumulative cases by prefecture/regional unit and by date, has been being maintained.<br>The number of cases with no location provided is initially estimated by adding the number of daily cases for which location is under investigation, as given by EODY from June 15 2020 onwards, to the total number of cases with no location announced up to the previous date. Duplicates are substracted from that said sum.<br>What duplicates are: As mentioned above (see greeceTimeline.csv, "Notes" section), on specific dates, the total number of confirmed cases is smaller than the one expected, if someone adds the number of new cases announced by EODY on those dates to the total number of cases announced the previous day each time. This happens because EODY corrects duplicate positive results of previous days. However, EODY does not disclose which dates and which locations those duplicates refer to. Therefore, said duplicates are substracted from the sum of older and daily cases with no location provided in our greece_cases_v2.csv dataset.<br>To sum up, the daily number of cumulative cases with no location provided is estimated as follows: sum of previous total cases with no location provided and new daily cases for which location is under investigation by EODY, with duplicates substracted.

### 8. greece_deaths.csv (ARCHIVED)
Cumulative data about deaths by prefecture/regional unit in Greece and by date of the incident. The value "<b><i>Απροσδιόριστος</b></i>" (<i>Unknown</i>) in the "county" column means that the prefecture/regional unit has not been known for the relevant number of cumulative deaths on the date of reference. The dataset is archived. Relevant figures about deaths have still been maintained in greece_deaths_v2.csv. Please find more information on these below.

#### Data Sources
Since neither EODY nor the Ministry of Health announce official data about the geographical location of each death, this dataset has been compiled by fact-checked news reports published in the Greek press. 

#### Notes
- As mentioned above, daily cumulative deaths data corresponds to deaths that occurred by the calendar date of reference. That means the sum of deaths by prefecture/regional unit on specific dates might be different than the total number of deaths announced by EODY, or the Ministry of Health, on the same date. This happens because authorities announce the total number of deaths as a result of the number of new deaths that occurred in their 24-hour reporting window, which is 15:00 - 15:00 (EEST) and 18:00 - 18:00 (EEST) for EODY and the Ministry of Health respectively.<br/>If you wish to use the exact number of new and total deaths officially announced each day, run through the pdfsDataFrame.csv for information extracted from the [official reports published in PDF files by EODY](https://eody.gov.gr/epidimiologika-statistika-dedomena/ektheseis-covid-19/).
- The "pop11" column holds the data on the resident population based on the 2011 census, as provided by the [Hellenic Statistical Authority](https://www.statistics.gr/el/statistics/-/publication/SAM03/-).

### 9. greece_deaths_v2.csv (ARCHIVED)
Cumulative data about deaths by prefecture/regional unit in Greece and by date of the incident. The value "<b><i>Χωρίς Γεωγραφικό Προσδιορισμό</b></i>" in the "county" column means that the prefecture/regional unit has not been known for the relevant number of cumulative deaths on the date of reference. 

#### Data Sources
Since neither EODY nor the Ministry of Health announce official data about the geographical location of each death, this dataset has been compiled by fact-checked news reports published in the Greek press. 

#### Notes
- As mentioned above, daily cumulative deaths data corresponds to deaths that occurred by the calendar date of reference. That means the sum of deaths by prefecture/regional unit on specific dates might be different than the total number of deaths announced by EODY, or the Ministry of Health, on the same date. This happens because authorities announce the total number of deaths as a result of the number of new deaths that occurred in their 24-hour reporting window, which is 15:00 - 15:00 (EEST) and 18:00 - 18:00 (EEST) for EODY and the Ministry of Health respectively.<br/>If you wish to use the exact number of new and total deaths officially announced each day, run through the pdfsDataFrame.csv for information extracted from the [official reports published in PDF files by EODY](https://eody.gov.gr/epidimiologika-statistika-dedomena/ektheseis-covid-19/).
- The "pop11" column holds the data on the resident population based on the 2011 census, as provided by the [Hellenic Statistical Authority](https://www.statistics.gr/el/statistics/-/publication/SAM03/-).

### 10. pdfsDataFrame.csv (ARCHIVED)
Content retrieved and data extracted from the reports published in PDF files by [EODY](https://eody.gov.gr/epidimiologika-statistika-dedomena/ektheseis-covid-19/). The dataset is updated automatically on a daily basis. The PDF files are read with the [Apache TIKA library](https://tika.apache.org/) and the program which extracts the data is written in Python. 

### 11. regions_greece.csv (ARCHIVED)
Cumulative data on cases, deaths, critically ill patients (intubated), and recovered patients by region in Greece. The value "<b><i>No Location Provided</b></i>" in the "district_EN" column means that the region has not been known for the relevant numbers of cases, of deaths, of critically ill patients, and of people who recovered. The dataset used to be updated automatically. The dataset has been archived; last publication date is October 19, 2020 including data up to October 18, 2020. Relevant figures about cases and deaths have still been maintained in regions_greece_cases.csv, greece_cases_v2.csv, regions_greece_deaths.csv and greece_deaths_v2.csv. Please find more information on these in the relevant sections for said datasets. 

#### Data Sources
- The [Hellenic National Public Health Organisation (EODY)](https://eody.gov.gr/) is the main source of data that have been released through:
    - [covid19.gov.gr](https://covid19.gov.gr/covid19-live-analytics/)
    - Announcements published by [EODY](https://eody.gov.gr/category/anakoinoseis/) and the [Ministry of Health](https://www.moh.gov.gr/articles/ministry/grafeio-typoy/press-releases).
    - [Reports](https://eody.gov.gr/epidimiologika-statistika-dedomena/ektheseis-covid-19/) published in PDF files by EODY.
- Deaths data have been retrieved from fact-checked news reports, published in the Greek Press, since neither EODY nor the Ministry of Health announce official data about the geographical location of each death.
    
#### Notes
- <b>Data updates</b>: Usually, the dataset is updated at 18:00 (EEST), once EODY announcement is out. Then, the number of new cases announced is added to correspond to "No Location Provided". Αs soon as covid19.gov.gr updates its dashboard, the dataset is updated again and new cases are added to their respective region. 
- The "pop11" column holds the data on the resident population based on the 2011 census, as provided by the [Hellenic Statistical Authority](https://www.statistics.gr/el/statistics/-/publication/SAM03/-).

### 12. regions_greece_cases.csv (ARCHIVED)
Cumulative data about cases by region in Greece and by date of announcement. The value "<b><i>No Location Provided</i></b>" in the "district_EN" column means that the region has not been announced by the authorities for the relevant number of cases on the date of reference. The data is updated automatically. 

#### Data Sources
- The [Hellenic National Public Health Organisation (EODY)](https://eody.gov.gr/) is the main source of data that have been released through:
    - [covid19.gov.gr](https://covid19.gov.gr/covid19-live-analytics/) (data from April 23, 2020, onwards)
    - Announcements published by [EODY](https://eody.gov.gr/category/anakoinoseis/) and the [Ministry of Health](https://www.moh.gov.gr/articles/ministry/grafeio-typoy/press-releases)(data by April 22, 2020)
    - [Reports](https://eody.gov.gr/epidimiologika-statistika-dedomena/ektheseis-covid-19/) published in PDF files by EODY (data by April 22, 2020)
    
#### Notes 
- The "pop11" column holds the data on the resident population based on the 2011 census, as provided by the [Hellenic Statistical Authority](https://www.statistics.gr/el/statistics/-/publication/SAM03/-).

### 13. regions_greece_deaths.csv (ARCHIVED)
Cumulative data about deaths by region in Greece and by date of the incident. The value "<b><i>No Location Provided</b></i>" in the "district_EN" column means that the region has not been known for the relevant number of cases on the date of reference. 

#### Data Sources
Since neither EODY nor the Ministry of Health announce official data about the geographical location of each death, this dataset has been compiled by fact-checked news reports published in the Greek press. 

#### Notes
- As mentioned above, daily cumulative deaths data corresponds to deaths that occurred by the calendar date of reference. That means the sum of deaths by prefecture/regional unit on specific dates might be different than the total number of deaths announced by EODY, or the Ministry of Health, on the same date. This happens because authorities announce the total number of deaths as a result of the number of new deaths that occurred in their 24-hour reporting window, which is 15:00 - 15:00 (EEST) and 18:00 - 18:00 (EEST) for EODY and the Ministry of Health respectively.<br/>If you wish to use the exact number of new and total deaths announced each day, run through the pdfsDataFrame.csv for information extracted from the [official reports published in PDF files by EODY](https://eody.gov.gr/epidimiologika-statistika-dedomena/ektheseis-covid-19/).
- The "pop11" column holds the data on the resident population based on the 2011 census, as provided by the [Hellenic Statistical Authority](https://www.statistics.gr/el/statistics/-/publication/SAM03/-).

### 14. schools.csv
Data about schools suspended in Greece because of COVID-19 cases. Information about schools closed and/or partially suspended have been retrieved from the relevant list of announcements published by the Ministry of Education. We process those data to remove duplicates if there are any and to give status value to schools listed: "Ολική αναστολή" ("Schools closed"), "Μερική αναστολή ("Partial suspension"), "Επαναλειτουργία" ("Re-operation") are the possible status classifications for the schools in the dataset. Schools are geolocated by iMEdD Lab with the use of Google Geolocation API service. The dataset is updated twice a day.

#### Data Sources
- [Schools list published by the Ministry of Education](https://www.sch.gr/anastoli/web/index.php?r=site%2Findex&fbclid=IwAR1EnmUjFxut8odh8vbQIoYXpRKJmFCOt7r599yq_SV5mEvLsgMj0_Q0FrE&page=1&per-page=100)

### 15. wom_data.csv (ARCHIVED)
International data retrieved from the [Worldometer](https://www.worldometers.info/coronavirus/). 

### 16. rapid_tests.csv
Data of rapid tests samples taken from EODY Mobile Health Groups throughout Greece. The dataset contains information such as UID of the area that the tests were performed each day, the name of the regional unit, the area and the address that EODY had set up the tent where they performed the  tests, total of samples taken, the positive samples and how many of them where males or females, their median age, the positivity rate (%) and finally lat - long of the address. 
This dataset is produced automatically, by parsing the e-mails EODY has been sending to accredited science health reporters via e-mail. 
#### Notes
Data are collected automatically and may contain mistakes. Geolocation is also automated and may not be accurate. In case you find mistakes, please contact a.troboukis [at] imedd.org.

### 17. sorted_rapid_tests.csv
rapid_tests.csv sorted by positivity (ascending = False)
#### Notes
Data are collected automatically and may contain mistakes. Geolocation is also automated and may not be accurate. In case you find mistakes, please contact a.troboukis [at] imedd.org.

### 18. greece_covid_deaths_20_21.csv
Cumulative covid-19 related deahts by region unit for the years 2020 & 2021. Columns all_deaths_20 & all_deaths_21 record the total number of deaths by regional unit by any cause (not just covid-19).
#### Data Source
The Minister of Interior, Makis Voridis, submitted to the Parliament (March 2022) the data on deaths due to covid, per municipality, for the period 2020-2021, in response to a question from MP Maria Apatzidi of  MeRA25 political party. 
#### Notes
Voridis claims the data were drawn from the Registry Subsystem of the Information System "Citizen Registry" based on the following criteria:
- The finalised and undeleted Death Certificates were taken into account.
- The municipality is derived from the municipality to which the Registry Office of the compilation of the Death Certificate is belonging.
- The date of death has been set as the search criterion.
- Deaths recorded at the Special Registry of Athens or at Greek consulates (deaths of Greeks abroad) are not included.
- The description of the cause of death in the Information System is derived from the death certificate and is a free text field and not a list of values, so the identification of deaths due to covid-19 was carried out by searching for critical words such as "COVID", "SARS", "COV2", "SARS", "KORON" etc. within the "cause of death" field.
-Based on the data submitted to the Parliament, in the two years 2020-2021, no deaths due to covid have been reported in the Municipalities of Agathonisi, Agios Efstratios, Agistri, Alonissos, Amari, Anafi, Antiparos, Vrilissia, Gavdos, Elafonisos, Heroic Island of Kasos, Heroic Island of Psara, Kimolos, Kythnos, Meganissi, Megisti, Nisyros, Patmos, Serifos, Sikinos, Skyros, Symi, Tilos, Tinos, Folegandros, Fournoi Korseon, Halki.

