print("Enter the number of stu:")
n=int(input())
students={}
for i in range(n):
    stu=input().split();
    name,*mark=stu;
    marks=list(map(int, mark))
    
    students[name]=marks;
print(students)
tot=0;
name=input();
for mark12 in students[name]:
    tot+=mark12;
    len12=len(students[name]) 
print(f"{tot/len12:.2f}")