import bluetooth
import socket
from picamera import PiCamera


server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )

port = 1
server_sock.bind(("",port))
server_sock.listen(1)

client_sock,address = server_sock.accept()

camera=PiCamera()
camera.resolution = (640,480)
camera.framerate = 90
camera.start_preview()

while True:

    data = client_sock.recv(1024)
    print "received [%s]" % data

    if data== "s":
        camera.start_recording('/home/pi/video.h264')
    elif data=="e":
        camera.stop_recording()
        camera.stop_preview()
        break

client_sock.close()
server_sock.close()
