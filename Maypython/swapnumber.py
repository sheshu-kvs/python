# Swap numbers
a=230;
b=223;
temp=0;

temp=a;
a=b;
b=temp;

print("\nA Value:",a,"\nB Value:",b);


# Even/odd
print("Printing the Even or Odd Number")
val = [1,2,3,4,5,5,8];
for i in range(len(val)):
    if(val[i]%2==0):
        print("Even Number",val[i]);
    else:
        print("Odd Number",val[i]);


# Positive/negative
print("printing the Greatest of Two Number ")
a=12;
b=210;
if(a>b):
    print("a is greater");
else:
    print("b is greater");


