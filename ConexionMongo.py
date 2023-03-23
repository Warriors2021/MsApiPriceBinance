# Importar la clase MongoClient desde el módulo pymongo
from pymongo import MongoClient

# Importar la clase ScrapyBinance desde el módulo scrapy

from dotenv import load_dotenv
import os

load_dotenv()


class conexion_mongo:

    client = MongoClient(host= os.getenv("HOST_MONGO"))
    db = client[os.getenv("DB_MONGO")]


    def collection(self, nameCollection:str):


        self.nameCollection = nameCollection


        return self.db[self.nameCollection]
    
    