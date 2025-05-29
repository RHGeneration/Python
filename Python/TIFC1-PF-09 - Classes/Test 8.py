class Cat():
    #an attempt to model a cat
    def __init__(self, name, age):
        #assign the cats name and age
        self.name = name
        self.age = age

    def sleep(self):
        #Cat is sleeping
        print(f"{self.name} is sleeping soundly")

    def climb(self):
        #The cat can sleep
        print(f"Quick! {self.name} is climbing on the roof!")
        

