#!/usr/bin/python

from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from datetime import datetime as dt
from csv import writer
import time

sense = SenseHat()
sense.set_imu_config(True, True, True)  # accelerometer, magnetometer , gyroscope
sense.clear()


def get_sense_data():
    sense_data = []
    temperature = round(sense.get_temperature(), 2)
    pressure = round(sense.get_pressure(), 2)
    humidity = round(sense.get_humidity(), 2)
    sense_data.append(temperature)
    sense_data.append(pressure)
    sense_data.append(humidity)

    mag = sense.get_compass_raw()
    mag_x = round(mag["x"], 2)
    mag_y = round(mag["y"], 2)
    mag_z = round(mag["z"], 2)
    sense_data.append(mag_x)
    sense_data.append(mag_y)
    sense_data.append(mag_z)

    acc = sense.get_accelerometer_raw()
    acc_x = round(acc["x"], 3)
    acc_y = round(acc["y"], 3)
    acc_z = round(acc["z"], 3)
    sense_data.append(acc_x)
    sense_data.append(acc_y)
    sense_data.append(acc_z)

    gyro = sense.get_orientation()
    pitch = round(gyro["pitch"], 2)
    roll = round(gyro["roll"], 2)
    yaw = round(gyro["yaw"], 2)
    sense_data.append(pitch)
    sense_data.append(roll)
    sense_data.append(yaw)

    sense_data.append(dt.now())

    return sense_data


while True:
    start_time = dt.now()
    time_stamp = dt.strftime(start_time, '%Y%m%d%H%M%S')
    file_name = '/home/faisal/sense_data/{}.csv'.format(time_stamp)
    with open(file_name, 'w', newline='') as f:
        data_writer = writer(f)
        data_writer.writerow(['temp', 'pres', 'hum',
                              'mag_x', 'mag_y', 'mag_z',
                              'acc_x', 'acc_y', 'acc_z',
                              'pitch', 'roll', 'yaw',
                              'datetime'])
        while True:
            data = get_sense_data()
            data_writer.writerow(data)
            if (dt.now() - start_time).total_seconds() >= 60:
                break
            time.sleep(0.1)
