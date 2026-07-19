class Flyable:
    def fly(self):
        print(f"{self.__class__.__name__} is flying")

class Swimmable:
    def swim(self):
        print(f"{self.__class__.__name__} is swimming")

class Runnable:
    def run(self):
        print(f"{self.__class__.__name__} is running")

class Duck(Flyable, Swimmable, Runnable):
    def quack(self):
        print("Quack!")

class FlyingFish(Flyable, Swimmable):
    pass

duck = Duck()
duck.fly()
duck.swim()
duck.run()
duck.quack()

fish = FlyingFish()
fish.fly()
fish.swim()

print(Duck.__mro__)
