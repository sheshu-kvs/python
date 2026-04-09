
#Replace all vowels in a string with *.
str="hello , world";
converted="";
for x in range(len(str)):
    val = str[x];
    if val in 'aeiou':
        converted = converted + "*";
    else:
        converted = converted + val;
print("Updated Vowel ",converted);



#Find the first non-repeating character in a string.


str = "hello, world";


for x  in range(len(str)-1):
    # val = sortedval[x];
    if(str[x] != str[x+1]):
        print("first non repeating chracter "+str[x]);
        break;
