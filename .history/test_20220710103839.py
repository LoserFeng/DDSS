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
        sys.stdout = open(os.devnull, 'w')
        while(True):
            print("Controller")
      
            
    def stop():
        threading.Thread._stop()


def main():
    # while True:
    #     option = input('shh')
    #     if option == '1':
    #         user_id = input('asdd')
    #         query_by_id(user_id)
    #     elif option == '2':
    #         user_name = input('fassa')
    #         query_by_name(user_name)
    #     elif option == 'exit':
    #         print('125251125')
    #         break
    #     else:
    #         print('53253253')

    print("1111111")


    print("2222222")
  
    sys.stdout = sys.__stdout__
    print("3333333")



if __name__ == '__main__':
    main()
