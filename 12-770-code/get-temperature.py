from w1thermsensor import W1ThermSensor, Sensor

for sensor in W1ThermSensor.get_available_sensors([Sensor.DS18B20]):
    print("Sensor %s has temperature %.2f" % (sensor.id, sensor.get_temperature()))
