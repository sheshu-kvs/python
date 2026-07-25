# splitting the string 
# str='this is python'
# a=str.split(" ");
# new="-".join(a);
# print(a)
# print(new)

# val="HackerRank.com presents Pythonist 2";
# t="";
# for i in range(len(val)):
#     ch=val[i];
#     if ch>='A' or ch<='Z':
#         t=ch+32;
#     elif ch>='a' or ch<='z':
#          t=ch-32;
#     else:
#         t=t+ch;
# print(t);

# new="a";
# val=ord(new);
# # converts the integer
# dt=val-32;
# # convert back to the str
# new=chr(dt);
# print(new);



# converts all the str to lowercase
# st="HELO";
# t="";
# for i in range(len(st)):
#     val=ord(st[i]);
#     if val >=97 or val <=122:
#         t=t+chr(val+32);
#     else:
#         t=t+chr(val);
# print(t)

# converts upper case
# st="helo";
# t="";
# for i in range(len(st)):
#     val=ord(st[i]);
#     if val >=65 or val <=96:
#         t=t+chr(val-32);
#     else:
#         t=t+chr(val);
# print(t)



# converts upper to lower , lower to upper
st="heloWORLD";
t="";
for i in range(len(st)):
    val=ord(st[i]);
    if val >=65 or val <=96:
        t=t+chr(val+32);
    elif val >=97 or val <=122:
        t=t+chr(val-32);
    else:
        t=t+chr(val)
        # t=t;
print(t)

