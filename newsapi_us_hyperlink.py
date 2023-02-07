#!/Users/sankarasarma/opt/anaconda3/bin/python3
''' Program to pull data from  news api '''
from datetime import date
today = date.today()
import requests
import pandas as pd
import re
pd.options.display.width = None
pd.set_option("display.max_colwidth", None) # to display column value without any truncation
pd.set_option('expand_frame_repr', False)  #To print the DataFrame on a single line:

params={"country":"us",
"category":"general",
"apiKey":"<your API Key>"}

def get_topheadlines():
    # Define the API endpoint for translating text
    endpoint = "https://newsapi.org/v2/top-headlines"
    # Make the API request and get the response
    response = requests.get(endpoint, params=params)
    output=response.json()
    outfile="/Users/sankarasarma/Library/CloudStorage/GoogleDrive-sankarasarma@gmail.com/My Drive/DailyNews/"+"us"+str(today)+".csv"
    data=pd.DataFrame(output["articles"], columns=["title","description","url"])
    urlhyper=data['url']
    #print(urlhyper)
    for urls in urlhyper:
        replace_url_to_link(urls)
    datacsv=data.to_csv(outfile,index=False)  #converting dataframe to csv file
    urls=pd.read_csv(outfile,usecols=['url'],squeeze=True)

def replace_url_to_link(value):
    # Replace url to link
    urls = re.compile(r"((https?):((//)|(\\\\))+[\w\d:#@%/;$()~_?\+-=\\\.&]*)", re.MULTILINE|re.UNICODE)
    value = urls.sub(r'<a href="\1" target="_blank">\1</a>', value)
    
    #print(f'{value}')
    return value    
get_topheadlines()

