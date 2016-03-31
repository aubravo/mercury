#!/usr/bin/python

import XboxController
import socket
import sys

HOSTNAME_ = socket.gethostbyname(socket.gethostname())
PORT_ = 5550

class Comms:
    def __init__ (self):
        self.HOST = HOSTNAME_
        self.PORT = PORT_
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.sock.connect ((self.HOST,self.PORT))

    def rotationCallback(self,value):
        self.sock.sendall ("T%0.3f"%(value))

    def accelCallback(self,value):
        self.sock.sendall ("A%0.3f"%(value))

    def gripperCallback(self,value):
        self.sock.sendall ("C%0.3f"%(value))

    def gripperReleaseCallback(self,value):
        self.sock.sendall ("R%0d"%(value))

    def close(self):
        self.sock.close()

class Kontrol:
    def __init__ (self):
        try:
            Controller = XboxController.XboxController(joystickNo = 0,
            deadzone = 0.1,
            scale = 5,
            invertYAxis = True)

            Komms = Comms()
            while (True):
                try:
                    Komms.connect()
                    break
                except:
                    print "Could not connect"

            Controller.setupControlCallback(Controller.XboxControls.LTHUMBX, Komms.rotationCallback)
            Controller.setupControlCallback(Controller.XboxControls.RTRIGGER, Komms.accelCallback)
            Controller.setupControlCallback(Controller.XboxControls.LTRIGGER, Komms.gripperCallback)
            Controller.setupControlCallback(Controller.XboxControls.LB, Komms.gripperReleaseCallback)

            Controller.start()
        except KeyboardInterrupt:
            Controller.stop()
            Komms.close()

if __name__ == '__main__':
    control = Kontrol()
