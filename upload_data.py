from pymongo.mongo_client import MongoClient
import pandas as pd
import json

#create a new client and connectt to server
from urllib.parse import quote_plus
from pymongo import MongoClient

username = quote_plus("ajjit1")
password = quote_plus("VKfdYYCZOPPixgPR")

url = f"mongodb+srv://{username}:{password}@cluster0.vwv6s.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(url)


#create database name and collection name
DATABASE_NAME="pwskills"
COLLECTION_NAME='waferfault'

df=pd.read_csv("D:\wefer_detection_project\notebooks\wafer_23012020_041211.csv")

df=df.drop("Unnamed: 0",axis=1)

json_record=list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)