#Import Necessary libraries
import requests
from bs4 import BeautifulSoup
import re
from datetime import date
import time
import pandas as pd
import os.path
from os import path

#Get date and the time of the request to cdc page
current_date = date.today().strftime("%m/%d/%y")
print("Getching data from ")
print("Date: " + str(current_date))
current_time = time.strftime("%H:%M:%S", time.localtime())
print("Time EST: " + str(current_time))
#Get all the contents of the website and parse into a Beautiful Soup Object
page = requests.get("https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/cases-in-us.html#2019coronavirus-summary")
soup = BeautifulSoup(page.content, 'html.parser')

#Find the tags where number of cases and deaths are reproted
links = soup.find_all('li')
for link in links:
    if link.find(text=re.compile("Total cases")):
        total = link
    if link.find(text=re.compile("Total deaths")):
        deaths = link

#Get the total number of cases
total = str(total)
if "," in total:
    total = total.replace(',' , '')
Ntotal = re.findall(r"[-+]?\d*\.\d+|\d+", str(total))[0]
print ("Total Confirmed cases: " + Ntotal)

#Get the total number of deaths
deaths= str(deaths)
if "," in deaths:
    deaths = deaths.replace(',' , '')
Ndeath = re.findall(r"[-+]?\d*\.\d+|\d+", str(deaths))[0]
print("Total Deaths: " + Ndeath)



#print(data.columns)
#dfToAdd = pd.DataFrame([current_date],[current_time],[Ntotal],[Ndeath], columns = data.columns)
if path.exists("CoronaCDCTImeSeries.csv"):
    print("file exists")
    data = pd.read_csv("CoronaCDCTImeSeries.csv")
    data = data.append({'Date' : current_date, 'Time (EST)' : current_time, 'Confirmed' : Ntotal, 'Deaths' : Ndeath} , ignore_index=True)
    print(data)
    data.to_csv ("CoronaCDCTImeSeries.csv", index = False, header=True)
else:
    df = pd.DataFrame({'Date' : [current_date], 'Time (EST)' : [current_time], 'Confirmed' : [Ntotal], 'Deaths' : [Ndeath]})
    print(df)
    df.to_csv ("CoronaCDCTImeSeries.csv", index = False, header=True)
