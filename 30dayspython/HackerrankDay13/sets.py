val=int(input());

for i in range(val):
    val1=list(map(int, input().split()));
    a,b=val1;
    try:
        print(a/b);
    except ZeroDivisionError as e:
        print("Error Code:",e);
    except ValueError as e:
        print("Error Code:",e);

