def leftrotatebykpos(k):

    a=[1,2,3,4,5,6,7];
    print(a)
    k=k%len(a);
    tmp=a[:k];
    for i in range(k,len(a)):
        a[i-k]=a[i];
    j=0;
    for k in range((len(a)-k),len(a)):
        a[k]=tmp[j];
        j+=1;
    print(a);


def rightsotatearraybykpos(k):
        # ans
        # [1, 2, 3, 4, 5]
        # [4, 5, 1, 2, 3]     
     a=[1,2,3,4,5];
     print(a)
     k=k%len(a);
    #  O(k)
     tmp=a[len(a)-k:];        
    #  O(n-k)     
     for i in range(len(a)-1,k-1,-1): 
         a[i]=a[i-k];
     j=0;
    #  o(k)
     for k in range(k):
         a[k]=tmp[j];
         j+=1;

     print(a)



def MovezeroendBrute():
    a=[1,2,0,4,5,0,1];
    tmp=[];
    for i in range(len(a)):
        if a[i]!=0:
            tmp.append(a[i]);
    print(tmp)
    k=0
    for i in range(len(tmp)):
        a[i]=tmp[k];
        k+=1;
    for j in range(len(tmp),len(a)):
        a[j]=0;
    print(a)



def MovezeroendOptimal():
    a=[1,2,0,4,5,0,1];
    j=-1;
    for i in range(len(a)):
        if a[i]==0:
            j=i;
            break;
    for k in range(j+1, len(a)):
        if a[k]!=0:
            tmp=a[k];
            a[k]=a[j];
            a[j]=tmp;
            j+=1;
    print(a);



def MovezerofrontOptimal():
    a=[1,2,0,4,5,0,1];
    j=-1;
    for i in range(len(a)-1,-1,-1):
        if a[i]==0:
            j=i;
            break;
    for k in range(j-1, -1,-1):
        if a[k]!=0:
            tmp=a[k];
            a[k]=a[j];
            a[j]=tmp;
            j-=1;
    print(a);

# rightsotatearraybykpos(2);
# leftrotatebykpos(2)
# MovezeroendBrute();
# MovezeroendOptimal();
MovezerofrontOptimal();
