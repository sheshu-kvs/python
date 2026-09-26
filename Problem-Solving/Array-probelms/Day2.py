
# brute
def movezerobrute():
    count=0;
    a=[0,1,0,3,12,0,5];
    a2=[0]*len(a)
    insert=0
    for i in range(len(a)):
        if a[i]!=0:
            a2[insert]=a[i];
            count+=1;
            insert+=1
    for j in range(count,len(a)):
        a2[j]=0;
    print(a2)

# optimal
def movezerosend():
    # a=[0,1,0,3,12,0,5];
    a=[3,0,5];
    i=0
    for j in range(0,len(a)):
        if a[j]!=0:
            temp=a[i];
            a[i]=a[j];
            a[j]=temp;
            i+=1;
    print(a);

def commitemstwoarrays():
    a1=[1,2,3,4,5];
    a2=[3,4,6,7];
    for i in range(len(a1)):
        for j in range(len(a2)):
            if a1[i]==a2[j]:
                print(a1[i],end=" ");



# using the brute
def printnegativenum():
    a=[-2,-4,-6,1,3,5];
    for i in range(len(a)):
        if a[i]<0:
            print(a[i])


# using the brute right
def printnegleft():
    a=[1,-2,3,-4,5,-6];
    a2=[0]*len(a);
    count=0;
    for i in  range(len(a)):
        if a[i]<0:
            a2[count]=a[i];
            count+=1
    for i in range(len(a)):
        if a[i]>0:
            a2[count]=a[i];
            count+=1;
    print(a2)

                                               


printnegleft();
# printnegativenum();
# commitemstwoarrays();
# movezerobrute()
# movezerosend();