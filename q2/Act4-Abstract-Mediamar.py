from abc import ABC, abstractmethod

class Sensor(ABC):
    @abstractmethod
    def get_reading(self):
        pass

class PHSensor(Sensor):
#    def __init__(self):
#        super().__init__()

    def get_reading(self):
        return 7.2

class TempSensor(Sensor):
#    def __init__(self):
#        super().__init__()

    def get_reading(self):
        return 24.5

pH_sensor = PHSensor()
my_sensor = TempSensor()
#my_sensor = Sensor()

print("   ")
print("--- Lab Inventory System ---")
print(f"[pH Sensor] Reading: {pH_sensor.get_reading()} (Neutral)")
print(f"[Temperature Sensor] Reading: {my_sensor.get_reading()}°C")
print("   ")
print("----------------------------")
print("   ")