# ****
# ****
# ****
# ****
def pt1():
    n=int(input());
    for i in range(n):
        for j in range(n):
            print("*",end="");
        print();


def pt2():
    n=int(input());
    for i in range(n):
        for j in range(0,i+1):
            print("*",end=" ")
        print();    

# 6
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 
def pt3():
    n=int(input());
    for i in range(1,n):
        for j in range(1,i+1):
            print(j,end=" ");
        print();    



def pt4():
    n=int(input());
    for i in range(1,n):
        for j in range(1,i+1):
            print(i,end=" ");
        print();    


# * * * * 
# * * * 
# * * 
# * 
def pt5():
    n=int(input());
    for i in range(1,n+1):
        for j in range(0,n-i+1):
            print("*",end=" ");
        print();


def pt6():
    n=int(input());
    for i in range(1,n+1):
        for j in range(1,(n-i+1)+1):
            print(j,end=" ");
        print();




def pt6():
    n=int(input());
    for i in range(0,n):
        for j in range(0,(n-i-1)):
            print("-",end="");
        for k in range(0,(2*i+1)):
            print("*",end="");
        for j in range(0,n-i-1):
            print("-",end="");
            
        print();


def pt7():
    n=5;
    for i in range(0,n):
        for j in range(0,i):
            print("-",end="");
        for k in range(0,(2*n-(2*i+1))):
            print("*",end="");
        for j in range(0,i):
            print("-",end="");
            
        print();


def pt8():
     n1=5;
     for i in range(0,n1):
        for j in range(0,(n1-i-1)):
            print("-",end="");
        for k in range(0,(2*i+1)):
            print("*",end="");
        for j in range(0,n1-i-1):
            print("-",end="");
                
        print();
     n=5;
     for i in range(0,n):
        for j in range(0,i):
            print("-",end="");
        for k in range(0,(2*n-(2*i+1))):
            print("*",end="");
        for j in range(0,i):
            print("-",end="");
        print();

def pt9():
    n=int(input());
    for i in range(1,(2*n-1)+1):
        stars=i;
        if i>n:
            stars=2*n-i;
        for j in range(0,stars):
            print("*",end="");
        

        print()

def pt10():
    n=int(input());
    strt=1
    for i in range(1,n+1):
        if i%2==0:
            strt=1;
        else:
            strt=0;
        for j in range(0,i):
            print(strt,end=" ");
            strt=1-strt;
        print()
# pt1();
# pt2();
# pt3();
# pt4();
# pt5();
# pt6();
# pt7();
# pt8();
# pt9();
pt10();