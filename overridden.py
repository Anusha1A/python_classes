class Animal:
    def example(self):
        print('Hello, I am the parent class')
class Dog(Animal):
    def example(self):
        print('Hello, I am the child class')
r = Dog()
r.example()
r = Animal()
r.example()