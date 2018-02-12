import time

from gossipy import gossipy

def send_to_file(msg):
    global path
    with open(path, "a") as f:
        f.write(str(int(time.time())) + ':' + msg + "\n")

def receive_from_file():
    global path
    global timenow
    msg = []
    with open(path, "r") as f:
        for line in f.readlines():
            t, s = line.split(':')
            if int(t) > timenow:
                msg.append(s)
                timenow = int(t)
    return msg
    
    
timenow = 0
path = "/tmp/gossipy"

def main():
    chat = gossipy.gossipy(send_to_file, receive_from_file)
    chat.start()

if __name__ == "__main__":
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
