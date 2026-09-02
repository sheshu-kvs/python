# *****
# *****
# *****
# *****
# *****


def pat1():
    for i in range(5):
        for j in range(5):
            print("*",end="");
        print();



# *
# **
# ***
# ****
# *****
def pat2():
    for i in range(5):
        for j in range(i+1):
            print("*",end="");
        print()

def pat3():
    val=5;
    for i in range(5):
        for j in range(val,1,-1):
            print("-",end="")
        val=val-1;
        for j in range(i+1):
            print("* ",end="")
        print()
# pat1();
# pat2();
pat3();