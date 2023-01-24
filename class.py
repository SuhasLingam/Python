#classes and objects

class car:
    somename = "Supercars"
    
    def __init__(self,name,speed,cost):
        self.name = name
        self.speed = speed
        self.cost = cost

x = car("Supra" , 280 , 75)        
y = car("lambo" , 300 , 12)

print(x.name)
print(y.name)

print(x.speed)
print(y.speed)

print(x.cost)
print(y.cost)


    
