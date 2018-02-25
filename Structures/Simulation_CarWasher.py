from pythonds.basic.queue import Queue
import random

class Washer:
    def __init__(self,ppm):
        ...
    def tisk(self):
        ...
    def buzy(self):
        ...
    def startNext(self):
        ...

class Task:
    def __init__(self,task):
        ...
    def getStamp(self):
        ...
    def getCars(self):
        ...

    def simulation(numSeconds, carsPerMinute):
        labprinter = Washer(carsPerMinute)
        printQueue = Queue()
        waitingtimes = []