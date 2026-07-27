c='qW9';
hasalpha=False;
hasalnum=False;
haslower=False;
hasupper=False;
hasdigit=False;

for i in c:
    if i.isalpha():
        hasalpha=True;
    if i.isalnum():
        hasalnum=True;
    if i.islower():
        haslower=True;
    if i.isupper():
        hasupper=True;
    if i.isdigit():
        hasdigit=True;
 
print(hasalpha)       
print(hasalnum)       
print(hasdigit)       
print(haslower)       
print(hasupper)       


# str to capitalize

str12="merry mana";
spl=str12.split(" ");
for i in range(len(spl)):
    if spl[i].isalpha():
        res=spl[i].title();
        print(res)
        print("happy")
    else:
        print("unhappy")