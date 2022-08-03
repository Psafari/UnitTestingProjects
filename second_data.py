from email import header
from fileinput import filename
import requests
import pandas as pd
import numpy as np
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima_model import ARIMA
import pmdarima as pmd
import itertools
import warnings
warnings.filterwarnings('ignore')


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
    df[df['date','Consumption']]
    #df['Class'] = np.NaN
    #int(0.75*len(df['Consumption'])) 
    
    #train = df[df["Class"] == "Train"]
    #test = df[df["Class"] == "Test"]
    #creating train and test arrays 
    #train_array = train["Consumption"]
    #test_array = test["Consumption"]
    
    #testing for stationarity
    #if p value is less than conventional 0.05 take difference
    #determination of p value for model
    pValue  = adfuller(df['Consumption'].dropna())[1]
    d = 0
    if pValue > 0.05:
        
        df['Consumption'].diff().dropna()
        d = d+1
        
    else:
        d=0
    X = df['Consumption'].values
    train = X[0:int(0.75*len(X))]#majority of data
    test = X[int(0.75*len(X)): ] #remaining data
    predictions = []
    #Arima model
    #p, order of auto-regressive model, q=order of the moving average model, d= the order of first-differencing
    #def arimamodel(timeseriesaarray):
    #    auto_arima_model = pmd.auto_arima(timeseriesaarray,start_P=1,start_q=1,test="adf",trace=True)
        
    #    return auto_arima_model
    
#using above function to build arima estimator on training data
    #arima_model = arimamodel(train_array)
    
    #ARIMA MODEL
    p=d=q = range(0,8)
    pdq = list(itertools.product(p,d,q))
    for param in pdq:
        try:
            
            model_arima = ARIMA(train,param)
            model_arima_fit = model_arima.fit()
            aicValue = np.array(model_arima_fit.aic, param)
            leastAicValue_point = aicValue[np.argmin(aicValue[:,0])][1]
            p_new = leastAicValue_point[0]
            d_new = leastAicValue_point[1]
            q_new = leastAicValue_point[2]
            
        except:
            continue
    model_arima=ARIMA(train,order=(p_new,d_new,q_new)) 
    model_arima_fit=model_arima.fit()   
    predictions=model_arima_fit.forecast(steps=7)[0]
    print (predictions)
    
    
        
    
    
        
    
    
    
    
    
    

    




    


