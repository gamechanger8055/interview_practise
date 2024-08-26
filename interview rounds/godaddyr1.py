#url="https://jsonmock.hackerrank.com/api/moviesdata/search/?Title=man"

# !/bin/python3

import sys
import os
from urllib.request import Request
from urllib.request import urlopen
from urllib.error import URLError
import json
import requests
import threading

# Complete the function below.
# Base url: https://jsonmock.hackerrank.com/api/moviesdata/search/?Title=
'''
{"page":1,"per_page":10,"total":6,"total_pages":1,"data":[{"Title":"Italian Spiderman","Year":2007,"imdbID":"tt2705436"},{"Title":"Superman, Spiderman or Batman","Year":2011,"imdbID":"tt2084949"},{"Title":"Spiderman","Year":1990,"imdbID":"tt0100669"},{"Title":"Fighting, Flying and Driving: The Stunts of Spiderman 3","Year":2007,"imdbID":"tt1132238"},{"Title":"Spiderman 5","Year":2008,"imdbID":"tt3696826"},{"Title":"Spiderman in Cannes","Year":2016,"imdbID":"tt5978586"}]}'

https://jsonmock.hackerrank.com/api/moviesdata/search/?Title=man&page=

'''

URL = "https://jsonmock.hackerrank.com/api/moviesdata/search/?Title="


def fetch_data(page,url,combined_dataset,lock):
    new_url = url + "&page=" + str(page)
    response_page = requests.get(new_url).json()["data"]
    with lock:
        combined_dataset.extend(response_page)
def getMovieTitles(substr):
    url = URL + str(substr)
    combined_dataset = []
    abc={}
    requests.post(url,data=abc)
    if requests.get(url).status_code != 200:
        return []
    response = requests.get(url).json()  # fetching json response
    total_pages = response["total_pages"]
    lock=threading.Lock()
    threads=[]
    # making a list of combined dataset
    for page in range(1, total_pages + 1):
        thread=threading.Thread(target=fetch_data,args=(page,url,combined_dataset,lock))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    #print(combined_dataset)
    movie_titles = []
    for element in combined_dataset:
            if "Title" in element:
                movie_titles.append(element["Title"])

    movie_titles.sort()  # sorting the titles
    return movie_titles


print(getMovieTitles("man"))