# import sqlite3
import pymongo
from pymongo import MongoClient
import json
import os
from email.utils import parsedate_tz,mktime_tz
import datetime
# con=sqlite3.connect("Emails.db")
# cur = con.cursor()

Curr_dir="emails"
con=MongoClient(host="localhost",port=27017)
db=con["Email-Application"]

collcn=db.Emails2


# Create table
# cols=("From", "To","Date","Snippet")
# f="""CREATE TABLE "Messages" (
# 	"ID"	TEXT UNIQUE,
#     "Subject"  TEXT,
# 	"From"	TEXT NOT NULL,
# 	"To"	TEXT NOT NULL,
# 	"Date"	TEXT,
# 	"Snippet"	TEXT,
# 	PRIMARY KEY("ID")
# )"""


def get_headers(data,d):
    h={i['name']:i['value'] for i in  data['payload']["headers"]}
    header=("Date","Subject","From","To")
    alt={"From":"Bcc",}
    for i in header:
        try:
            d[i]=h[i]#.replace('"',"")
        except KeyError as e :
            if e.args[0]=="Subject":
                d[i]="No Subject"
            elif e.args[0]=="To":
                d[i]=h["Bcc"]
    return(d)
def Insert_Data():
    l=os.listdir(Curr_dir)
    for i in l:
        d={}
        with open(f"Emails/{i}") as f:
            data=json.load(f)
            d["_id"]=data["id"]
            # d["Labels"]=data["labelIds"]
            # print(i)
            # print(data)
            d=get_headers(data,d)
            # print(data)
            
            d["Snippet"]=data["snippet"]
            d["Labels"]=data["labelIds"]
            timestamp = mktime_tz(parsedate_tz(d["Date"]))
            d["Date"]=datetime.datetime.fromtimestamp(timestamp)
            collcn.insert_one(d)
            # query.
            # print(query)
            # print(d)
            # cur.execute(query)
            
            # print(d)
    # con.commit()

Insert_Data()
        

    
# con.close()