# An  Higherorderfunction, Accepts the Function as the argument, returns the function  

def square(x):
    return x**2;


# returning the function
def highorderfunction(type):
    if type == 'square':
        return square;


res=highorderfunction("square");
print(res(2));



def shout(txt):
    return txt.upper();

def run_tool(func,val):
    return func(val);


# passing the function as the argument
print(run_tool(shout,"hello"))


# Closure

# A Python Closure are used to the outer scope of the function we can use
def add():
    num=10;
    def addnum(val):
        return val+num;
    return addnum

res = add();
print(res(5))