print (3=="3")
print (id(3))
print (3 is 3)
print (type(3))
print (isinstance(3, int))


def test(a=1, b=2, c=3):
    print(a+b+c)
    
test(1)

a = lambda n, x: print(x+n)
a(2,2)


# print(locals())
# print(globals())

b = "Hello"
print(b[-1])
# print(b[10])
# b[0]= "J"
b= "jello"
print(b) 
print(f"Line {b}")

# listen
a= [1,2,"a"]
print(a)
a[0] = 2 
print(a)


# Dictionaries
priceDict = {"mehl": 99, "butter":122} 
print(priceDict)
print(priceDict["butter"])
print(priceDict.keys)


# schleifen

for x in a:
    print(x)

x = 0
while (x<2):
    print("jado")
    x+=1

# break, continue

class HelloWorld:
    def __init__(self) -> None:
        print("Hello World in Class")
    def test(self):
        print("test")
        

HelloWorld()

# Modules
import abModule

abModule.a()
abModule.b()


# Zufalls Module
import random
test = random.Random()
print(test.random())
print(random.randint(0,3))



# Files .. (see presentation)



# input

a = input("Name:")


# exceptions:



