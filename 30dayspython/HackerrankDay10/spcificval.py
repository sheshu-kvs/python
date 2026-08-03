str12='ABCDEFGHIJKLIMNOQRSTUVWXYZ';
max=4;
print(len(str12))
# slicing
# for i in range(0,len(str12),4):
#     print(str12[i:i+4]);

for i in range(0,len(str12),4):
    for j in range(i,i+4):
        if j<len(str12):
            print(str12[j],end=" ");
    print(" ") 



val1=[1,2]
val2=[3,4]
for i in range(len(val1)):
    for j in range(len(val2)):
        print(f"({val1[i]},{val2[j]})")    

a=[1,2];
b=[3,4];