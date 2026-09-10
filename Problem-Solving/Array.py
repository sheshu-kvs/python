# largest element in the array
def lgfirst():
    ls=list(map(int,input("Enter the array Elements:").split()));
    # Brute Force
    # ls.sort();
    # print(ls)
    # print("Largest element",ls[len(ls)-1])

    # optimal approach
    lg=ls[0];
    for i in  range(len(ls)):
        if ls[i]>lg:
            lg=ls[i];
    print("Largest Element:",lg)


def secondlg():
   ls=list(map(int,input("Enter the array Elements:").split()));
    # min val -inf
   fl=float('-inf') 
   sl=float('-inf')
   for i in range(len(ls)):
       if ls[i]>fl:
        sl=fl;
        fl=ls[i];
       elif ls[i]>sl and ls[i]!=fl:
          sl=ls[i];
   print(sl);
           
       
        


# lgfirst()
secondlg()
