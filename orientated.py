class fruit:
    print("My favorate fruits are Mango,Grapes,Kiwi.")
obj=fruit()
# Write a program to create a class Parrot and perform the following tasks - Create a class variable species,
#  Create a constructor that has instance variables - name and age, Create instances of class Parrot,
#   passing arguments as well, Print Class variable by accessing it, Print Instance variables as well.
class parrot:
    species="bird"
    def __init__(self, name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name)
        print(self.age)
oge=parrot("sravan",10)
oge.display()
class student:
    def __init__(self,name,grade):
       self.name=name
       self.grade=grade
    def display(self):
        print(self.name)
        print(self.aggrade)
abc=student("Advaith",10)
abc.display()