import pymongo
from datetime import datetime, timedelta
from typing import Collection
import pymongo # pip install pymongo

class Database:
    def __init__(self, database, collection):
        self.connect(database, collection)

    def connect(self, database, collection):
        try:
            connectionString = "localhost:27017"
            self.clusterConnection = pymongo.MongoClient(
                connectionString,
                tlsAllowInvalidCertificates=True
            )
            self.db = self.clusterConnection[database]
            self.collection = self.db[collection]
            print("Conectado ao banco de dados com sucesso!")
        except Exception as e:
            print(e)

    def resetDatabase(self):
        try:
            self.db.drop_collection(self.collection)
            print("Banco de dados resetado com sucesso!")
        except Exception as e:
            print(e)

    def update_sensor_data(self, sensor_nome, temperatura):
        timestamp = datetime.utcnow()

        self.collection.update_one({"nomeSensor": sensor_nome}, 
                                   {"$set": {"valorSensor": temperatura, 
                                             "timestamp": timestamp},
                                    "$setOnInsert": {"sensorAlarmado": False}},
                                   upsert=True)

    def set_sensor_alarm(self, sensor_nome):
        self.collection.update_one({"nomeSensor": sensor_nome}, {"$set": {"sensorAlarmado": True}})

    def get_sensor_data_last_hour(self):
        hour_ago = datetime.utcnow() - timedelta(hours=1)
        return self.collection.find({"timestamp": {"$gt": hour_ago}})
