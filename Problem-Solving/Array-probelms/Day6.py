# better approach for the maximum subarray
def maxsubarrsum():
    a=[-2 ,1 ,-3, 4, -1, 2, 1, -5]
    max=0;
    for i in range(len(a)):
        sum=0;
        for j in range(i,len(a)):
            sum=sum+a[j];
            if sum>max:
                max=sum;     
    print(max)
# maxsubarrsum();

# optimal
def maxsubarrsum():
    a=[-2 ,1 ,-3, 4, -1, 2, 1, -5]
    max=float('-inf');
    sum=0;
    for i in range(len(a)):
        sum=sum+a[i];
        if sum>max:
            max=sum;
        if sum<0:
            sum=0;     
    print(max)

def minsubarrsum():
    a=[-2 ,1 ,-3, 4, -1, 2, 1, -5]
    min=float('inf');
    sum=0;
    for i in range(len(a)):
        sum=sum+a[i];
        if sum<min:
            min=sum;
        if sum>0:
            sum=0;     
    print(min)
minsubarrsum();
# maxsubarrsum();