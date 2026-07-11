# A list comprehension is the used to create the new list 
# a list comprehension is faster than processing the for loop

# Convert the str to list
str="python";
# newls=list(str);
# print(newls);

# using the list comprehension we can use

lis= [i for i in str]
print(lis) 

# we can also generate the numbers
lis2 = [i for i in range(10)]
print(lis2)

# we can also perform the mathematical operation
# i,e multiply the each number
lis3 = [i*i for i in range(10)]
print(lis3)

# we can also use the if condition
# even numbers
lis4 = [i for i in range(21) if i%2 == 0]
print(lis4)
# odd numbers
lis5 = [i for i in range(21) if i %2 != 0]
print(lis5);

# Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
lis6 = [i for i in numbers if i<0]
print(lis6);

# # Flattening a two dimensional array
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

lis7= [row for number in list_of_lists for row in number]
print(lis7)


