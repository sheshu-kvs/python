def merge2arr():
    a1=[1,2,3,4,5];
    a2=[7,8,10,12,25];
    i=0;
    j=0;
    val=len(a1)+len(a2);
    a3=[]
    while i<len(a1) and j<len(a2):
        if a1[i]<a2[j]:
            a3.append(a1[i]);
            i+=1;
        else:
            a3.append(a2[j]);
            j+=1;
    while i<len(a1):
        a3.append(a1[i]);
        i+=1;
    while j<len(a2):
        a3.append(a2[j]);
        j+=1
    print(a3);

def maxconsquetive():
    a=[1,1,0,1,1,1,0,1];
    count=0;
    maxcount=0;
    for i in range(len(a)):
   

# maxconsquetive();
# merge2arr();