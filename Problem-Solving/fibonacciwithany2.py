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
    num=1234;
    rev=0;
    valrl=num
    while num>0:
        rem=num%10;
        rev=rev*10+rem;
        num=num//10;
    if valrl==rev:
        print("Entered number is the palindrome",num)
    else:
        print("Entered number is the palindrome",num)

palin();
# reversenum();
# countnumberofdigit();
# swapchar();
# fibo();