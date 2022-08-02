from email import header
from fileinput import filename
import requests
import pandas as pd
import numpy as np
from statsmodels.tsa.stattools import adfuller


def query(payload):
    url = "https://enersmart.sperixlabs.org/balance"
    headers = {'Accept': '*/*',
    'Origin': 'https://enersmart.sperixlabs.org',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }

    response =  requests.request("POST", url, headers=headers, data=payload)
    result = response.json()
    
    return result


query("14125509")



#reading data from excel or database
#excel data in this instance


def get_energy_data(filemame):
    
    df=pd.read_excel(filename)
    df['Consumption'] = abs(df['Balance'].diff().dropna())
    train = df[df["Class"] == "Train"]
    test = df[df["Class"] == "Test"]
    #creating train and test arrays 
    train_array = train["Consumption"]
    test_array = test["Consumption"]
    
    #testing for stationarity
    #if p value is less than conventional 0.05 take difference
    
    pValue  = adfuller(train_array.dropna())[1]
    while (pValue > 0.05):
        p = 0
        df['Consumption'].diff()
        p = p+1
        
    else:
        p=0
    
    
        
        
    
    
    
    
    
    

    




    


