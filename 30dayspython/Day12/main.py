# Module
# A set of the Code & Function are used in the module 

import Day12.Mymodule as Mymodule
print(Mymodule.generate_full_name("sheshadri","kumar"))

# Import Function From the MyModule
from Day12.Mymodule import generate_full_name
print(generate_full_name("Deva","Durga"))

# During the Import Function We Can rename the module

from Day12.Mymodule import generate_full_name as fullname
print(fullname("Manisha","Varma"));


# OS Module
# Using the Os Module we can create, get the directory,  the
import os

# Creating the Directory
# print(os.mkdir("newdir"));

# Getting the Current Directory details
print(os.getcwd());

# os.chdir("newdir12")

# os.rmdir("newdir")

# Using the Stastics
from statistics import*
ages=[20,20,2,24,25,22,26,20,23,22,26];
print(mean(ages));
print(median(ages)); 
print(mode(ages)); 
print(stdev(ages)); 

# Math Module Contains Many Mathematical Operations
import math
print(math.pi)
print(math.sqrt(2))
print(math.pow(2,3))



from math import pi,sqrt
# or
from math import *    
# Which Imports all the Math Modules
print(math.pi)
print(math.sqrt(2))
print(math.pow(2,3))



import random

print(random.randint(5,10));
print(random.randrange(100,120));


import random
print(random.randint(100000,999999));




