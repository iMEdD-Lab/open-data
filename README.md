# [lab.imedd.org/covid19](lab.imedd.org/covid19)
## [iMEdD Lab](https://www.imedd.org/imedd-lab/)'s Application and the Data

The “COVID-19: The spread of the disease in Greece and worldwide” was created and is managed by iMEdD Lab. Its purpose is to facilitate the work of the journalistic community and to inform anyone interested in the spread of the pandemic in Greece and around the world. 

It was first launched online on 16 March 2020 and, since then, it is constantly updated with the most recently known information. From its first launch to last November, the application had been regularly updated with various new features and additional analyses. Fully redesigned as it is today, the application was presented on December 2, 2020, when iMEdD Lab launched the version 2.0. 
The application shows the geographical distribution of confirmed recorded cases and deaths in our country and globally, while it also comprehensively presents analyses on the evolution of epidemiologic data in Greece and across the globe, by country. 

<b> The data sources </b>

All epidemiologic data for Greece, except for the geographical distribution of deaths, are based on official information announced by the competent bodies. Since February 26, 2020, iMEdD Lab has been collecting official data from multiple channels of distribution and it maintains them in open datasets, which are available in the relevant repository, in iMEdD Lab’s account on GitHub.

Specifically, all our analyses about cases, intubated and recovered patients, the total number of deaths and samples tested in Greece derive from datasets structured by iMEdD Lab based on information released through: 

- daily epidemiological surveillance reports published by EODY in PDF format
- other daily announcements and informal updates emailed to the Press by EODY 
- briefings to accredited health journalists by the Ministry of Health
- informal updates emailed to the Press by the Ministry of Health
- updates released by the General Secretariat of Civil Protection in .pdf files (indicatively) 
- the covid19.gov.gr platform

The source of the global current data is the Worldometer, the content of which is subject to terms of use. That data is shown on the main world map, when the –preselected– “Last day” time period filter is active. In the iMEdD Lab application, this information and the corresponding visualisations are updated every two hours.
The global historical data comes from the repository of Johns Hopkins University on GitHub. In this repository, the University makes the data collected by its research team available for educational and research purposes. This database is updated once a day, as well as the relevant visualizations on iMEdD Lab’s application. That data is shown on the world map, whenever every other time filter except for the “Last day” one is active, as well as in charts presented in the “Insights on the World” section. More information about the corresponding online application of Johns Hopkins University, which was launched on 22 January 2020, its development and the data it uses can be found here.

Data analysis and visualizations
The world map shows the total number of recorded cases and deaths per 100,000 population for each country. The map of Greece shows the total number of recorded cases per 100,000 population for each area (Attica Region, by Regional Unit for the rest of the mainland and by Prefecture for the island country): this calculation is done secondarily by iMEdD Lab, taking into account the absolute number of recorded cases and deaths, which are known per Prefecture, and the data on the resident population based on the 2011 census, as provided by ELSTAT.
This “normalisation of numbers” (in this case, the recording of the number of recorded cases per 1,000,000 and per 100,000 population, around the world and in the Prefectures of Greece respectively) has been selected for two reasons: on the one hand, it allows the visualisation of data on a choropleth map, such as that used by iMEdD Lab. On the other hand, it allows a more correct understanding of the issue of the spread of the virus per country or per Prefecture, allowing a comparison of the extent of the problem based on population size.
However, in reading any such map of cases, attention is brought to the fact that, for example, there are differences in terms of the laboratory tests various countries perform: Some countries opt for mass testing of the population and therefore announce more confirmed cases. Other countries conduct targeted testing on smaller populations, so they may record fewer cases than is the case. Thus, there can be significant differences in the mapping of the actual spread of the virus in each country, even between states with equal populations. For this reason, the normalisation of recorded cases based on the laboratory tests that each country has conducted would be even more appropriate. So far, the relevant publicly available official data found are not recorded in one homogeneous and standardized way for every country. For instance, a country may report the total number of samples tested, while another country might report the total number of people tested. Thus,  different policies of various countries regarding both testing and the way tests are reported might drive to underestimations or overestimations. You could visit Our world in data, if you wish to read more about testing data.
A 7-day moving average is additionally presented in every chart showing the evolution of epidemiological data over time (i.e. daily new cases or cumulative cases up to each day of reference): the 7-day moving average is based on secondary calculations, using available official data, and is used to smooth values recorded and announced by the authorities. In specific, the rolling average of each variable (cases, deaths, etc) is calculated and represented for each day, taking into account the data of the last seven days before it.
In the “Insights on Greece” section, the chart entitled “Evolution of new cases by area in Greece” represents daily new cases both per 100,000 residents and in absolute numbers, in each area. Areas are ranked based on the number of new cases per 100,000 residents, meaning that districts on top currently face a more severe outbreak. International data are similarly visualized in the chart entitled “Evolution of new cases and deaths by country” in the “Insights on the World” section.
Finally, the active cases figure that is presented in the side menu on the map section, when the –preselected– “Last day” time filter is active, is calculated by subtracting both the number of recovered patients and the number of deaths from the total number of cases, according to the most recent known data each time. 

Tools we use
Scripts developed with the use of Python programming language run for the retrieval, the extraction and the processing of data. As for the retrieval of content enclosed in the daily epidemiological surveillance report issued by EODY in .pdf files, the Apache TIKA library is used. 
One of the tools that have been used to collect global data from Worldometer is Workbench, an application that makes it easier for journalists to collect and analyse data without requiring programming language skills, has been used for the collection and the processing of global data deriving from Worldometer. Workbench was developed in Greek in the framework of the first cycle of the iMEdD Incubator.
The map background has been sponsored by the Mapbox Community team, which encloses data deriving from the open and publicly available Open Street Map.  
The application is developed with JavaScript, by Civic Information Office (CVCIO) and it is an open code project. You may find more information about scripts developed, tools and libraries used on the relevant GitHub repository. 
 
Plotly Python Open Source Graphic Library was also used to create charts in the “STATISTICS” section of the former version 1.0 of the application. 

Framwork of use
Both iMEdD Lab’s web application, “COVID-19: The spread of the disease in Greece and worldwide”, and all open datasets on the relevant repository of iMEdD Lab on GitHub, are publicly available under a Creative Commons license of use. 
You can share and/or embed contents of iMEdD Lab’s web application in your website, in accordance with the terms hereof. Please kindly cite the creator and comply with the terms and restrictions stated here.
The iMEdD Lab app does not contain data regarding the age, gender, nationality of patients nor any other type of demographic or personal data.
The web application has been created solely for informational purposes and its use for any other purpose is expressly prohibited. Any commercial or medical use is strictly prohibited. This website does not provide any medical guidance. No information of the website replaces the official sources and announcements of the competent state authorities. For official announcements and useful information, you can visit the website of the EODY. iMEdD bears no responsibility for the accuracy of the content of this website or for any violation of its terms.
For any additional information or clarification, please contact lab@imedd.org or use the iMEdD contact form.

