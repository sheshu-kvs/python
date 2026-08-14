# ****
# ****
# ****
# ****
def pt1():
    n=int(input());
    for i in range(0,n):
        for j in range(0,n):
            print("*",end="");
        print()

# *
# **
# ***
# ****

def pt2():
    n=int(input());
    for i in range(1,n+1):
        for j in range(0,i+1):
            print("*",end="");
        print();      

# 1
# 12
# 123
# 1234
def pt3():
    n=int(input());
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end="");
        print();

# 1
# 22
# 333
# 4444

def pt4():
    n=int(input());
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i,end="");
        print();  



# *****
# ****
# ***
# **
# *
def pt5():
    n=int(input());
    for i in range(n,-1,-1):
        for j in range(i,-1,-1):
            print("*",end="");
        print();

# 12345
# 1234
# 123
# 12
# 1
def pt6():
    n=int(input());
    for i in range(n,0,-1):
        for j in range(1,i+1):
            print(j,end="");
        print()

def pt7():
    n=int(input());
    space=4
    for i in range(1,n+1):
        # space
        for j in range(0,space):
            print("-",end="");
        for j in range(0,(2*i-1)):
            print("*",end="");
        for j in range(0,space):
            print("-",end="");
        space-=1
        print()


def pt8():
    n=int(input());
    space=4
    for i in range(n,0,-1):
        # space
        for j in range(0,space):
            print("-",end="");
        for j in range(0,(2*i-1)):
            print("*",end="");
        for j in range(0,space):
            print("-",end="");
        space-=1
        print()


def pt8():
    n=int(input());
    space=0;
    for i in range(n,0,-1):
        # space
        for j in range(0,space+1):
            print("-",end="");
        for j in range((2*n-i),0,-1):
            print("*",end="");
        for j in range(0,space+1):
            print("-",end="");
        space+=1
        print()       
        
# pt1();
# pt2();
# pt3();
# pt4();
# pt5();
# pt6();
# pt7();
pt8();