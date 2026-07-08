# Create an empty dictionary called dog
dog={};
print(type(dog))

# Add name, color, breed, legs, age to the dog dictionary
dog={"name":"pomoreon","color":"white","brred":"hybrid","legs":"2legs","age":1}
print(dog)
print(len(dog))
print(dog["name"])

dog["name"]="mottu";
print(dog)
print(dog.keys())
print(dog.values())


newdoglst=list(dog);
print(newdoglst)

print(dog.pop(1));
