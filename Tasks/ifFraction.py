number=input('please')

def getUp(number):


    if number.__contains__('/'):
        new=number.split('/')
        print("Числитель", new[0])
        print("Знаменатель", new[1])
    else:
        print("Это не дробь!")


getUp(number)