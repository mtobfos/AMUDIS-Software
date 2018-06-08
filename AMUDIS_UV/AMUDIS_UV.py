import datetime
import matplotlib.pyplot as plt
import netCDF4 as nc
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import time as tm
import os
from picam import *
from GUI import AMUDIS_GUI as GUI

cam = picam()
cwd = os.getcwd()


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
        self.ui.takePictureButton.clicked.connect(self.Camera.take_picture)
        self.ui.pushButtonLoadSettings.clicked.connect(self.load_setting)
        self.ui.startButton.clicked.connect(self.timed_measurement)


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
        cam.setParameter("ReadoutControlMode", PicamReadoutControlMode["FullFrame"])
        # send configuration
        cam.sendConfiguration()
        print("Sensor temperature: {}\nExposure time: {}\nParameters loaded".
              format(sensorTemperature, exposure))


    def timed_measurement(self):

        initial_time = self.ui.dateTimeEdit_begin.dateTime().toPyDateTime()
        end_time = self.ui.dateTimeEdit_end.dateTime().toPyDateTime()
        lcd = self.ui.lcdNumber

        self.timed = TimedMeasurement(initial_time, end_time, lcd)
        self.thread = QtCore.QThread()
        self.timed.moveToThread(self.thread)
        self.timed.started.connect(self.timed.run)
        self.timed.start()


class TimedMeasurement(QtCore.QThread):

    def __init__(self, initial_time, end_time, lcd):
        super(TimedMeasurement, self).__init__()

        self.initial_time = initial_time
        self.end_time = end_time
        self.lcd = lcd


    def run(self):
        """ """
        self.Camera = Camera()

        print(self.initial_time)
        meas_time = self.initial_time
        step = 4 # seconds
        cnt = 0

        while self.end_time >= meas_time:
            time_now = datetime.datetime.now()
            if time_now >= self.end_time:
                print("Write a valid initial time")
                break
            elif time_now < self.initial_time:
                tm.sleep(1)
                print('waiting initial time {},{}'.format(self.initial_time, time_now))
            else:
                if meas_time - datetime.timedelta(seconds=step) <= time_now:
                    self.Camera.take_picture(False)
                    print("measuring, ", meas_time)      # %run nir.py
                    meas_time += datetime.timedelta(seconds=step)
                    self.lcd.display(cnt)
                    cnt += 1
                else:
                    pass

        print('Measurement completed')


class Camera:

    def __init__(self):
        pass

    @staticmethod
    def read_sensor():
        foto = cam.readNFrames(1, timeout=20000)
        return foto[0][0]

    def take_picture(self, show=True):
        image = self.read_sensor()

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
        name = name.strftime('%Y%m%d_%H%M%S')

        with nc.Dataset(cwd + '/data/data_{}.nc'.format(name), 'w', format='NETCDF4') as data:
            # create Dimensions
            data.createDimension('axisDim', 1024)
            data.createDimension('dataDim', 1048576)
            # add variables
            data.set_fill_off()
            datos = data.createVariable('Data', 'f4', ('dataDim',))
            datos[:] = image

            xaxis = data.createVariable('xAxis', 'f4', ('axisDim',))
            xaxis[:] = np.arange(0, 1024)

            # add global attributes
            date = datetime.datetime.now().date()
            date = date.strftime('%d.%m.%Y')

            time = datetime.datetime.now().time()
            time = time.strftime('%H:%M:%S.%f')

            data.RecordDate = date
            data.RecordTime = time
            data.Setup = "UV"
            data.ExposureTime = cam.getParameter('ExposureTime')
            data.DetectorTemperature = cam.getParameter('SensorTemperatureReading')
            data.NoOfAccumulations = '1' # to modify
            data.Averaged = '1'
            data.Shutter = '1'
            data.xDim = "1024"
            data.yDim = "1024"


if __name__ == "__main__":
    Program = QtWidgets.QApplication(sys.argv)
    AMUDIS_run = AMUDIS_control()
    AMUDIS_run.show()
    sys.exit(Program.exec_())
