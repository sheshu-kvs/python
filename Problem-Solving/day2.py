def factors():
    n=int(input());
    for i in range(1,n+1):
        if n%i==0:
            print(i,end=" ")


def checkprime():
    n=int(input())
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1;    
    if count==2:
        print("Prime");
    else:
        print("Not Prime");


def printallprime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1;    
    if count==2:
        print(i);
    # else:
    #     print("Not Prime");



# factors()
# checkprime();
n=int(input())
for i in range(n):
    printallprime(i)