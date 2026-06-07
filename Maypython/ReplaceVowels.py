# Replace Vowels with the *
str="hello world";
t="";
for i in range(len(str)):
    if((str[i]=='a') or (str[i]=='e') or (str[i]=='i') or (str[i]=='o') or (str[i]=='u')):
      t=t+"*";
    else:
       t=t+str[i];

# print("Replaced With the Vowels ",t);

# Remove the Space
str=" hello";
# print(str);
# print(str.lstrip());


str2="hello  world ";
count=0;
for i in range(len(str)):
    if(str[i]==" "):
       count+=1;
print("Count The Number Of Spaces ",count);