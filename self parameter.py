class Dog:
    def __init__(self, name, age):  
        self.name = name 
        self.age = age
    def bark(self): 
        print(f"{self.name} is barking!")
dog1 = Dog("Buddy", 3)
dog1.bark()
