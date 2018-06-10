import datetime
import matplotlib.pyplot as plt
import netCDF4 as nc
from PyQt5 import QtCore, QtGui, QtWidgets
import time as tm
import numpy as np
import os

import sys

# path to camera modules
cwd = os.getcwd()

CAMERA_PATH = cwd

if not CAMERA_PATH in sys.path:
    sys.path.append(CAMERA_PATH)

from picam import *
from GUI import AMUDIS_GUI as GUI

cam = picam()


class AMUDIS_control(QtWidgets.QMainWindow):
    """Program to control AMUDIS camera"""

    def __init__(self):
        super(AMUDIS_control, self).__init__()

        self.ui = GUI.Ui_MainWindow()
        self.ui.setupUi(self)

        self.Camera = Camera()

        self.ui.actionQuit.triggered.connect(self.close_program)
        self.ui.actionInitialize_system.triggered.connect(self.initialize)
        self.ui.loadCamera.clicked.connect(self.loadCamera)
        self.ui.takePictureButton.clicked.connect(self.take_picture)
        self.ui.pushButtonLoadSettings.clicked.connect(self.load_setting)
        self.ui.startButton.clicked.connect(self.start)
        self.ui.stopButton.clicked.connect(self.stop)

        self.config = self.configuration()
        self.timed = TimedMeasurement(config=self.config)
        self.thread = QtCore.QThread()


    # Methods of class
    def close_program(self):
        """disconnect camera, unload libraries and close the programm"""
        cam.disconnect()
        cam.unloadLibrary()
        print("Program closed by user")
        sys.exit()

    def initialize(self):

        print("Loading program, wait 10 seconds ...")
        #tm.sleep(5)
        # initialize camera class and connect to library, look for available camera and connect to first one
        cam.loadLibrary(pathToLib="C:\Program Files\Common Files\Princeton Instruments\Picam\Runtime/")
        cam.getAvailableCameras()

    def loadCamera(self):
        # connect to camera
        print("connecting to camera...")
        cam.connect()
        print("connected")

    def load_setting(self):
        sensorTemperature = int(self.ui.TempSensorValue.text())
        cam.setParameter("SensorTemperatureSetPoint", sensorTemperature)
        # exposure
        exposure = int(self.ui.ExposureValue.text())
        cam.setParameter("ExposureTime", exposure)
        # cam.setParameter("ReadoutControlMode", PicamReadoutControlMode["FullFrame"])
        # send configuration
        cam.sendConfiguration()
        print("Sensor temperature: {}\nExposure time: {}\nParameters loaded".
              format(sensorTemperature, exposure))

    def configuration(self):

        initial_time = self.ui.dateTimeEdit_begin.dateTime().toPyDateTime()
        end_time = self.ui.dateTimeEdit_end.dateTime().toPyDateTime()
        lcd = self.ui.lcdNumber
        interval = int(self.ui.IntervalValue.text())
        average = int(self.ui.AverageValue.text())

        config = {'initial_time': initial_time,
                  'end_time': end_time,
                  'lcd': lcd,
                  'interval': interval,
                  'average': average}

        return config

    def take_picture(self):
        """ """
        average = int(self.ui.AverageValue.text())

        if self.ui.showPicture.isChecked() is True:
            self.Camera.take_picture(show=True, average=average)
        else:
            self.Camera.take_picture(show=False, average=average)

    def start(self):
        self.config = self.configuration()
        self.timed = TimedMeasurement(config=self.config)
        self.timed.moveToThread(self.thread)
        self.timed.started.connect(self.timed.run)
        self.timed.isRunning = True
        print('Starting measurements...')
        self.timed.start()

    def stop(self):
        self.timed.isRunning = False
        print("Stopping measurements...\n")


class TimedMeasurement(QtCore.QThread):

    def __init__(self, config):
        super(TimedMeasurement,  self).__init__()

        self.config = config
        self.Camera = Camera()
        self.isRunning = False

    def __del__(self):
        self.quit()
        self.wait()

    def run(self):
        """Run the schedule measurements """
        print(self.config['initial_time'])
        meas_time = self.config['initial_time']
        step = self.config['interval']  # seconds
        cnt = 0
        cnt_wait = 0

        while self.config['end_time'] >= meas_time:

            if self.isRunning is True:
                time_now = datetime.datetime.now()

                if time_now >= self.config['end_time']:
                    print("Write a valid initial time")
                    break

                elif time_now < self.config['initial_time']:
                    tm.sleep(0.1)

                    if (cnt_wait % 20) == 0:
                        print('waiting initial time {},{}'.format(self.config['initial_time'],
                                                                  time_now))
                    else:
                        pass
                    cnt_wait += 1

                else:
                    if meas_time - datetime.timedelta(seconds=step) <= time_now:
                        self.Camera.take_picture(show=False, average=self.config['average'])
                        print("measuring, ", meas_time)  # %run nir.py
                        meas_time += datetime.timedelta(seconds=step)
                        self.config['lcd'].display(cnt)
                        cnt += 1
                    else:
                        pass
            else:
                self.isRunning = False
                print('Measurements stopped by User\n')
                break


class Camera:

    def __init__(self):
        pass

    def read_sensor(self, average):
        foto = cam.readNFrames(average, timeout=20000)

        #np.average(foto[:][0])
        return foto[0][0]

    def take_picture(self, show, average):
        image = self.read_sensor(average)

        if show is True:
            plt.imshow(image, cmap='gray')
            plt.colorbar(cmap='gray')
            plt.show()
        else:
            pass
        # save data to netCDF4 file
        self.save_to_nc(image)
        print("Image saved")
        
    def save_to_nc(self, image):
        """ Saves """
        name = datetime.datetime.now()
        name = name.strftime('%Y_%m_%d_%H_%M_%S')

        with nc.Dataset('data/data_{}.nc'.format(name), 'w', format='NETCDF4') as data:
            # create Dimensions
            data.createDimension('axisDim', 640)
            data.createDimension('dataDim', 327680)
            # add variables
            data.set_fill_off()
            datos = data.createVariable('Data', 'f4', ('dataDim',))
            datos[:] = image

            xaxis = data.createVariable('xAxis', 'f4', ('axisDim',))
            xaxis[:] = np.arange(1, 641)

            # add global attributes
            date = datetime.datetime.now().date()
            date = date.strftime('%d.%m.%Y')

            time = datetime.datetime.now().time()
            time = time.strftime('%H:%M:%S.%f')

            data.RecordDate = date
            data.RecordTime = time
            data.Setup = "NIR"
            data.ExposureTime = cam.getParameter('ExposureTime')
            data.DetectorTemperature = cam.getParameter('SensorTemperatureReading')
            data.NoOfAccumulations = '1' # to modify
            data.Averaged = '1'
            data.Shutter = '1'
            data.xDim = "640"
            data.yDim = "512"


if __name__ == "__main__":
    Program = QtWidgets.QApplication(sys.argv)
    AMUDIS_run = AMUDIS_control()
    AMUDIS_run.show()
    sys.exit(Program.exec_())
