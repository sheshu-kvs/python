def movezerosend():
    a=[0,1,0,3,12,0,5];
    for i in range(len(a)):
        for j in range(1,len(a)):
            if a[j]!=0:
                temp=a[i];
                a[i]=a[j];
                a[j]=temp;
                i+=1;
    print(a);

def commitemstwoarrays():
    a1=[1,2,3,4,5];
    a2=[3,4,6,7];
    for i in range(len(a1)):
        for j in range(len(a2)):
            if a1[i]==a2[j]:
                print(a1[i],end=" ");


commitemstwoarrays();
# movezerosend();