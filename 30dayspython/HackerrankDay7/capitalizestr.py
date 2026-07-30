# # list31=['dal','dem','mena'];
# # lisd2=str(list31);
# # lisd2.capitalize()
# # print(lisd2)

# # dw='sre gjnjn'
# # print(dw.title())
# strval='deva mani';
# splval = strval.split(" ");
# t=""
# for i in range(len(splval)):
#     # print(i)
#     # print(len(splval[i]));
#     for j in range(len(splval[i])):
#         # print(splval[i][j])
#         if splval[i][j].isdigit():
#             t=t+splval[i][j];



# val='deva';
# t='';
# if val[0].isdigit():
#     print(val);
# else:
#     upval=val[0].upper();
#     print(upval)


# only single value
# val='deva'
# t="";
# for i in range(len(val)):
#     if i==0:
#         t=val[i].upper();
#     else:
#         t=t+val[i];

# print(t)



# val='deva mariya';
# t='';
# splval=val.split(' ');
# for word in range(len(splval)):
#     for char in range(len(splval[word])+1):
#         if char==0:
#             t=t+splval[word][char].upper();
#         elif char<len(splval[word]):
#               t=t+splval[word][char];
#         elif char==len(splval[word]):
#               if word<len(splval)-1:
#                    t=t+' '; 

# print(t)



# str12=input("Enter the String");

# if any(char.isdigit() for char in str12):
#     print(str12);
# else:
#     res=str12.title();
#     print(res);


str12=input("Enter the String:");
val=str12.split( );
newval=[]
for word in val:
    words=''
    for ch_idx in range(len(word)):
        if ch_idx==0:
            words=word[ch_idx].upper();
        else:
            words=words+word[ch_idx];
    newval.append(words)
res=" ".join(newval)
print(res);


