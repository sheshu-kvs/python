
def consquetivearray():
    a=[0];
    count=0;
    maxcount=0;
    for i in range(len(a)):
        if a[i]==1:
            count+=1;
        else:
            count=0
        if count>maxcount:
            maxcount=count;
    print(maxcount)
def factors():
    num=int(input());
    for i in range(1,num+1):
        if num%i==0:
            print(i)
factors();
# consquetivearray();