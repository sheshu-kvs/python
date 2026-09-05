

def setremove():
    # n=int(input())
    s12=set(map(int,input().split()))
    num=int(input())
    
    
    for i in range(num):
        ip=input().split()
        if len(ip)>1:
            if ip[0]=="remove":
                 val2=int(ip[1]);
                 s12.remove(val2);
            elif ip[0]=="discard":
                 val2=int(ip[1]);
                 s12.discard(val2);
        elif len(ip)==1 and ip[0]=="pop":
            s12.pop();
    
    print(int(s12))





setremove();
