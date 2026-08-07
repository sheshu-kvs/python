# a=input();
# print(a)
# print(type(a));
# a=int(input());
# print(a)
# print(type(a));

# here map gives the special object
# val=input();
# print(val)
# print(type(val))
# vl_spl=input().split();
# print(vl_spl)
# we need to convert the integer & also map (it gives the special object)
# vl_spl=list(map(int, input().split()));
# print(vl_spl)
# print(type(vl_spl))

t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    try:
        res=a/b;
        print(int(res));
    except ZeroDivisionError as e:
        print("Error Code",e)
    except ValueError as v:
        print("Error Code",v)    