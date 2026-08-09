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
    for i in range(1,n+1):
        for j in range(1,(n-i+1)+1):
            print("-",end="");
        for k in range(1,n+1,2):
            print("*",end=" ");
        for j in range(1,(n-i+1)+1):
                    print("-",end="");
            
        print();
# pt1();
# pt2();
# pt3();
# pt4();
# pt5();
pt6();