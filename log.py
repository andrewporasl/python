import time

def timestamp(a):
    def theFunc():
        print(time.ctime())
    return theFunc