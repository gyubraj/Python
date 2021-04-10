import threading
import time

def helloworld():
    for x in range(10):
        print("Hello world")
        time.sleep(1)

def hellonext():
    for x in range(10):
        print("Hello Hello")
        time.sleep(1)


t1=threading.Thread(target=helloworld)
t2=threading.Thread(target=hellonext)

t1.start()

# t1.join()

t2.start()