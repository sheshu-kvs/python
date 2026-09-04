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

def fibonacci():
    print("Enter the number values to print the Fibonacci Sereis:")
    n=int(input())
    first=0;
    second=1;
    for i in range(n):
        print(first)
        tmp=second;
        second=first+second;
        first=tmp;
        

# findrectangle()
# swapvalues()
# greatestofthree()
# fibonacci();
vowelorconso();
