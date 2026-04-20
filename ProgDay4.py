
#Replace all vowels in a string with *.
# str="hello , world";
# converted="";
# for x in range(len(str)):
#     val = str[x];
#     if val in 'aeiou':
#         converted = converted + "*";
#     else:
#         converted = converted + val;
# print("Updated Vowel ",converted);



#Find the first non-repeating character in a string.


str = "hello, world";
count = 1;
sortval = sorted(val);
print(sortval)
for x  in range(len(sortval)-1):
    # val = sortedval[x];
    if(sortval[x] == sortval[x+1]):
        count = count+1;
    else:
        print(sortval[x] ,":", count); 
        count = 1;

print(sortval[x], ":" ,count);