#Count how many times a character appears in a string.
str="hello,erinol";
sortedval=sorted(str);
print(sortedval);
count=1;
for x in range(len(sortedval)-1):
    if(sortedval[x] == ","):
        continue;
    if(sortedval[x]==sortedval[x+1]):
        count=count+1;
    else:
        print(sortedval[x], ":", count);
        count=1;
print(sortedval[len(sortedval)-1], ":" ,count)
