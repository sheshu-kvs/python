# Declare an empty list

# Declare a list with more than 5 items

# Find the length of your list

# Get the first item, the middle item and the last item of the list

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.

# Print the list using print()

# Print the number of companies in the list

# Print the first, middle and last company

# Print the list after modifying one of the companies

lst=[]
print(lst);


# Declare a list with more than 5 items
lst=['a','b','c','d','e'];
print(lst)

# Find the length of your list
print(len(lst));

# Get the first item, the middle item and the last item of the list
print(lst[0]);
resmid=len(lst)//2;
print(lst[resmid]);
reslast=len(lst)-1;
print(lst[reslast]);


# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.

it_companies=["facebok",'Google','Microsoft','apple','ibm','oracle','amazon'];
print(it_companies);

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
print(len(it_companies));

# Print the first, middle and last company
print(it_companies[0]);

midle=len(it_companies)//2;
print(it_companies[midle]);

lstcompany=len(it_companies)-1;
print(lstcompany);


# Print the list after modifying one of the companies
it_companies[0]="meta";
print(it_companies);

# Add an IT company to it_companies
it_companies.append("Zoho");
print(it_companies);


# Insert an IT company in the middle of the companies list
it_companies.insert(4,"VistRA");
print(it_companies);


# Change one of the it_companies names to uppercase (IBM excluded!)
firslst=it_companies[0].upper();

new_itompanies="";
for i in range(len(it_companies)):
    if i==0:
        new_itompanies=it_companies[i].upper()+" ";
    else:
        new_itompanies=new_itompanies+it_companies[i]+" ";
print(new_itompanies);


# Join the it_companies with a string '#;  '
# resjn="# " .join(it_companies);
# print(resjn)


#Check if a certain company exists in the it_companies list.

# for cer in it_companies:
if "Zoho" in it_companies:
    print("True");
else:
    print("False")


# Sort the list using sort() method

# print(sort(it_companies))

# it_companies.sort(key=str.lower)
# print(it_companies)


# it_companies.sort(key=str.lower,reverse=True);
# print(it_companies)

# it_companies.reverse()
print(it_companies)

print(it_companies[0:3]);

print(it_companies[3:6])

# Remove the first IT company from the list
it_companies.remove("meta");
print(it_companies)


# Remove the middle IT company or companies from the list
it_companies.pop(3)
print(it_companies);


# Remove the last IT company from the list
print(it_companies.pop());

# Remove all IT companies from the list
it_companies.clear();
print(it_companies)

# Destroy the IT companies list
del it_companies;
# print(it_companies)

# 
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack=front_end+back_end;
print(full_stack);

# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sort the list and find the min and max age

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort();
print(ages);

# Sort the list and find the min and max age
print(max(ages))
print(min(ages))

# Add the min age and the max age again to the list
maxval = max(ages);
minval = min(ages);
ages.append(maxval);
ages.append(minval);
print(ages)

# Find the median age (one middle item or two middle items divided by two)

# Find the average age (sum of all items divided by their number )
sum=0;
avg="";
for val in ages:
    sum=sum+val;
print(sum)

avg=sum/len(ages);
print(avg);


# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
tup1 = ("a","b","c");
tup2 = ("d","e","f");
print(tup1 + tup2);
