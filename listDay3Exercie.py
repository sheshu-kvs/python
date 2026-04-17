adev=["apple","banana","mango","devc"]
val=[]
for x in adev:
    if "a" in x:
        val.append(x)
print(val)


# with onesingle line what we written in above
val=[x for x in adev if "a" in x]
print(val)

# iterable in the int
b=[1,2,4,5,7,8];

newval = [x for x in range(len(b))]
print(newval)



# sort list 
a=[45,23,2,4,5,67,3];
a.sort();
print(a)

a.sort(reverse=True);
print(a)


forvaal=['jkedb',"nbsdasba",'jbxcjcbxz', 'abx'];
forvaal.reverse();
print(forvaal)

