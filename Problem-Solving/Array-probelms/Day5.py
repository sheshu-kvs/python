def leftbykpos():
    a=[1,2,3,4,5];
    k=2;
    a3=[]
    for i in range(k):
        a3.append(a[i]);
    new_i=0;
    for j in range(len(a)):
        if k<len(a):
            a[j]=a[k];  
        elif k>len(a)-1:
            a[j]=a3[new_i];
            new_i+=1;
        k+=1;
    print(a)


# def rightbykpos():
#     a=[1,2,3,4,5];
#     k=3;
#     # 4 5 1 2 3
#     a3=[];
#     for i in range(k):
#         a3.append(a[i]);
#     # print(a3)
#     new_i=0
#     for j in range(len(a)):
#         if k<len(a):
#             a[j]=a[k];
#         elif k>len(a)-1:
#             a[j]=a3[new_i];
#             new_i+=1;
#         k+=1;
#     print(a);

def rightbykpos():
    a=[1,2,3,4,5];
    n=len(a);
    k=2;
    # 4 5 1 2 3
    a3=[];
    val=n-k
    for i in range(val):
        a3.append(a[i]);
    # print(a3)
    new_i=0
    for j in range(len(a)):
        if val<len(a):
            a[j]=a[val];
        elif val>len(a)-1:
            a[j]=a3[new_i];
            new_i+=1;
        val+=1;
    print(a);



rightbykpos();
# leftbykpos();
# shittingitem();