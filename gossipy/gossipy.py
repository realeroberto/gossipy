import socket
import threading
import time

class gossipy(object):
        def send(self):
            while True:
                msg = input('\nLOCAL > ')
                if msg and len(msg) > 0:
                    self.sender(msg)

        def receive(self):
            while True:
                msg = self.receiver()
                for m in msg:
                    print('\nREMOTE > ' + m)
                time.sleep(self.delay)

        def start(self):
            thread_send = threading.Thread(target = self.send)
            thread_receive = threading.Thread(target = self.receive)
            thread_send.start()
            thread_receive.start()

        def __init__(self, sender, receiver, delay=1):
            self.sender = sender
            self.receiver = receiver
            self.delay = delay


# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
