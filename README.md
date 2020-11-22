# surfs_up

## Overview of Analysis
The purpose of this analysis was to research temperature trends in Oahu in order to open up both a surf shop and ice cream shop. To determine if these shops would be sustainable year-round, an analysis of the temperatures in June -- between 2010 and 2017 -- and in December, from the years 2010 through 2016.

## Resources
### Data Tools and Resources
* Python 3.9
* Anaconda 4.8.5
* Pandas
* Jupyter Notebook 6.1.4
* sqlalchemy
* hawaii.sqlite

## Results
![](https://github.com/jaredcclarke/surfs_up/blob/main/Resources/june_stats.png)

* The mean temperature in June from the year 2010 through the year 2017 was approximately 74.9 degrees Farenheit. 
* The minimum and maximum temperatures for June, between 2010 and 2017, were 64 degrees Farenheit and 85 degrees farenheit, respectively. 
* The mean and median (50% quartile) for June are extremely close

![](https://github.com/jaredcclarke/surfs_up/blob/main/Resources/dec_stats.png)

* Data for December temperatures was only available up to 2016, therefore thre are less temperature counts. 
* The mean temperature in December from the year 2010 through the year 2016 was approximately 71.0 degrees Farenheit. 
* The minimum and maximum temperatures for December, between 2010 and 2016, were 56 degrees Farenheit and 83 degrees farenheit, respectively. 
* The mean and median (50% quartile) for June are extremely close
* Quartile temperatures for June tend to be warmer than the temperatures for December.
* The mean and median (50% quartile) for December are extremely close
* December temperatures has a larger standard deviation

## Summary
* Overall, June temperatures are warmer than December temperatures.
* The closeness of the median and means for both months suggests the data is evenly distributed.
* The higher standard deviation for December temperatures suggests there are more outliers in the data.
* The max and min for June data are outliers
* The max and min for Decemeber data are outliers
* Judging by the data analysis, a year-round surf shop and ice cream shop could be viable business. 
* Would also want to check precipitation for these months because rain and tsunamis could be detrimental to the business. the query for this data is as follows:
``` june_precip_results = session.query(Measurement.date,Measurement.prcp).\
                  filter(extract('month', Measurement.date)==6).all()
print(june_precip_results)
```
```dec_precip_results = session.query(Measurement.date,Measurement.prcp).\
                  filter(extract('month', Measurement.date)==12).all()
print(dec_precip_results)
```
