# list with 5  numbers 
a=[10,20,30,450]
print(a);


# count the number of the items in the list
count=0;
for i in a:
    print(i)
    count = count+1;
print(count);

# add an element end of list
b=[12,34,5,45,23,45]
print(b.append(100));
print(b)


# remove an element b value
# range will give the index;
# for i in b: it will give the directly item
# remove an item by the value
b=[12,34,5,45,23,45];
for i in range(len(b)):
    if(b[i]==23):
        continue;
    else:
        print(b[i]);


# sum of the list 
c=[1,2,3,4,5];
print(c)
sum=0;
for i in c:
    sum=sum+i;
print("the sum of the list ",sum);