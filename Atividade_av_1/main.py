import threading
from sensores import Sensor
from database import Database


db = Database(database="Sensores", collection="Tempos")
sensores = ["Sensor_1", "Sensor_2", "Sensor_3"]

threads = []
for sensor_name in sensores:
        sensor = Sensor(sensor_name)
        thread = threading.Thread(target=sensor.Temperatura, args=(db,))
        threads.append(thread)
        thread.start()

for thread in threads:
        thread.join()
  
print("Ultima leitura do sensor:")
for data in db.get_sensor_data_last_hour():
        print(data)