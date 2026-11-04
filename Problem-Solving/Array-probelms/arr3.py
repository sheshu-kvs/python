def uniqueitemsarr():
    a=[0,0,1,1,1,2,2,3,3,4];
    k=1;
    a2=[]
    for i in range(1,len(a)):
        if a[i]!=a[i-1]:
            # a2.append(a[i-1]);
            k+=1;
    print(a2)

def rotatearrkposbrute(k):
    a=[1,2,3,4,5];
    rotations=k%len(a);
    for _ in range(rotations):
        lst_item=a.pop();
        a.insert(0,lst_item);
    print(a)

def rotatearrkposoptimal(k):
    a=[1,2,3,4,5]
    k=k%len(a);
    # print(a[-k:])
    # print(a[:-k])
    print(a[-k:]+a[:-k])
rotatearrkposoptimal(8);
# rotatearrkposbrute(7);
# uniqueitemsarr();
