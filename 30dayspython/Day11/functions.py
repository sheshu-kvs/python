# # Declare a function add_two_numbers. It takes two parameters and it returns a sum.
# def sum(a,b):
#     add=a+b;
#     print(add);

# sum(10,5);


# def arc():
#     radius=2;
#     areaofcircle=3.14*2*2;
#     print(areaofcircle);

# arc();

# def findseason(season):
#     if season=="rainy":
#         print("this is the aug");
#     if season=="summner":
#         print("this is march");
#     if season=="winter":
#         print("this is oct");

# findseason("winter");


# # Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
# # Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).

# def reverse_list(lis):
#     for i in range(len(lis)-1,-1,-1):
#         print(lis[i]);



# # print(reverse_list([1, 2, 3, 4, 5]))



# print(reverse_list(["A", "B", "C"])) 

# # Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items

# def capitalize(lis):
#     print(lis.upper());

# capitalize("absd")


# # Declare a function named capitalize_list_items. 
# # It takes a list as a parameter and it returns a capitalized list of items
# def capitalize_list_items(lis,val):
#     lis.append(val);
#     print(lis);

# capitalize_list_items(["array","memory","value"],"data");

# # Declare a function named sum_of_numbers. It takes a number parameter
# #  and it adds all the numbers in that range.

# # print(sum_of_numbers(5))  # 15
# # print(sum_of_numbers(10)) # 55
# # print(sum_of_numbers(100)) # 5050


# num=5;
# sum=0
# while num>0:
#     print(num);
#     sum = sum + num;
#     num=num-1;
# print("sum",sum)


# def sum_of_values(num):
#     sum=0;
#     while(num>0):
#         sum=sum +num;
#         num=num-1;
#     print(sum);

# sum_of_values(100);

   

# # food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
# # print(remove_item(food_stuff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
# # numbers = [2, 3, 7, 9]
# # print(remove_item(numbers, 3))  # [2, 7, 9]

# food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk'];


# def foodremove(lis,item):
#     lis.remove(item);
#     print(lis);

# foodremove(food_stuff,"Milk");


# numbers = [2, 3, 7, 9]

# def remove_item(lis,num):
#     lis.remove(num);
#     return lis;
# print(remove_item(numbers, 3))  # [2, 7, 9]



# print(sum_of_numbers(5))  # 15
# print(sum_of_numbers(10)) # 55
# print(sum_of_numbers(100)) # 5050


# Declare a function named sum_of_odds. It 
# takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(num):
    sum12=0;
    while num>0:
        if num%2!=0:
            sum12=sum12+num;
        num=num-1    
    print("sum of odds",sum12);   

sum_of_odds(5);


def sum_of_evens(num):
    sum12=0;
    while num>0:
        if num%2==0:
            sum12=sum12+num;
        num=num-1    
    print("sum of evens",sum12);   

sum_of_evens(5);
# print(sum_of_odds);



# Declare a function named evens_and_odds . It takes 
# a positive integer as parameter and it counts number of evens and odds in the number.

def sum_of_odds(num):
    sum12=0;
    count=0;
    while num>0:
        if num%2!=0:
            sum12=sum12+num;
            count = count + 1;
        num=num-1    
    print("Count Number of odds",count);   

sum_of_odds(100);

count=0;
for i in range(100,-1,-1):
    if i%2!=0:
        count=count+1;
print(count)

def fact(num):
    fact=1;
    while num > 0:
        fact =  fact*num;
        num=num-1;
    print("Factorial Of Number ",fact);

fact(5);