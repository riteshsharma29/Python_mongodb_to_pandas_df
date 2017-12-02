#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import os
import sys
import pymongo
from pymongo import MongoClient

reload(sys)
sys.setdefaultencoding("utf-8")

#function to download sample mongodb
def downld_mongo_sample():
    os.system('wget http://media.mongodb.org/zips.json')
    os.system('chmod -R 777 zips.json')


#function to convert mongodb collection into a pandas dataframe
def create_df(jsonfile):
    try:
        df = pd.read_json(jsonfile,lines=True)
        #myexcel = df.to_excel('mongo_sample.xlsx')
        csvfile = jsonfile.split(".")
        mycsv = df.to_csv(csvfile[0] + '.csv')      
    except Exception as e:
        print e

#function to export Mongodb collections into json files
def export_mongo():
#creating instance of a class pymongo
    client = MongoClient()
#connecting to a mongodb Northwind database [Replace with your desired mongodb database]
    db = client.Northwind
    for collection in db.collection_names():
        os.system('mongoexport -d  Northwind -c ' + collection + ' -o ' + collection + '.json')     
        #print collection
        create_df(collection + '.json')
        os.remove(collection + '.json')

export_mongo()

