import pandas_datareader.data as web


def read_Sdata(ticker):
    df = web.DataReader(ticker, "yahoo")
    return df