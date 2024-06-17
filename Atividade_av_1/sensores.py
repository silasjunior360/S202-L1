import random
import time

class Sensor:
    def __init__(self, name):
        self.name = name

    def Temp_aleatoria(self):
        return round(random.uniform(30, 40), 2)

    def Temperatura(self, db):
        while True:
            temperature = self.Temp_aleatoria()

            db.update_sensor_data(self.name, temperature)

            print(f"{self.name}: {temperature} Graus Celsius")

            if temperature > 38:
                print(f"Atencao! Temperatura muito alta! Verificar {self.name}!")
                db.set_sensor_alarm(self.name)
                break

            time.sleep(1)
