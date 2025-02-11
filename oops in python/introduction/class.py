class Dog:
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed

      
    def bark(self):
        print("woof woof")
dog1 =Dog("bruce","lol")
dog1.bark()
print(dog1.breed)
print(dog1.name)