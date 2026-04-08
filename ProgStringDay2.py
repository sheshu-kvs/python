# Reverse a string without using slicing ([::-1]).

# str = "hello, world";
# rev="";
# for x in range(len(str)):
#     rev =  str[x] + rev;
# print("Reverse String: ",rev);


# Count the number of vowels in a string.
str = "hello, world";
countvowel=0;
countcons=0;
for x in range(len(str)):
    val= str[x];
    if((val == 'a') or (val == 'e') or (val == 'i') or (val=='o') or (val=='u')):
        countvowel=countvowel+1;
    else:
       countcons = countcons+1;


print("The Number of the Vowels is ",countvowel);   
print("The Number of the Consonent is ",countcons);   



# Find the length of a string without using len().

str = "hello";
count=0;
for x in range(len(str)):
    count = count+1;
print("the number of the character ",count)