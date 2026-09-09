a=[1,2,3,4,5];
# insert the single item
# a=a+[4];
# insert the multiple items
# a=a+[12,12,4,5]

# using the slicing
b=[];
for i in range(len(a)):
    if a[i]==1:
        continue;
    else:
        b.append(a[i]);

# print(b)



def countnumberoftimes():
    a=[1,2,3,4,5,1,2,3,4]
    a.sort();
    print(a)
    count=1;
    b=[];
    for i in range(len(a)-1):
        if a[i]==a[i+1]:
            count=count+1;
        else:
            print(a[i],":",count);
            count=1
    print(a[len(a)-1],":",count)




def duplicationremoval():
    a=[1,2,3,4,5,1,2,3,4]
    a.sort();
    print(a)
    count=1;
    b=[];
    for i in range(len(a)-1):
        if a[i]==a[i+1]:
            count=count+1;
        else:
            if count==1:
                b.append(a[i]);
            count=1
    if count==1:
        b.append(a[len(a)-1]);
    
    print(b)



def addduplicates():
    a=[1,2,3,4,5,1,2,3,4]
    a.sort();
    print(a)
    count=1;
    b=[];
    for i in range(len(a)-1):
        if a[i]==a[i+1]:
            count=count+1;
        else:
            if count>1:
                b.append(a[i]);
            count=1
    if count>1:
        b.append(a[len(a)-1]);
    
    print(b)

addduplicates()
# duplicationremoval();
# duplicationremoval();

# countnumberoftimes()