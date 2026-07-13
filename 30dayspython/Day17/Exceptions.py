# an example wrong i/p wrong data the python program will immediately crash
#  to prevent this we are using the try, except,else,finally
# try are used to the execute the prgm, except which means the exception 
# if anything goes wrong(error) the exception code will trigger, if exception 
# is not mentioned it will go the else statement, finaly are used to execute 
# 
try:
   a=10;
   b=0;
   print((a/b));
except Exception as e:
    print(e); 


def sum_of_values(a,b,c,d,e):
    return a+b+c+d+e;

lis=[1,2,3,4,5];
print(sum_of_values(*lis))
# when we write this  lis it will take as numbers, not the list 


city=['hospet','bellary','dvg','raichur','gulbarga','yadgir','shorpur'];
a,b,c,d,*e=city;
#*e will store the remaining itmes
print(a)
print(b)
print(c)
print(d)
print(e)

# Enummerate are used to the get the list items in the index
city=['hospet','bellary','dvg','raichur','gulbarga','yadgir','shorpur'];

for index, i in enumerate(city):
    # index is the idx , i is the item
    if i=='bellary':
        print(i," Found in the postion ",index);


# Zip Enumerate are used  to combine two list

fruits = ['banana', 'orange', 'mango', 'lemon', 'lime'];                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot'];

lis_fruits_vegs=[];

for fru,veg in zip(fruits,vegetables):
    lis_fruits_vegs.append({"Fruit ":fru,"Vegetable ":veg});

print(lis_fruits_vegs);




# names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']. 
# Unpack the first five countries and
#  store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively.\

names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia'];
a,b,c,d,e,*f=names;
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
