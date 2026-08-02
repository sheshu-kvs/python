str12='ABCDEFGHIJKLIMNOQRSTUVWXYZ';
max=4;
# slicing
# for i in range(0,len(str12),4):
#     print(str12[i:i+4]);

for i in range(0,len(str12),4):
    for j in range(i,i+4):
        print(str12[j],end=" ");
    print(" ") 