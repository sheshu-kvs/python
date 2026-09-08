def nestedList():
    nest_ls=[
        ["Harry",37.21],
        ["Berry",37.21],
        ["Tina",37.2],
        ["Akriti",41],
        ["Harsh",39]
    ]
    # print(nest_ls[1]);

    # using the list comprehension we can get the values
    ls_comprehension=[grade for name,grade in nest_ls];
    set_val=set(ls_comprehension)
    set_sort=sorted(set_val);
    second_low=set_sort[1];
    new_ls=[]
    for name,grade in nest_ls:
        if grade==second_low:
            new_ls.append(name)
            # jn="".join(rl);
            # print(jn)
    new_ls.sort();
    for name in new_ls:
        print(name)
    # using the traditonal loop
    # grade=[]
    # for student in nest_ls:
    #     grade.append(student[1])
    # print(grade)

# nestedList()




def nested_list_ip():
    nest_ls=[]
    n=int(input());
    for i in range(n):
        name=input();
        grade=float(input())
        nest_ls.append([name,grade])
    marks=[grade for name,grade in nest_ls];
    se_grade=set(marks);
    st_grade=sorted(se_grade)
    second_low=st_grade[1];
    new_ls=[];
    for name, grade in nest_ls:
        if grade==second_low:
            new_ls.append(name);
    new_ls.sort();
    for name in new_ls:
        print(name);


def hk():
    nest_ls=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        nest_ls.append([name,score])
    marks_ls=[grade for name,grade in nest_ls]
    new_set=set(marks_ls);
    st_vl=sorted(new_set);
    sc_low=st_vl[1];
    new_ls=[];
   
    for name,grade in nest_ls:
        if grade==sc_low:
            new_ls.append(name);
    new_ls.sort();
    for name in new_ls:
        print(name)

hk();
# nested_list_ip()