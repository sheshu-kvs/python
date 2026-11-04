def largest():
    # brute
    # a=[2,12,11,2,3];
    # print(max(a));
    a=[2,12,11,2,3];
    # optimal
    max=float('-inf');
    for val in a:
        if val>max:
            max=val;
    print(max);



def secondlg():
    a=[1,2,3,5,5,9];
    # Brute 
    # sc=sorted(a,reverse=True);
    # print(sc)
    # optimal
    #  o(n)
   
    largest=secondlargest=float('-inf');
  
    if len(a)==1:
        print("Not Found Second Largest Element");
    else:
        for val in a:
            if val>largest:
                secondlargest=largest;
                largest=val;
            elif val>secondlargest and val!=largest:
                secondlargest=val;
        print(secondlargest);

def checkifsorted():
    a=[1,2,3,4,4,6];
    for i in range(len(a)-1):
        if a[i]>a[i+1]:
            return "Not Sorted"
    return "Sorted";

print(checkifsorted());
# secondlg();
# largest();
