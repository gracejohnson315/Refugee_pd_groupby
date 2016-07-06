## UN REFUGEE POPSTATS - SPLIT DATA BY ORIGIN COUNTRY
## Author: Grace Johnson
## Description: this program reads a csv file of data including duplicate "origin" values
## from multiple months in a year and sums the values together in order to get one value
## per origin-destination. It uses the Pandas Groupby function and outputs the result
## to a new csv.
## ------------------------------------------------------------------------------------

import csv
import pandas as pd

## Read csv file 
csv_file = open("/Users/gj92/Desktop/Esri ConnectED/Refugees/refugee_all.csv", 'r')

## Create Pandas DataFrame
df_csv = pd.read_csv(csv_file, sep=None, engine='python')
df_csv.columns = ['Origin','Destination', 'Year', 'Value']

## Group records by origin
grouped_origin = df_csv.groupby(['Origin','Destination', 'Year'], sort=False).sum()

## Write grouped data to a new csv file 
with open("/Users/gj92/Desktop/Esri ConnectED/Refugees/all_sum.csv", 'wb') as newfile:
    grouped_origin.to_csv(newfile)






