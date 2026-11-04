def rev():
    s="hello";
    # approach 1
    # val='';
    # for c in s:
    #     val=c+val;
    # print(val);
    # approach 2
    # res="".join(list(s[::-1]));
    # print(res);
    n=len(s);
    for i in range (n//2):
        s[i],s[n-i-1]=s[n-i-1],s[i];
    print(s)

rev();