# Find the length of a list (without using len())
a=[1,2,3,4,4,4,23,23]
count=0;
for x in range(len(a)):
    count = count + 1;
print("the length of the list ",count)


# Find the maximum and minimum element in a list
b = [1,2,3,21,32,43]
max=0;
min=b[0];

for i in range(len(b)):
    if(b[i]>max):
        max=b[i];
  

print(max)
print(min)

# Sum all elements in a list
b = [1,2,3,21,32,43];
sum=0;
for i in range(len(b)):
     sum = sum+b[i];
print(sum)
