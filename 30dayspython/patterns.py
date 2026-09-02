# 1
# 12
# 123
# 1234
# 12345

def rectangelnum():
    for i in range(5):
        num=1;
        for j in range(i+1):
            print(num,end="");
            num+=1;
        print()

# 1
# 22
# 333
# 4444
# 55555

def rectanglei():
    for i in range(1,6):
        for j in range(1,i+1):
            print(i,end="")
        print()

# *****
# ****
# ***
# **
# *

def revrecatanglei():
    for i in range(5,0,-1):
        for j in range(i):
            print("*",end="")
        print();

# 12345
# 1234
# 123
# 12
# 1

def revrecatanglenum():
    for i in range(5,0,-1):
        num=1
        for j in range(i):
            print(num,end="")
            num+=1;
        print();


# ---- *
# ----***
# ---*****
# --*******
# -*********
def pyramid():
    num=5;
    for i in range(1,6):
        for j in range(num):
            print("-",end="");
        for j in range((2*i-1)):
            print("*",end="");
        print();    
        num-=1;

#  2*1-1=1
#  2*2-1=3
#  2*3-1=5
#  2*4-1=7
#  2*5-1=9


# -*********
# --*******
# ---*****
# ----***
# -----*
def revpyramid():
    for i in range(1,6):
        for j in range(i):
            print("-",end="");
        for j in range(2*5-(2*i-1)):
            print("*",end="");
        for j in range(i):
            print("",end="")
        print();

        # 10-1=9
        # 10-3=7
        # 10-5=5
        # 10-7=3
        # 10-9=1


# -----*
# ----***
# ---*****
# --*******
# -*********
# -*********
# --*******
# ---*****
# ----***
# -----*     
def daimondpyramid():
    num=5;
    for i in range(1,6):
        for j in range(num):
            print("-",end="");
        for j in range((2*i-1)):
            print("*",end="");
        print();    
        num-=1;
    for i in range(1,6):
        for j in range(i):
            print("-",end="");
        for j in range(2*5-(2*i-1)):
            print("*",end="");
        for j in range(i):
            print("",end="")
        print();

# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *
def lessrectangel():
    n=5;
    for i in range(1,(2*n-1)+1):
        st=i;
        if st>n:
            st=(2*n)-i;
        for j in range(1,st+1):
            print("*",end="");
        print();

# 1      1
# 12    21
# 123  321
# 12344321
# 1------1
# 12----21
# 123--321
# 12344321
def spacenum():
    space=6;
    for i in range(1,5):
        num=1;
        for j in range(1,i+1):
            print(num,end="");
            num+=1;
        for j in range(space):
            print("-",end="");
        space-=2;
        num=1;
        for j in range(i,0,-1):
            print(j,end="");
            num+=1;
        print()

def printnum():
    num=1
    for i in range(1,5):
       
        for j in range(1,i+1):
            print(num,end="")
            num+=1;
        print()
        



# rectangelnum();
# rectanglei();
# revrecatanglei();
# revrecatanglenum();
# pyramid();
# revpyramid();
# daimondpyramid();
# lessrectangel();
# spacenum();
printnum();
