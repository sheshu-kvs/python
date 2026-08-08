# input();
val1=set(map(int,input().split()))
val2=set(map(int,input().split()))
# print(val1)
# print(val2)

res1= val1.symmetric_difference(val2);
# res2= val2.symmetric_difference(val2);
# print(res1)
for i in  res1:
    print(i);
# print(res2)
