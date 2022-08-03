from email import header
from fileinput import filename
import requests
import pandas as pd
import numpy as np
from statsmodels.tsa.stattools import adfuller
import pmdarima as pmd


#query api and retrieve consumption data
def query(payload):
    url = "https://enersmart.sperixlabs.org/balance"
    headers = {'Accept': '*/*',
    'Origin': 'https://enersmart.sperixlabs.org',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }

    response =  requests.request("POST", url, headers=headers, data=payload)
    result = response.json()
    
    return pd.read_json(result)






#reading data from excel or database
#excel data in this instance


def get_energy_data(file_name):
    
    df=pd.read_excel(file_name)
    df['Consumption'] = abs(df['Balance'].diff().dropna())
    df['Class'] = np.NaN
    int(0.75*len(df['Consumption'])) 
    df[df['date','Consumption','Class']]
    train = df[df["Class"] == "Train"]
    test = df[df["Class"] == "Test"]
    #creating train and test arrays 
    train_array = train["Consumption"]
    test_array = test["Consumption"]
    
    #testing for stationarity
    #if p value is less than conventional 0.05 take difference
    #determination of p value for model
    pValue  = adfuller(train_array.dropna())[1]
    p = 0
    if pValue > 0.05:
        
        df['Consumption'].diff().dropna()
        p = p+1
        
    else:
        p=0
    
    #Arima model
    #p, order of auto-regressive model, q=order of the moving average model, d= the order of first-differencing
    def arimamodel(timeseriesaarray):
        auto_arima_model = pmd.auto_arima(timeseriesaarray,start_P=1,start_q=1,test="adf",trace=True)
        
        return auto_arima_model
    
#using above function to build arima estimator on training data
    arima_model = arimamodel(train_array)
    
        
    
    
    
    
    
    

    




    


