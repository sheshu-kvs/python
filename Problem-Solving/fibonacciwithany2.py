def fibo():
    num1=1;
    num2=5;
    for i in range(5):
        print(num1);
        temp=num2;
        num2=num1+num2;
        num1=temp;



def swapchar():
    ch=input("Enter the Character to swap:")
    print(ch.swapcase())
    

def countnumberofdigit():
    num=1234;
    count=0;
    while num>0:
        rem=num%10;
        count+=1;
        num=num//10;
    print("The number of the digits:",count);


def reversenum():
    num=1234;
    rev=0;
    while num>0:
        rem=num%10;
        rev=rev*10+rem;
        num=num//10;
    print("Reverse an number:",rev);


def palin():
    ip=121;
    num=ip;
    rev=0;
    while num>0:
        rem=num%10;
        rev=rev*10+rem;
        num=num//10;
    print(ip)
    print(rev)
    if ip==rev:
        print("Entered number is the palindrome",rev)
    else:
        print("Entered number not the palindrome ",rev)

palin();
# reversenum();
# countnumberofdigit();
# swapchar();
# fibo();
