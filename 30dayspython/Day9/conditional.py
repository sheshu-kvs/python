# Get user input using input(“Enter your age: ”). If user is 18 or older,
#  give feedback: You are old enough to drive. If below 18 give feedback to wait
#  for the missing amount of years.
#  Output:

# age=int(input("Enter the Age"));
# if  age>18:
#     print("Your Enough to Drive");
# else:
#     print("Your Not Able Drive");


# Compare the values of my_age and your_age using
# if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input.
# You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger
#  differences, and a custom text if my_age = your_age. Output:

# my_age=int(input("Enter the age"));
# your_age=int(input("Enter the age"));

# if my_age > your_age:
#     print(f"you are Greater than my age");
# elif my_age<your_age:
#     print(f"the your age was  Greater ");
# elif my_age == your_age:
#     print(f"My age is equal to Your Age");
# else:
#     print("Please Enter the Valid Input");

# Write a code which gives grade to students according to theirs scores:

# ```sh
# 90-100, A
# 80-89, B
# 70-79, C
# 60-69, D
# 0-59, F
# ```

# marks = int(input("Enter The Marks:"));
# if marks >= 90 and marks <= 100:
#     print("A");
# elif marks >= 80 and marks <= 89:
#     print("B");
# elif marks >= 70 and marks <= 79:
#     print("C");
# elif marks >= 60 and marks <= 69:
#     print("D");
# elif marks >= 0  and marks <= 59:
#     print("Fail");
# else:
#     print("Please Enter the Valid Input");


# Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. 
# If the user input is: September, October or November, the season is Autumn. December
# , January or February, the season is Winter. March, April or May, the season is Spring June,
# July or August, the season is Summer

# season=input("Enter the Season");
# if season == "sep" or season == "oct" or season =="nov":
#     print("autumn");
# elif season == "dec" or season =="jan" or season == "feb":
#     print("Winter");
# elif season == "mar" or season =="apr" or season == "may":
#     print("Spring");
# elif season == "jun" or season =="july" or season == "august":
#     print("summer");



# ```sh
# # fruits = ['banana', 'orange', 'mango', 'lemon']
# ```

# If a fruit doesn't exist in the list add the fruit to the list 
# and print the modified list. If the fruit exists 
# print('That fruit already exist in the list')
fruits = ['banana', 'orange', 'mango', 'lemon'];
f1=input("Enter the Fruit Name:");
if f1 not in fruits:
    fruits.append(f1);
    print(fruits)
elif f1 in fruits:
    print("Fruit Exists");


#  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
#  * If a person skills has only JavaScript and React, print('He is a front end developer'),
#  if the person skills has Node, Python, MongoDB, print('He is a backend developer'),
#  if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') 
# - for more accurate results more conditions can be nested!
#  * If the person is married and if he lives in Finland, print the information in the following format:



person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }