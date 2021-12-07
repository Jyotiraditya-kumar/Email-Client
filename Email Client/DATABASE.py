import pymongo
from pymongo import MongoClient

class EmailDatabase:
    def __init__(self,userId):
        self.connection = MongoClient(host="localhost",port=27017)
        self.database=self.connection["Email-Application"]
        self.collection=self.database[f"{userId}"]
    def Insert_Data(self,data):
        self.collection.insert_one(data)
    def fetch(self,query={},fields={}):
        x=self.collection.find(query,fields)
        return(x)
    def Close(self):
        self.connection.close()
    # def Insert_Dta


if __name__=="__main__":
    a=EmailDatabase("tyagi")
    # query={"_id":"17d393aa85f6a3ea"}
    # a.Insert_Data(query)
    print(list(a.fetch()))
    a.Close()
