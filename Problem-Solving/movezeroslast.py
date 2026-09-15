def movezeros():
    a=[1,0,2,3,2,0,0,4,5,1];
    tmp=[];
    # step1
    for i in range(len(a)):
        if a[i]!=0:
            tmp.append(a[i]);

    # step2
    for i in range(len(tmp)):
        a[i]=tmp[i]
    # step 3
    for j in range(len(tmp),len(a)):
        a[j]=0;
    print(a)

movezeros()