# UnitTestingProjects
This repo contains unit testing procedures performed on at least one project
Projects are mainly data analytics related, with the second being a unit of my final year project implementation.
 
 For the first, data.py, the function basically fetches stock data from the yahoo finance website, and then returns the pandas dataframe.
 Some failures may include the following scenarios:
 1. the data reader not returning anything probably because Yahoo finace is down or even null values as well as missing values so the test fucntions in this case will check for the modes of possible failure...