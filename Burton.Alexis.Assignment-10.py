#Alexis Burton Assignment8-Data Visualization
#02/27/2020
#Using matplotlib, numpy, json and pandas to access a json file with price information for 8 stock symbols

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import json
from datetime import datetime
from matplotlib import dates
import matplotlib as mpl
stock_Prices = []
stock_Dates = []
filePath ="AllStocks.json"
stock_Symbols = []
stock_Symbols_Unique = []

#Open json file
with open(filePath) as f: 
    dataSet = json.load(f)

#Using Pandas to read the json files into a data frame
df = pd.read_json (r'AllStocks.json')
ax = plt.gca()
#Adding y-axis label
plt.ylabel('Price')

#Plotting close price grouped by stock symbol
for name, group in df.groupby('Symbol'):
    #plotting the date to the x-axis and Close to the y-axis
    group.plot(x='Date',y='Close', ax=ax, label=name)
#Showing the chart
plt.show() 

