n=int(input());
stu_lst={};
for i in range(n):
    name=input();
    marks=float(input());
    stu_lst[name]=marks;

values={}
for val in stu_lst:
    values=stu_lst[val];

print(values)