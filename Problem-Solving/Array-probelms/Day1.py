def largest():
    a=[10,25,7,42,18];
    lg=float('-inf');
    for i in range(len(a)):
        if a[i]>lg:
            lg=a[i];
    print(lg);



def smallest():
    a=[10,25,7,42,18];
    sm=float('inf');
    for i in range(len(a)):
        if a[i]<sm:
            sm=a[i];
    print(sm);


def sumofarray():
    a=[10,20,30,40,50];
    sum=0;
    for i in range(len(a)):
        sum=sum+a[i];
    print(sum);



def findavg():
    a=[10,20,30,40,50];
    sum=0;
    for i in range(len(a)):
        sum=sum+a[i];
    avg=float(sum//len(a));
    print(avg);

def counteven():
    a=[1,4,7,8,10,13];
    count=0;
    for i in range(len(a)):
        if a[i]%2==0:
            count+=1;
    print(count);

def countodd():
    a=[1,4,7,8,10,13];
    count=0;
    for i in range(len(a)):
        if a[i]%2!=0:
            count+=1;
    print(count);


def printreverse():
    a=[10,20,30,40,50];
    print(a);
    for i in range(len(a)-1,-1,-1):
        print(a[i],end=" ")



def searchitem():
    a=[10,20,30,40,50];
    sc=10;
    for i in range(len(a)):
        if a[i]==sc:
            return "Found";
    return "Not Found";
print(searchitem());
# printreverse();
# countodd();
# counteven();
# findavg();
# sumofarray();
# smallest();    
# largest();