# *****
# *****
# *****
# *****
# *****


def pt1():
    print("Pattern 1")
    for i in range(5):
        for j in range(5):
            print("*",end="");
        print();

# *
# **
# ***
# ****
# *****

def pt2():
    for i in range(5):
        for j in range(i+1):
            print("*",end="");
        print();


# 1
# 12
# 123
# 1234
# 12345
def pt3():
    for i in range(5):
        num=1;
        for j in range(i+1):
            print(num,end="");
            num+=1
        print()
# 1
# 22
# 333
# 4444
# 55555
def pt3():
    for i in range(1,6):
        for j in range(1,i+1):
            print(i,end="");
        print()

# *****
# ****
# ***
# **
# *
def pt4():
    for i in range(5,0,-1):
        
        for j in range(i,0,-1):
            print("*",end="");
        print()
# 12345
# 1234
# 123
# 12
# 1
def pt5():
    for i in range(5,0,-1):
        num=1
        for j in range(i,0,-1):
            print(num,end="");
            num+=1
        print()


#     *   
#    ***   
#   *****  
#  ******* 
# ********* 
def pt6():
    num=4;
    for i in range(1,6):
        # Space
        for j in range(num):
            print(" ",end="")

        for j in range(1,(2*i-1)+1):
            print("*",end="");

        # Space
        for j in range(num):
            print(" ",end="")
        num-=1;
        print()




# *********
#  *******
#   *****  
#    ***   
#     * 


def pt7():
    num=0;
    n=5
    for i in range(1,6):
        # Space
        for j in range(num):
            print(" ",end="")

        for j in range(1,2*n-(2*i-1)+1):
            print("*",end="");

        # Space
        for j in range(num):
            print(" ",end="")
        num+=1;
        print()

#     *    
#    ***   
#   *****  
#  ******* 
# *********
# *********
#  ******* 
#   *****  
#    ***   
#     * 

def pt8():
    n1=4;
    for i in range(1,6):
        # Space
        for j in range(n1):
            print(" ",end="")

        for j in range(1,(2*i-1)+1):
            print("*",end="");

        # Space
        for j in range(n1):
            print(" ",end="")
        n1-=1;
        print()
    n2=0;
    n=5
    for i in range(1,6):
        # Space
        for j in range(n2):
            print(" ",end="")

        for j in range(1,2*n-(2*i-1)+1):
            print("*",end="");

        # Space
        for j in range(n2):
            print(" ",end="")
        n2+=1;
        print()

# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

def pt9():
    n=5
    for i in range(1,10):
        st=i;
        if st>n:
            st=10-i;

        for j in range(1,st+1):
            print("*",end="");    
        print()

# 1
# 0 1
# 1 0 1
# 0 1 0 1
# 1 0 1 0 1

def pt10():
    st=1
    for i in range(0,5):
        if i % 2 == 0:
            st=1;
        else:
            st=0;
        for j in range(0,i+1):
            print(st,end="");
            st=1-st;
        print();



# 1      1
# 12    21
# 123  321
# 12344321
def pt12():
    space=6;
    for i in range(1,5):

        for j in range(1,i+1):
            print(j,end="");
        # space
        for j in range(space):
            print(" ",end="")

        for j in range(i,0,-1):
            print(j,end="")
        space-=2;
        print()

# **********
# ****  ****
# ***    ***
# **      **
# *        *
# *        *
# **      **
# ***    ***
# ****  ****
# **********
def pt13():
    space=0;
    
    for i in range(5,0,-1):
        for j in range(i):
            print("*",end="");
        # Space
        for j in range(space):
            print(" ",end="");
        for j in range(i):
            print("*",end="");
        space+=2;
        print()
    desspace=8;
    for i in range(1,6):
        for j in range(1,i+1):
            print("*",end="");
        # Space
        for j in range(desspace):
            print(" ",end="");
        for j in range(1,i+1):
            print("*",end="");
        desspace-=2;
        print()
# pt12()
# pt1();
# pt2();
# pt3();
# pt4();
# pt5();
# pt6();
# pt7();
# pt8();
# pt9();
# pt10();
# pt11();
# pt12();

pt13();