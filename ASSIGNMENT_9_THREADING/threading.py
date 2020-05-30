# -*- coding: utf-8 -*-
"""
Created on Sat May 30 11:51:36 2020

@author: suraj gavali
"""

from time import sleep
from threading import *





class hello(Thread):
    def run(self):
        for i in range(5):
            print("hello")
            sleep(1)



class hi(Thread):
    def run(self):
        for i in range(5):
            print("hi")
            sleep(1)


o1 = hello()
o2 = hi()

o1.start()
sleep(0.2)
o2.start()


o1.join()
o2.join()
print()
print("thread o1 and o2 are joined to main thread............")