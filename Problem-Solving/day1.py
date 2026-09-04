def findrectangle():
    print("Enter the lenght:")
    l=int(input());
    print("Enter the Width:")
    w=int(input());
    print("The area of rectangel:",(l*w));


def swapvalues():
    print("Enter the value of a:")
    a=int(input());
    print("Enter the value of b:")
    b=int(input());
    a=a+b;
    b=a-b;
    a=a-b;
    print("The a Val",a)
    print("The b Val",b)


def greatestofthree():
    a=int(input())
    b=int(input())
    c=int(input())
    if a>b and a>c:
        print(a ,"is greater");
    elif b>c and b>a:
        print(b,"is greater");
    elif c>a and c>b:
        print(c,"is greater");


def vowelorconso():
    val=input();
    lw=val.lower();
    if lw=='a' or lw=='e'or lw=='i'or lw=='o'or lw=='u':
        print(lw,"is Vowels");
    else:
        print(lw,"is Consonent");

# findrectangle()
# swapvalues()
# greatestofthree()
vowelorconso();
