
# find the number of times character appears that is the count
a="aacdde"
count=1;
for i in range(len(a)-1):
    if(a[i]==a[i+1]):
        count= count+1
    else:
        print(a[i]," : ",count);
        count=1;
print(a[len(a)-1]," : ",count);

# Find the first non-repeating character in a string.
a="aacdde"
count=1;
for i in range(len(a)-1):
    if(a[i]==a[i+1]):
        count= count+1
    else:
        if(count==1):
            print("first non repeaing character ",a[i]);
            break;
        count=1;

        # print(a[i]," : ",count);
        # count=1;
# print(a[len(a)-1]," : ",count);
    