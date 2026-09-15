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

# optimal
def movezerosend():
    a=[1,2,2,3,4,2,1,2,2];

    j=-1;
    for i in range(len(a)):
        if a[i]==0:
            j=i;
            break;
    for i in range(j+1,len(a)):
        if 0 in a:

            if a[i]!=0:
                tmp=a[i]; 3
                a[i]=a[j]; 0
                a[j]=tmp; 3
                j+=1;
        else:
            break;


movezerosend()


movezeros()
