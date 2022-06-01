from curses.ascii import isdigit
from unittest import result


def getTheNumber(txt):
    digits = [int(s) for s in txt.split() if s.isdigit()]
    return digits[-1]

def checkIfNumber(txt):
    onlyDigits = True
    for char in txt:
        if(not char.isdigit()):
            onlyDigits = False
            return onlyDigits
        return onlyDigits

i=0
while(True):
    if(i==0):
        input0 = input("What is your first number?")
        if(not checkIfNumber(input0)):
            print("Wrong Input, Please give a number")
            break
            
    elif(i==1):
        input1 = input("What do you want to do next? (add, sub, mul, div)")
        if("add" in input1):
            result = int(input0) + getTheNumber(input1)
            print(result)
        elif("sub" in input1):
            result = int(input0) - getTheNumber(input1)
            print(result)        
        elif("mul" in input1):
            result = int(input0) * getTheNumber(input1)
            print(result)
        elif("div" in input1):
            if(getTheNumber(input1)==0):
                print("Cant divide by Zero")
                break
            else:
                result = int(input0) / getTheNumber(input1)
                print(result)        
        else:
            print("Wrong input!!")
            print("What do you want to do next?")
            
    else:
        input2 = input("What do you want to do next? (add, sub, mul, div)")
        if("add" in input2):
            result += getTheNumber(input2)
            print(result)
        elif("sub" in input2):
            result -= getTheNumber(input2)
            print(result)        
        elif("mul" in input2):
            result *= getTheNumber(input2)
            print(result)
        elif("div" in input2):
            if(getTheNumber(input2)==0):
                print("Cant divide by Zero")
                break
            else:
                result /= getTheNumber(input2)
                print(result)        
        else:
            print("Wrong input!!")
            print("What do you want to do next?")
        
    i+=1
        
    
    
