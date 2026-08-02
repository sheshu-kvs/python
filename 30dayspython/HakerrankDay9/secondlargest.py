a=[10,8,5,3,8];
a.sort();
print(a)
p=0;
vp=0;
tp=0;
for i in range(len(a)):
    if a[i]>p:
        vp=p;
        p=a[i];
    elif a[i]>vp:
        vp=a[i];
print(vp)