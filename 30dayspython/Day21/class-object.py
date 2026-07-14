class dog:
    # __init__ it is intialising the constructor,self  parameter is the current instanse of the class
    def __init__(self,name,breed):
        self.name=name;
        self.breed=breed;




dog1 = dog("marry","pomoreon");
print(dog1.name);
print(dog1.breed);



import statistics
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
print(statistics.mean(ages));
print(statistics.mode(ages));
print(statistics.median(ages));
sum=0;
for i in ages:
    sum = sum+i;
print(sum)



# Create a class called PersonAccount. It has firstname, lastname, incomes,
#  expenses properties and it has total_income, total_expense, account_info, add_income, 
# add_expense and account_balance methods. Incomes is a set of incomes and its description. The same goes for expenses.

class person:
    def __init__(self,firname,lasname,income):
        self.firname=firname;
        self.lasname=lasname;
        self.income=income;

p1 = person("murari","kumar",13440);
print(p1.firname,p1.lasname,p1.income)