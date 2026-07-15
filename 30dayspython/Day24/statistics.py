# statstics is the collection of the organization, interpretation, analysing & presentation of the data


# Data is the set of the characters, numbers, it can be  any format & stored in the some purpose
# Numpy is the core library computing in the python,it multidimensional array object computing with the arrays;


import numpy as np

print("Numpy Version",np.__version__)

python_list=[1,2,3,4,5,6];
print(type(python_list))

# to convert the list to the array we can use the  np.array(lis)


two_dimensional =  np.array(python_list);
print(two_dimensional)
print(type(two_dimensional))

# creating the array to the float
two_dimensional_float = np.array(python_list,dtype=float);
print(two_dimensional_float)


# creating the boolean type arrays
two_dimensional_bool = np.array([0,1,-1,0,2,-1,-1],dtype=bool)
print(two_dimensional_bool)

# creating the multidimensional array using the np
multidimensional = np.array([[0,1,2],[2,3,4],[4,5,6]]);
print(multidimensional*2);

# converting the multidimensional array to the list

listdata =  two_dimensional.tolist();
print(type(listdata))
print(listdata)

# shape of the array means if the array is the one dimensional it will return the size of the array, 
# if the array is the 2 dimensional it will return the row X columns 

# print(multidimensional)
# print(multidimensional.shape);

threebyfour=np.array([[0,1,2,4],[2,3,4,9],[5,6,7,1]]);
print(threebyfour)
print(threebyfour.shape)


# size will display the size of the array
print(two_dimensional.size)
print(multidimensional.size)
print(threebyfour.size)



# Mathematical operation using the numpy 
print(two_dimensional+10);
print(two_dimensional-10);
print(two_dimensional*10);
print(two_dimensional//10);
print(two_dimensional**10);



# getting the items from the 2 dimensional array
print("First Row",multidimensional[0])
print("Second Row",multidimensional[1])
print("THird row",multidimensional[2])

# getting the columns
print("First Column ",multidimensional[:,0])
print("First Column ",multidimensional[:,1])
print("First Column ",multidimensional[:,2])


# slicing the multidimensional array itmes
print(multidimensional)
# print(multidimensional[0:2])
# print("first two_rows & Columns ",multidimensional[0:2,0:2])


# two reverse the array
print(multidimensional[::-1])


# generating the random numbers
randval = np.random.randint(0,11);
print(randval)



# arange are used to the  we need to use in this format
# (start,step,stop)

evenum = np.arange(0,20,2);
print(evenum)