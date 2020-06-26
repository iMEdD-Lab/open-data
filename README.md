# [lab.imedd.org/covid19](lab.imedd.org/covid19)
## [iMEdD Lab](https://www.imedd.org/imedd-lab/)'s Application and the Data

[lab.imedd.org/covid19](lab.imedd.org/covid19) is a web application that was created and is managed by [iMEdD Lab](https://www.imedd.org/imedd-lab/). It was launched online on 16 March 2020 and is updated daily since then. Its purpose is to inform the Greek journalistic community and anyone else interested in the spread of the SARS-CoV-2 virus in Greece and around the world, using a simple, easy-to-use tool.

The application shows the geographical distribution of confirmed recorded cases in our country and globally, while it also comprehensively presents the available statistics. A couple of different analyses are also presented in the “[STATISTICS](https://lab.imedd.org/covid19/stats/)” page via interactive charts and maps.

The data on confirmed recorded cases in Greece and the data on the geographical distribution of cases in the country are based on official data, announced daily by the [Hellenic National Public Health Organisation (EODY)](https://eody.gov.gr/) and the Ministry of Health, along with cross-checked information published in the Greek Press. The iMEdD Lab team collects this data and stores it in datasets, which are available on the [open-data relevant repository](https://github.com/iMEdD-Lab/open-data/tree/master/COVID-19), in iMEdD Lab’s account on GitHub.

The source of the global current data is the [Worldometer](https://www.worldometers.info/coronavirus/), the content of which is subject to [terms of use](https://www.worldometers.info/disclaimer/). That data is shown on the main world map, in the table of countries, by number of cases, number of recoveries or number of deaths, and on additional world maps found in the “STATISTICS” page. In the iMEdD Lab application, this information and the corresponding visualisations are updated regularly throughout the day.

The global historical data shown in the chart “Evolution of Cases through Time”, in the timeline of the world map and in the rest of visualizations available at the “STATISTICS” page comes from the repository of [Johns Hopkins University on GitHub](https://github.com/CSSEGISandData/COVID-19). In this repository, the University makes the data collected by its research team available for educational and research purposes. This database is updated once a day. More information about the [corresponding online application](https://coronavirus.jhu.edu/map.html) of Johns Hopkins University, which was launched on 22 January 2020, its development and the data it uses can be found [here](https://coronavirus.jhu.edu/map-faq).

The chart “7-day Moving Average of Cases” is based on secondary calculations, using available data, and represents the seven-day rolling average, with the aim of “normalising” the daily number of new cases, as recorded and announced by the Authorities. In specific, the rolling average of cases is calculated and represented for each day, taking into account the data of the last seven days before it.

The world map shows the total number of recorded cases and deaths per 1,000,000 population for each country. The map of Greece shows the total number of recorded cases and deaths per 100,000 population for each Prefecture: this calculation is done secondarily by iMEdD Lab, taking into account the absolute number of recorded cases and deaths, which are known per Prefecture, and the data on the resident population based on the 2011 census, as provided by the [Hellenic Statistical Authority](https://www.statistics.gr/el/statistics/-/publication/SAM03/-).

This “normalisation of numbers” (in this case, the recording of the number of recorded cases per 1,000,000 and per 100,000 population, around the world and in the Prefectures of Greece respectively) has been selected for two reasons: on the one hand, it allows the visualisation of data on a choropleth map, such as that used by iMEdD Lab. On the other hand, it allows a more correct understanding of the issue of the spread of the virus per country or per Prefecture, allowing a comparison of the extent of the problem based on population size.

However, in reading any such map of cases, attention is brought to the fact that, for example, there are differences in terms of the laboratory tests various countries perform: Some countries opt for mass testing of the population and therefore announce more confirmed cases. Other countries conduct targeted testing on smaller populations, so they may record fewer cases than is the case. Thus, there can be significant differences in the mapping of the actual spread of the virus in each country, even between states with equal populations. For this reason, the normalisation of recorded cases based on the laboratory tests that each country has conducted would be even more appropriate. However, so far, the relevant official data is not publicly available for all countries.

In the “STATISTICS” page, the chart “Cases, Tests and Deaths per Country” and the map “Cases/Tests Ratio per country” touch the matter of the correlation between the number of recorded cases and the number of reported tests performed by each country based on data published by the [Worldometer](https://www.worldometers.info/coronavirus/). In any case, different policies of various countries regarding both testing and the way laboratory tests are reported might drive to underestimations or overestimations. You could visit [Our world in data](https://ourworldindata.org/coronavirus-testing), if you wish to read more about testing data.

In the “STATISTICS” page again, the charts “Evolution of deaths from the 10th death onwards” and “Evolution of cases after first 100” are updated once a day, because they are based on data published on the [Github repository](https://github.com/CSSEGISandData/COVID-19) of Johns Hopkins University, which is updated daily. Thus, you probably see the number of cases and the number of deaths recorded yesterday.

The charts “Deaths per 100K residents in countries with population similar to that of Greece” and “Cases per 100K residents in countries with population similar to that of Greece” include countries with a population of 9-12 million residents ([Worldometer / United Nations Population Division](https://www.worldometers.info/world-population/population-by-country/)).

You can share or/and embed this iMEdD Lab online application in your website, in accordance with the terms hereof. Please kindly cite the creator and comply with the terms and restrictions stated here.

The code for embedding the [map](https://lab.imedd.org/covid19/) is:

<iframe
src="https://lab.imedd.org/covid19/?lang=en"
style="border:0px #ffffff none;"
name="imedd-covid"
scrolling="no"
frameborder="1"
marginheight="0px"
marginwidth="0px"
height="640px"
width="640px"
allowfullscreen>
</iframe>


The code for embedding the "[STATISTICS](https://lab.imedd.org/covid19/stats/)" page is:

<iframe
src="https://lab.imedd.org/covid19/stats/?lang=en"
style="border:0px #ffffff none;"
name="imedd-covid-stats"
frameborder="1"
marginheight="0px"
marginwidth="0px"
height="640px"
width="640px"
allowfullscreen>
</iframe>

The iMEdD Lab app does not contain data regarding the age, gender, nationality of patients nor any other type of demographic or personal data.

In the list of countries, the entry “Diamond Princess” refers to the cases on board the cruise ship Diamond Princess, which is anchored off the coast of Japan. More information can be found here. The countries listed are not always shown accurately on the map. For example, because it is a overseas region of France, Martinique, located in the Caribbean, appears on the map under France. In other cases, because the name of the country in the Worldometer is not exactly the same as the name of the country on the map, it may not appear on the map as a country with active cases. We try to correct any such mistakes every time they come to our notice.

One of the tools that have been used to collect global data from Worldometer is [Workbench](https://workbenchdata.com/gr/), an application that makes it easier for journalists to collect and analyse data without requiring programming language skills. Workbench was developed in Greek in the framework of the [first cycle of the iMEdD Incubator](https://www.imedd.org/el/inhouse/workbench/).

The map showing the spread of COVID-19 in Greece and around the world was sponsored by the [Mapbox Community team](https://www.mapbox.com/community/).

This json file, which has been made available by [python-visualtization/folium](https://github.com/python-visualization/folium) on GitHub, under MIT License of use (Copyright © 2013, Rob Story), is used for the purposes of mapping the “Cases/Tests Ratio per Country” and the “Recovered Ratio per Country”.

This website has been created solely for informational purposes and its use for any other purpose is expressly prohibited. Any commercial or medical use is strictly prohibited. This website does not provide any medical guidance. No information of the website replaces the official sources and announcements of the competent state authorities. For official announcements and useful information, you can visit the website of the [EODY](https://eody.gov.gr/).

iMEdD bears no responsibility for the accuracy of the content of this website or for any violation of its terms.

For any additional information or clarification, please contact lab@imedd.org or use the iMEdD [contact form](https://www.imedd.org/el/contact/).
