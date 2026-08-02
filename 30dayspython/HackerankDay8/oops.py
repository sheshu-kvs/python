# Class
# a class consits of the variables & methods, an class is the blueprint of the object, it is imaginary
# for example Car , an car can start ,stop, accelarate
# for example i am can walk, run, sleep, dance



# an object is the instance of the class , it is real
# bmw,sheshadri,audi this all are the object

# __init__(constructor in the python when object is created it will directly call the consturctor)
# self it is the currently executing object

class Car:
    def __init__(self,color):
        self.color=color;
    
    def show(self,name,age,class1):
        self.name=name;
        self.age=age;
        self.class1=class1;


# c1=Car("black");
c2=Car();
print(c2.show("deva",12,12));
# print(val)