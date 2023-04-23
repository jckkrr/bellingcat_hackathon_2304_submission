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

### Getting the data ###
ADS-B Exchange makes historical data available in 5-second snapshots - a total of 17280 files per day. This means that a few hours of observations can. when combined, result in massive dataframes of millions of rows. Accessing this data would be ideal. This repository contins one file for downloading a day's data, one for compiling it into a dataframe, and another for cleaning this up and adding plane registrant details. In this second stage, filters are applied so that only business jets are included in the concatenated dataframe, in order to make the dataframe a more manageable size. 
