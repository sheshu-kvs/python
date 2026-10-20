
def findmaxsuminRow():
    a=[[1,2,3],[4,5,6],[7,8,9]];
    max=0;
    # for row in a:
    #     sum=0
    #     for val in row:
    #         sum=sum+val;
    #         if sum>max:
    #             max=sum;
    # print(max);

    # another brute
    # O(m*n)
    for i in range(len(a)):
        val=sum(a[i]);
        if val>max:
            max=val;
    # print(max);

    # optimal
    # val=list(map(sum,a))
    # enummerate will return the index
    # val=list(enumerate(map(sum,a)))
    max_row,max_sum=max(enumerate(map(sum,a)), 
            key=lambda x:x[1])
    
    print(max_row)
    print(max_sum)
    print(val)

findmaxsuminRow()
