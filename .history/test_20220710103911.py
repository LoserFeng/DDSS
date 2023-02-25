import threading
import sys
import os

def query_by_id(user_id):
    print('123')

def query_by_name(user_name):
    print('234')

class Controller(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)


    def run(self):
        sys.stdout = open(os.devnull, 'w')
        while(True):
            print("Controller")
      
            
    def stop():
        threading.Thread._stop()


class Controller1(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)


    def run(self):
        while(True):
            print("Controller1")
      
            
    def stop():
        threading.Thread._stop()


def main():
    a=Controller()
    b=Controller1()
    a.start()
    b.start()
    

    print("1111111")


    print("2222222")
  
    sys.stdout = sys.__stdout__
    print("3333333")



if __name__ == '__main__':
    main()
