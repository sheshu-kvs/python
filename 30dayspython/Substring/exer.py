# Substring an substring is the part of the string (in a string sequence chars is the str)

# # 
# str12='python';
# for i in range(len(str12)):
#     for j in range(i+1,len(str12)+1):
#         print(str12[i:j])




# Print every substring along with its starting index.


# str12='abc';
# for i in range(len(str12)):
#     for j in range(i+1,len(str12)+1):
#         print(i,"",str12[i:j])


# # Print every substring with both start and end indices.
# str12='abc';
# for i in range(len(str12)):
#     for j in range(i+1,len(str12)+1):
#         print((i,j),"",str12[i:j])

        

# Find the total number of substrings.
# str12='abcd';
# count=0;
# for i in range(len(str12)):
#     for j in range(i+1,len(str12)+1):
#         # print((i,j),"",str12[i:j])
#         count=count+1;

# print(count)


# Print only the substrings whose length is 2.
# str12='python';
# for i in range(len(str12)):
#     for j in range(i+1,len(str12)+1):
#         if len(str12[i:j]) ==2:
#             print(str12[i:j])


# # Print only the substrings whose length is 3.
# str12='python';
# for i in range(len(str12)):
#     for j in range(i+1,len(str12)+1):
#         if len(str12[i:j]) ==3:
#             print(str12[i:j])


# #Print only the substrings that start with 'a'.
# str12='apple';
# for i in range(len(str12)):
#     for j in range(i+1,len(str12)+1):
#         if str12[i:j].startswith("a"):
#             print(str12[i:j]);



# # Print only the substrings ending with 'n'.
# str12='python';
# for i in range(len(str12)):
#     for j in range(i+1,len(str12)+1):
#         if str12[i:j].endswith("n"):
#             print(str12[i:j]);



# # Print only the substrings containing 'a'.
# str12='banana';
# for i in range(len(str12)):
#     for j in range(i+1,len(str12)+1):
#         if 'a' in str12[i:j]:
#             print(str12[i:j])


# # Print longest substrings .
# str12='ississippiem';
# uncount=0;
# for i in range(len(str12)):
#     for j in range(i+1,len(str12)+1):
#             if len(str12[i:j]) >uncount:
#                   uncount=len(str12[i:j]);


# print(str12[0:uncount])
# val=10;
# for i in range(val,-1,-1):
#     print(i)


def palin(val):
    t=''
    for i in range(len(val)-1,-1,-1):
        t=t+val[i];
    if t==val:
        return True;
    else:
        return False;

# str12='babad';
# uncount=0;
# for i in range(len(str12)):
#     for j in range(i+1,len(str12)+1):
#             if palin(str12[i:j]):
#                   if  len(str12[i:j])>uncount:
#                        uncount=len(str12[i:j]);

# print(str12[0:uncount])




str12='ABCDCDC';
inp='CDC'
count=0;
for i in range(len(str12)):
    for j in range(i+1,len(str12)+1):
        if str12[i:j]==inp:
            # print(str12[i:j])
            count=count+1;
print(count)