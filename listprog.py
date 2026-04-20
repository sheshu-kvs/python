a=[22,2,3,10,5];
# b=[-12,-3,-11,-1];
large=0;
for x in range(len(a)):
    if(a[x]>large):
        large=a[x];
print(large)