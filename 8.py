class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print(f"{self.name} makes sound")
class Dog(Animal):
    def __init__(self, name,breed):
        super().__init__(name)
        self.breed=breed
    def speak(self):
        print(f"{self.name} makes sound woof")
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    def speak(self):
        print(f"{self.name} makes sound meow")
c=Cat("snowball")
c.speak()
d=Dog('shiro','pup')
d.speak()
a=Animal('horse')
a.speak()
    
        