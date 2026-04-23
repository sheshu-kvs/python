# Check if two strings are anagrams.

def checkangram(str1,str2):
        # we need to sort both the stirngs paralley compare both
        return sorted(str1.lower())==sorted(str2.lower());



print(checkangram("listen","silent"));



# Find the most frequent character in a string.
str="hello world";

sortedval= sorted(str);
count=1;
for x in range(len(sortedval)-1):
        if(sortedval[x]==sortedval[x+1]):
                count=count+1;
        else:
                print(sortedval[x]," : ",count);
print(sortedval[x]," : ",count);