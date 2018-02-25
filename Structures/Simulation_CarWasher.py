from pythonds.basic.queue import Queue
import random

class Washer:
    def __init__(self,ppm):
        self.carerateerate = ppm
        self.currentTask = None
        self.timeRemaining = 0
    def tisk(self):
        if self.currentTask == None:
            self.timeRemaining = self.timeRemaining - 1
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
        w = Washer(carsPerMinute)
        washQueue = Queue()
        waitingtimes = []