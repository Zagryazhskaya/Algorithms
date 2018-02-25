from pythonds.basic.queue import Queue

import random

class Washer:
    def __init__(self, ppm):
        self.carerateerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self,newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getCars() * 60/self.carerateerate

class Task:
    def __init__(self,time):
        self.timestamp = time
        self.cars = random.randrange(1,21)

    def getStamp(self):
        return self.timestamp

    def getCars(self):
        return self.cars

    def waitTime(self, currenttime):
        return currenttime - self.timestamp


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
        waitingtimes.append( nexttask.waitTime(currentSecond))
        w.startNext(nexttask)

      w.tick()

    averageWait=sum(waitingtimes)/len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining."%(averageWait,washQueue.size()))

def newCar():
    num = random.randrange(1,181)
    if num == 180:
        return True
    else:
        return False

for i in range(10):
    simulation(3600,5)