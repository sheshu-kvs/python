# Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def sum(a,b):
    add=a+b;
    print(add);

sum(10,5);


def arc():
    radius=2;
    areaofcircle=3.14*2*2;
    print(areaofcircle);

arc();

def findseason(season):
    if season=="rainy":
        print("this is the aug");
    if season=="summner":
        print("this is march");
    if season=="winter":
        print("this is oct");

findseason("winter");


# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).

def reverse_list(lis):
    for i in range(len(lis)-1,-1,-1):
        print(lis[i]);



# print(reverse_list([1, 2, 3, 4, 5]))



print(reverse_list(["A", "B", "C"])) 

# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items

def capitalize(lis):
    print(lis.upper());

capitalize("absd")


# Declare a function named capitalize_list_items. 
# It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(lis,val):
    lis.append(val);
    print(lis);

capitalize_list_items(["array","memory","value"],"data");

# Declare a function named sum_of_numbers. It takes a number parameter
#  and it adds all the numbers in that range.

# print(sum_of_numbers(5))  # 15
# print(sum_of_numbers(10)) # 55
# print(sum_of_numbers(100)) # 5050

sum=0;
rem=0;

def sum_of_values(num):
    while(num>0):
        rem = rem % 10;
        sum = sum+rem;
        num=num/10;
print(sum);


sum_of_values(5)

