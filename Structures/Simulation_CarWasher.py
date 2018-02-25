from pythonds.basic.queue import Queue
import random

class Washer:
    def __init__(self,ppm):
        self.carerateerate = ppm
        self.currentTask = None
        self.timeRemaining = 0
    def tisk(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
    def buzy(self):
        if self.currentTask != None:
            return True
        else:
            return False
    def startNext(self,newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getCars() * 60 / self.carerateerate


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