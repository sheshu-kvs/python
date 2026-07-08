# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
tup1 = ("a","b","c");
tup2 = ("d","e","f");
siblings = tup1 + tup2;
print(siblings);

# How many siblings do you have?
print(len(siblings));

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members

fam=siblings+("mother","father");


# Unpack siblings and parents from family_members
# *sib grab all the elements from the tuple 
*sib,father,mother=fam;
print(sib);
print(father);
print(mother);

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruit=("apple","banana","guwa");
veg=("tomato","potato","onion");
animal=("milk","curd","ghee");
food_stuff_tp=fruit + veg + animal;
print(fruit + veg + animal);

# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt=list(food_stuff_tp);
print(food_stuff_lt);

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.

print(food_stuff_tp[4]);

# Slice out the first three items and the last three items from food_stuff_lt list
print(food_stuff_lt[0:4]);
print(food_stuff_lt[4:8]);

# Delete the food_stuff_tp tuple completely
del food_stuff_tp;
# print(food_stuff_tp);

# Check if an item exists in tuple:
if "potato" in food_stuff_lt:
    print("true");