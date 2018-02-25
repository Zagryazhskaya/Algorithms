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

        for currentSecond in range(numSeconds):

            if newCar():
                task = Task(currentSecond)
                washQueue.enqueue(task)

            if (not w.busy()) and (not washQueue.isEmpty()):
                nexttask = washQueue.dequeue()
                waitingtimes.append(nexttask.waitTime(currentSecond))
                w.startNext(nexttask)

            w.tick()

        averageWait = sum(waitingtimes) / len(waitingtimes)
        print("Average Wait %6.2f secs %3d tasks remaining." % (averageWait, washQueue.size()))
