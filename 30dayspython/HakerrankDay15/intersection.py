input();
val1=set(map(int,input().split()));
input();
val2=set(map(int,input().split()));
l1=len(val1);
l2=len(val2)
print(val1)
print(val2)

print(len(val1.intersection(val2)))
# print(l1+l2)



def spacenum():
    n=int(input());
    sp=6;
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end="");
        for j in range(sp):
            print(" ",end="")
        for k in range(i,0,-1):
            print(k,end="");
        sp-=2;
        print()
# spacenum();


def printnum():

    n=int(input())
    num=1;  
    for i in range(1,n+1):
        # num=1;
        for j in range(1,i+1):
            print(num,end="");
            num+=1;
        print()
# printnum();

def printalpha():
  
    for i in range(1,6):
        ch=65;
        for j in range(ch,ch+i):
            print(chr(j),end="");
            ch=ch+1;
        print()

# printalpha();


def reversealph():
    for i in range(5,6):
        ch=65;
        
        for j in range(ch+):
            print(chr(j),end="")
        ch+=1;
        print()

reversealph()
