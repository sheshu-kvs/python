def leftrotatearrayby1():
    a=[1,2,3,4,5];
    j=1;
    fst=a[0];
    for i in range(len(a)):
        # fst=a[0];
        if i==len(a)-1:
            a[i]=fst
        else:
            a[i]=a[j];
            j+=1;
    print(a);



def rightrotatearray():
    a=[1,2,3,4,5];
    j=1;
    for i in range(len(a)):
        if i==0:
            a[i]=a[len(a)-1];
        else:
             a[i]=j;
             j+=1;
    print(a)

def pairgivensum():
    # a=[11,15,3,6,8,1];
    a=[1,7,2,6,3,5];
    sm=8
    j=1;
    for i in range(len(a)):
        if j<len(a):
            if a[i]+a[j]==sm:
                # print("(",a[i],",",a[j],")",end="");
                print(f"{a[i],a[j]}",end="");
        j+=1;
     


# leftrotatearrayby1();
# rightrotatearray();
pairgivensum();