# # splitting the string 
# # str='this is python'
# # a=str.split(" ");
# # new="-".join(a);
# # print(a)
# # print(new)

# # val="HackerRank.com presents Pythonist 2";
# # t="";
# # for i in range(len(val)):
# #     ch=val[i];
# #     if ch>='A' or ch<='Z':
# #         t=ch+32;
# #     elif ch>='a' or ch<='z':
# #          t=ch-32;
# #     else:
# #         t=t+ch;
# # print(t);

# # new="a";
# # val=ord(new);
# # # converts the integer
# # dt=val-32;
# # # convert back to the str
# # new=chr(dt);
# # print(new);



# # converts all the str to lowercase
# # st="HELO";
# # t="";
# # for i in range(len(st)):
# #     val=ord(st[i]);
# #     if val >=97 or val <=122:
# #         t=t+chr(val+32);
# #     else:
# #         t=t+chr(val);
# # print(t)

# # converts upper case
# # st="helo";
# # t="";
# # for i in range(len(st)):
# #     val=ord(st[i]);
# #     if val >=65 or val <=96:
# #         t=t+chr(val-32);
# #     else:
# #         t=t+chr(val);
# # print(t)



# # converts upper to lower , lower to upper
# st="helo12344";
# t="";
# for i in range(len(st)):
#     val=ord(st[i]);
#     # print(val)
#     # if val >=65 or val <=96:
#     #     t=t+chr(val+32);
#     #     # which converts to lowercase
#     if val >=97  or val <=122:
#         t=t+chr(val-32);
#         # which converts the upprecase
#     else:
#         t=t+st[i];

#         # t=t;
# print(t)

st='helo12WORLD.com';
t=''

for i in range(len(st)):
    if st[i].isalpha():
        val=ord(st[i]);
        if val>=96 and val<=122:
                    t=t+chr((val-32));
        elif val>=65 and val<=95:
            t=t+chr((val+32));
    #   print(st)
       
    elif st[i].isdigit():
        t=t+st[i];
    elif not st[i].isalnum() and not st[i].isspace():
        t=t+st[i]; 




# split and join the str
# srt="hello12 WorD";
srt="hACKERrANK.COM PRESENTS pYTHONIST 2 .";
val=srt.split(" ");

t="";
for i in range(len(val)):
    for j  in range(len(val[i])):
        #  print(val[i][j])
         if val[i][j].isalpha():
              realval=ord(val[i][j])
              if realval>=65 and realval<=96:
                   t=t+chr(realval+32);
              elif realval>=97 and realval<=122:
                   t=t+chr(realval-32);              
         elif val[i][j].isdigit():
              t=t+val[i][j];
         elif not val[i][j].isspace() and not val[i][j].isalnum():
              t=t+val[i][j];

    # Add space 
    if i<len(val)-1:
         t=t+" ";
realstr="".join(t);
print(realstr);
# print(t);