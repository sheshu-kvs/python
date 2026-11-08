words = ["hey","aeo","mu","ooo","artro"];
left = 1;
right = 4;
val=0;
volwels={'a','e','i','o','u'};
# Brute
for i in range(left,right):
    char = words[i];
    if char[0] in volwels and char[-1] in volwels:
        val+=1;
# print(val)

# optimal
val=sum(1 for i in range(left,right)   if words[i][0] in volwels and words[i][-1] in volwels )
print(val)