import pytest
import datetime
import unittest
import pandas as pd
import pandas_datareader.data as web


def read_Sdata(ticker):
    dataFrame = web.DataReader(ticker, "yahoo")
    return dataFrame


class TestReadSdata(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.dataFrame = read_Sdata('^DJI') 
        
#To ensure that all expected columns are present in the returned dataframe        
    def test_columnsPresent(self):
            self.assertIn("Open", self.df.columns)
            self.assertIn("High", self.df.columns)
            self.assertIn("Low", self.df.columns)
            self.assertIn("Close", self.df.columns)
            self.assertIn("Volume", self.df.columns)

#to ensure that there is more than one row of data    
    def test_non_empty(self):
        self.assertNotEqual(len(self.df.index),0)
        
#for high and low to be the actual highest and lowest in the same row       
    def test_highLow(self):
        open_high_close_low = self.df[["Open","High","Low","close"]]
        highest = open_high_close_low.max(axis=1)
        lowest = open_high_close_low.min(axis=1)
        self.assertTrue(open_high_close_low.le(highest, axis=0).all(axis=None))
        self.assertTrue(open_high_close_low.ge(lowest, axis=0).all(axis=None))
        

#to ensure that the most recent data was collected within the last week.        
    def test_most_recent_within_week(self):
        most_recent_date= pd.to_datetime(self.df.index[-1])
        self.assertLessEqual((datetime.datetime.today() - most_recent_date).days, 7)  
        
        
unittest.main()    
            
        
            