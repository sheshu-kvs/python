from itertools import permutations
val=input().split();
val1=sorted(val[0]);
val2=int(val[1]);
am=permutations(val1,val2);
for i in range(1,val2+1):
    for res in permutations(val1,i):
        print(" ".join(res).upper());


