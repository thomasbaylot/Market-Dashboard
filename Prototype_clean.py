#Dashboard with equity (SPY), forex (USD), commodities (Gold ($GC=F), crude oil ($WTI, or $USO), wheat ($ZW=F)), bonds ($^TNX) Inflation Linked Bonds)
#Data about growth, inflation, volatility and yield
#Data goes back as far as possible, with widget slider to chose time frame

#Import libraries
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

#Data download and save in CSV
def data_download(ticker, filename):
    data = yf.download(ticker, period = 'max')['Close']
    data.to_csv(filename)

ticker_filename = {
    "SPY" : "spy.csv",
    "DX-Y.NYB" : "usd.csv",
    "GC=F" : "gold.csv",
    "WTI" : "wti.csv",
    "ZW=F" : "wheat.csv",
    "^TNX" : "bonds.csv"
}

for ticker, filename in ticker_filename.items():
    data_download(ticker, filename)

#Sanity check
def check_na(data):
    null_sum = data.isna().sum()
    null_percentage = null_sum/len(data)
    print(f"Ratio of missing values: {null_percentage}")

for price in ticker_filename.values():
    check_na(pd.read_csv(price, index_col=0, parse_dates = True))
