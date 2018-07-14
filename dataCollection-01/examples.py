#!/usr/bin/env python3

import requests
import pandas as pd 
import json
from bs4 import BeautifulSoup
import re

def issuing_http_queries():
    response = requests.get("http://www.datasciencecourse.org")

    # some relevant fields"
    print("response.status_code: {}".format(response.status_code))
    # print("response.content: {}".format(response.content))
    # print("response.headers: {}".format(response.headers))
    print("response.headers['Content-Type']: {}".format(response.headers['Content-Type']))

def http_request_basics():
    params = {"sa":"t", "rct":"j", "q":"", "esrc":"s","source":"web", "cd":"9", "cad":"rja", "uact":"8"}
    response = requests.get("http://www.google.com/url",params = params)
    print(response.status_code)
    
def querying_resful_api():
    """using access_token, use this link https://github.com/settings/tokens/new to generate new access token
       or use user / password to access
    """
    token = ""
    response = requests.get("https://api.github.com/user",
                           params={"access_token": token})

    # response = requests.get("https://api.github.com/user",
    #                        auth=('chidamnat','password'))
    print(response.text)

def read_csv():
    dataframe = pd.read_csv("D:\code\practicalDS\dataCollection-01\course_roster.csv", delimiter=',', quotechar='"')
    # print(dataframe.head())

def parsing_json():
    """ load json from a REST API call"""
    response = requests.get("https://api.github.com/user",
                            auth=('chidamnat','password'))
    data = json.loads(response.text)  # loads from a JSON string
    print("data = {}".format(data))
    # json.load(file)                   # load json from file
    # json.dumps(obj)                   # return json string
    file = open("output1.txt","w")
    json.dump(data, file)              # write json to file
    file.close()

def parse_xml_html():
    response = requests.get("https://www.datasciencecourse.org/2016")
    root = BeautifulSoup(response.text,"html.parser")
    resp = root.find("section",id="schedule")\
        .find("table").find("tbody").findAll("a")
    return resp

def parse_reg_exp():
    text = """This course will introduce the basics of data science.
    ml is not data science. etl is not data science
    statistics is not data science"""
    match = re.match(r"data science", text)   # check if the start of the text matches
    match = re.search(r"data science",text)   # find the first occurance of the string "data science"
    for match in re.finditer("data science", text):
        print(match.start())

    all_matches = re.findall(r"data science", text)  # return all matches
    ### compiled version of regular expression ###
    regex = re.compile(r"data science")
    # regex.match(text, [startpos, [endpos]])
    # regex.search(...)
    # regex.finditer(...)
    # regex.findall(...)

    ## Grouping
    match = re.search(r"(\w+)\s([Ss]cience)",text)
    print(match.start(), match.groups())

    ## substitution
    better_text = re.sub(r"data science", r"schmada science", text)
    better_text = re.sub(r"(\w+)\s([Ss])cience", r"\1 \2hmience", text)
    

def main():
    issuing_http_queries()
    http_request_basics()
    #querying_resful_api()
    read_csv()
    #parsing_json()
    print(parse_xml_html())
    parse_reg_exp()

if __name__ == '__main__':
    main()
