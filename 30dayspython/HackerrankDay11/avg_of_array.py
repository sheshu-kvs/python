print("Enter the number of Students:")
n=int(input());
students={}
sum={};
for i in range((n)):
    stu=input().split();
    name,*mar=stu;
    students[name]=mar;
# print("Enter the stu name:")
# name=input();
# print(students[name])
tot={}
for val in students:
    print(students[val])
    for val_idx in students[val]:
        tot=tot+students[val_idx]