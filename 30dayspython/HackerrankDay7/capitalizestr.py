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



val='deva mariya';
t='';
splval=val.split(' ');
for word in range(len(splval)):
    for char in range(len(splval[word])+1):
        if char==0:
            t=t+splval[word][char].upper();
        elif char<len(splval[word]):
              t=t+splval[word][char];
        elif char==len(splval[word]):
              if word<len(splval)-1:
                   t=t+' '; 

print(t)