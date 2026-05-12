# number of times item appears in the list

# a=[1,2,3,2,1,5,3,5,12];
# val=sorted(a);
# print(val)
# count=1;
# for i in range(len(val)-1):
#     if(val[i]==val[i+1]):
#         count=count+1;
#     else:
#         print(val[i]," : ",count);
#         count=1;
# print(val[len(val)-1]," : ",count);

# find the duplicate item in the list
a=[1,2,3,2,1,5,3,5,12];
val=sorted(a);
print(val)
count=1;
for i in range(len(val)-1):
    if(val[i]==val[i+1]):
        count=count+1;
    else:
        if(count==1):
            print(val[i]);
    count=1;
#         print(val[i]," : ",count);
#         count=1;
# print(val[len(val)-1]," : ",count);
