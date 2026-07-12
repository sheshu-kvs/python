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

# print(dog.pop(1));




# dictionary Practising session
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }

# print(len(dict));

person={
    'first_name':'sheshu',
    'last_name':'kumar',
    'is_married':True,
     'skills':['html','css','js','python','sql'],
     'address':{
         'hometown':'madhavaram',
         'living':'banglore'
     }
}

# len of the str
print(len(person));

print(person['first_name']);
print(person['last_name']);
print(person['skills']);
print(person['address']);

person['skills'].append("Java")
print(person['skills'])

# if the particular item is present or not in the in the dictionary
# print('skills' in person)  

# print('address' in person)
# print('first_name' in person)

#popitem are used to delete the last item in the dictionary 
# pop are used to delete the 


print(person.items());
# is used to convert the dictionary  to the list
# print(person)


# 


 