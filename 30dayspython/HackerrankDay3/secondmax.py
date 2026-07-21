# lis=[2,14,1,6,8];
lis=[2,3,6,6,5];

# p=0;
# vp=0;
# for i in range(len(lis)):
#     if lis[i]>p:
#         vp=p;
#         p=lis[i];
#     elif lis[i]>vp:
#         vp=lis[i];
# print(vp); 

count = 1
lis2=[]
sortval=sorted(lis);
# print(sortval)
for i in range(len(sortval)-1):
    if sortval[i] == sortval[i+1]:
        count+=1;
    else:
        if count==1:
            lis2.append(sortval[i]);
            count=1;
lis2.append(sortval[len(lis)-1]);
print(lis2)        

p=0;
vp=0;
for j in range(len(lis2)):
    if lis2[j] > p:
        vp=p;
        p=lis2[j];
    elif lis2[j] > vp:
        vp=lis2[j];
print(vp) 