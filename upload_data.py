# from pymongo.mongo_client import MongoClient
# import pandas as pd
# import json

# #create a new client and connectt to server
# from urllib.parse import quote_plus
# from pymongo import MongoClient

# username = quote_plus("ajjit1")
# password = quote_plus("VKfdYYCZOPPixgPR")

# url = f"mongodb+srv://{username}:{password}@cluster0.vwv6s.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# client = MongoClient(url)


# #create database name and collection name
# DATABASE_NAME="pwskills"
# COLLECTION_NAME='waferfault'

# df=pd.read_csv("D:\wefer_detection_project\notebooks\wafer_23012020_041211.csv")

# df=df.drop("Unnamed: 0",axis=1)

# json_record=list(json.loads(df.T.to_json()).values())

# client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)


from pymongo import MongoClient
from urllib.parse import quote_plus
import pandas as pd
import json

# MongoDB credentials and connection string
username = quote_plus("ajjit1")
password = quote_plus("VKfdYYCZOPPixgPR")

url = f"mongodb+srv://{username}:{password}@cluster0.vwv6s.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(url)

# Database and collection names
DATABASE_NAME = "pwskills"
COLLECTION_NAME = "waferfault"

# Load the CSV file
csv_path = r"D:\wefer_detection_project\notebooks\wafer_23012020_041211.csv"
df = pd.read_csv(csv_path)

# Drop unnecessary column if it exists
if "Unnamed: 0" in df.columns:
    df = df.drop("Unnamed: 0", axis=1)

# Convert DataFrame to JSON records
json_records = json.loads(df.to_json(orient='records'))

# Insert into MongoDB
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_records)

print(f"{len(json_records)} records inserted into '{DATABASE_NAME}.{COLLECTION_NAME}' collection.")
