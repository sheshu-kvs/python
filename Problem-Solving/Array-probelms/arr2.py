def uiqueitemsarr():
    a=[0,0,1,1,1,2,2,3,3,4];
    k=1;
    a2=[]
    for i in range(1,len(a)):
        if a[i]!=a[i-1]:
            # a2.append(a[i-1]);
            k+=1;
    print(a2)
uiqueitemsarr();
