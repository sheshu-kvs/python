def binarysearchof2d():
    # a=[
    #         [1,2,3],
    #         [4,5,6],
    #         [7,8,9]
    #     ]

    # for row in a:
    #     for col in row:
    #         print(col,end=" ")
    

    # 2D Explanation
    # 0   1 -> 2
    # 0   2 -> 3
    # 1   0 -> 4
    # 1   1 -> 5
    # 1   2 -> 6
    # 2   0 -> 7
    # 2   1 -> 8
    # 2   2 -> 9
    # tar=6
    # for i in range(len(a)):
    #     for j in range(len(a)):
    #         print(i," ",j,"->",a[i][j])
    #         if a[i][j]==tar:
    #             print("Found")
    #             break;



    # For 1D array
    # a=[1,2,4,12,56,57,90];

    # low=0; 
    # high=len(a);
   
    # target=570;
    # while low<high:
    #     mid=(low+high)//2;
    #     if a[mid]==target:
    #         return mid;
    #     elif a[mid]<target:
    #         low=mid+1;
    #     else:
    #         high=mid-1;
    # return False;



    # For 2d Array of the binary search
    a=[[1,3,5,7],
       [10,11,16,20],
       [23,30,34,60]]

    rows=len(a)
    cols=len(a[0])
    low=0;
    high=(rows*cols)-1;
    target=112;
    while low<high:
        mid=(low+high)//2;
        r=mid//cols;
        c=mid%cols;
        val=a[r][c];
        if val==target:
            return "Found";
        elif val<target:
             low=mid+1;
        else:
            high=mid-1;
    return"Not Found";

  

# print(binarysearchof2d())
# binarysearchof2d()
print(binarysearchof2d())
