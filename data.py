from pandas import DataFrame
import pandas_datareader.data as web

#function for fetching stock data from yahoo finance
def read_Sdata(ticker):
    DataFrame = web.DataReader(ticker, "yahoo")
    return DataFrame