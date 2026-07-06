# In Python and other programming languages \ followed by a character is an escape sequence. Let us see the most common escape characters:

# \n: new line
# \t: Tab means(8 spaces)
# \\: Back slash
# \': Single quote (')
# \": Double quote (")
# Now, let us see the use of the above escape sequences with examples.


print("Everyone is Enjoying python language \n are you?");
print("Days\tTopics\tExercises");
print("1\t5\t2");
print("2\t6\t3");
print("3\t2\t1");
print("1\t3\t2");


print("Hello this is the \\b backslash");
print("Hello this is the \"Double quote\"");


lang="python";
a,b,c,d,e,f=lang;
print(a);
print(b);
print(c);
print(d);
print(e);
print(f);


greeting="Hello,World";
# print(greeting[::-1]);

t=""
for i in range(len(greeting)-1,-1,-1):
    t=t+greeting[i];
print(t);

# iterating the item by item


lang="python";

print(lang[0:6:2]);  
# even loop i,e start from 0,end to 6 , skip 2(step)
print(lang[1:6:2]);



# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
a='Thirty';
b="Days";
c="Of";
d="Python";

print(a+" "+b+" "+c+" "+b);


# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.

a="Coding";
b="For";
c="All";
print(a+" "+b+" "+c);


# Declare a variable named company and assign it to an initial value "Coding For All".
company="Coding For All";
print(company[0]);

# Print the length of the company string using len() method and print().
print(len(company));

# Change all the characters to uppercase letters using upper() method.
print(company.upper());

# Change all the characters to lowercase letters using lower() method.
print(company.lower());


# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())

# Converts the First char of the string to Capital capitalize()
print(company.title());
# Converts the Each starting character to be the capital



# Cut(slice) out the first word of Coding For All string.
print(company[0]);

# Check if Coding For All string contains a word Coding using the method index, find or other methods.
print("check the index",company.lower().find("coding"));


# Replace the word coding in the string 'Coding For All' to Python.
print(company.replace("Coding","Python"));

# Change "Python for Everyone" to "Python for All" using the replace method or other methods.

company2="Python for Everyone";
print(company2.replace("python","Python For All"));


# Split the string 'Coding For All' using space as the separator (split()) .
print(company.split(" "));

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
mang="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon";
print(mang.split(" "));


# Create an acronym or an abbreviation for the name 'Coding For All'.
# We need to Print the CFA
words=company.split(" ");
acor="";
for word in words:
    acor=acor+word[0];
print(acor);


# Create an acronym or an abbreviation for the name 'Coding For All'.
words = company2.split(" ");
acor="";
for word in words:
    acor=acor+word[0];
print(acor)

# Use index to determine the position of the first occurrence of C in Coding For All.
print(company.index("C"));


# Use index to determine the position of the first occurrence of F in Coding For All.
print(company.index("F"));

# Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(company.rfind("l"));

# Does 'Coding For All' start with a substring Coding?
print(company.startswith("Coding"))

# Does 'Coding For All' end with a substring coding?
print(company.endswith("Coding"))


# Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python

# Checks the valid string , it should not start with the number
val1="30DaysOfPython";
val2="thirty_days_of_python";

print(val1.isidentifier())
print(val2.isidentifier())


# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. 
# Join the list with a hash with space string.

libraries=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon'];
joinghash="#".join(libraries);
print(joinghash)



# Use a tab escape sequence to write the following lines.
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki


print("Name\t\tAge\tCountry\t\tCity")
print("Asabeneh\t250\tFinland\t\tHelsinki")

# Use the string formatting method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.

radius = 10
area = 3.14 * radius ** 2

print(f"The area of a circle with radius {radius} is  {area} meters square");

# Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144


a=8;
b=6;
print(f"{a} + {b} = {a+b}");
print(f"{a} - {b} = {a-b}");
print(f"{a} * {b} = {a*b}");
print(f"{a} / {b} = {a/b}");
print(f"{a} % {b} = {a%b}");
print(f"{a} // {b} = {a//b}");
print(f"{a} ** {b} = {a**b}");