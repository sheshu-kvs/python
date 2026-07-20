

# An List Comprehension is the shorter more readble way 
# to create the list

# printing the square nums
# using the for loop
lis=[1,2,3,4]
for i in range(len(lis)):
    print(lis[i]*lis[i])

# Using the list comprehension
lisval = [i*i for i in range(len(lis))]
print(lisval)

# convert the name to the uppercase
strval=['morris','marry','divya','jyothi'];
upperval = [item .upper() for item in strval if "a" in item]
print(upperval)

# length of the each word
lenval = [len(item) for item in strval]
print(lenval);

# printing the even num
evenum = [i for i in range(len(lisval)) if i%2 ==0]
print(evenum);


# printing the pairs with the normal loop
newlis=[];
for i in range(3):
    for j in range(3):
        newlis.append((i,j));

# print(newlis)


lispairs=[(i,j) for i in range(3) for j  in range(3)]
for i,j in lispairs:
    print(i,j);

i=int(input('Enter the num1 '));
j=int(input('Enter the num2 '));
k=int(input('Enter the num3 '));
n=int(input('Enter the N value'));
numlis=[(num1,num2,num3) for num1 in range(i) for num2 in range(j) for num3 in range(k)]
sum=0;
for (num1,num2,num3) in  numlis:
    sum=num1+num2+num3;
    if(sum  == n):
        print(num1,num2,num3)