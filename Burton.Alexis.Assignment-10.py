#Alexis Burton Assignment10-Data Visualization Part Two
#03/12/2020
#Using matplotlib, json,  and pandas to 
# 1)access a json file with price information for 8 stock symbols
# 2)Get average-mean of the closing stock price for each symbol
# 3)show a pie chart graph of the value distribution of different stocks in the portfolio

import matplotlib.pyplot as plt
import pandas as pd
import json
filePath ="AllStocks.json"

#Using Pandas to read the json files into a data frame
df = pd.read_json (r'AllStocks.json')

#Average Close price by stock using groupby
av_column = df.groupby('Symbol').mean()
#create pie chart graph of the value distribution of different stocks in the portfolio
av_column.plot.pie(y='Close', subplots=True,  figsize=(5,5), autopct ='%1.1f%%', fontsize=10, title=('Portfolio Stock Valuation Distribution'))
#Plot the piechart
plt.show() 

