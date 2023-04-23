##### bellingcat_hackathon_2304_submission

# BOMBARDIER WATCH

A tool to monitor the movements of business jets around the world.

by Jack Kerr (Group: Jackmaster)

Unfiltered crowd-sourced flight-tracking service ADS-B Exchange offer an excellent view of air traffice movements. But finding out who is on board is another matter.

This tool provides one solution to that: by showing which of these jets arrived or departed from the same location on the same day, it amy be possible to work out who met who.

Development notes: 
- Data source from ADS-B Exchange. 
- This protype model uses data from one day, as recorded at the start of each minute. 
- Results filter to only include Bombardier, Gulfstream, Dassault and Embraer business jets that are show as "grounded".

### FEATURES

![image](https://user-images.githubusercontent.com/69304112/233846351-947c5fde-e061-49f5-8d02-b3de6450d0ca.png)

As this a prototype with limited access to data, only one day of data is availalbe, and therefore the date dropdown has been disabled.

![image](https://user-images.githubusercontent.com/69304112/233846488-2f688dff-dda6-4054-b826-e37b7451fb00.png)

The globe shows where business jets were recorded as being on the ground. This provides insights into unusual locations business jets may be.

![image](https://user-images.githubusercontent.com/69304112/233846567-abb6242c-c742-44d2-b6d2-f346bbcfe628.png)

This section allows you to chose a location where jets were recorded, and examine the results for interesting matches. Unfortunately, the majority of planes are registered to charter companies, but this tool will still be able to produce interesting results over time.

![image](https://user-images.githubusercontent.com/69304112/233846689-4f8a14da-3bd5-435c-8cb8-e6b9cd720443.png)

Lastly, it is possible to check by company, and see which other registered owners their jet(s) were in the same location as.

### Getting the data ###
ADS-B Exchange makes historical data available in 5-second snapshots - a total of 17280 files per day. This means that a few hours of observations can. when combined, result in massive dataframes of millions of rows. Accessing this data would be ideal. This repository contins one file for downloading a day's data, one for compiling it into a dataframe, and another for cleaning this up and adding plane registrant details. In this second stage, filters are applied so that only business jets are included in the concatenated dataframe, in order to make the dataframe a more manageable size. Whiledata from every 5 seconds is available, this app only uses data from every 60 seconds. 

