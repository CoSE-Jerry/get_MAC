from picamera import PiCamera
from time import sleep
import os

while True:
    camera = PiCamera()
    camera.start_preview()
    sleep(3600)
    camera.stop_preview()
 
