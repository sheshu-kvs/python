n=int(input("Enter the Year"))
if (n%4==0 or n%400==0) and (n%100!=0):
    print("leap");
else:
    print("Not Leap");