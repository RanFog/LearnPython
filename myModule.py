#import mypackage.utilits #Вариант 1
#from mypackage.utilits import multiply
from mypackage.utilits import *

#print(mypackage)
if __name__ == "__main__":
    print ("Hello")

print (__name__)
#print (mypackage.utilits.multiply(4,5)) #Вариант 1
print (multiply(4,5))

#import this
#import inspect
#inspect.getfile(this)
#>> 'C:\\Python37\\lib\\this.py'
#import os
#os.listdir ("C:\\Python37\\lib")