from itertools import permutations
val=input().split();
val1=val[0];
val2=int(val[1]);
am=permutations(val1,val2);
for res in am:
    print(" ".join(res));
