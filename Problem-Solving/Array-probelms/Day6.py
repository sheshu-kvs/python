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
    # a=[-2 ,1 ,-3, 4, -1, 2, 1, -5]
    a=[-1,2]
    max=float('-inf');
    sum=0;
    if len(a)==1:
        print(a[0]);
    else:
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


def printsubarrsum():
    a=[2,3,7,1,5];
    sum=12;
    for i in range(len(a)):
        sm=0;
        count=0
        for j in range(i,len(a)):
            sm=sm+a[j];
            count+=1
            if sm==sum:
                # print(sm)
                for val in range(i,count+1):
                    print(a[val]);
                    
# minsubarrsum();
# maxsubarrsum();
printsubarrsum();