def dequeex():
    from collections import deque
    d=deque();
    n=int(input());
    for i in range(n):
        ip=input().split();
        val1=ip[0];
        
        if len(ip)==1:
            if val1=="pop":
                d.pop();
            elif val1=="popleft":
                d.popleft();
        elif len(ip)>1:
              val2=int(ip[1]);
              if val1=="append":
                d.append(val2);
              elif val1=="appendleft":
                d.appendleft(val2);
    print(*d)
# from collections import deque
# d=deque();
# d.append(1);
# d.appendleft(11);
# print(d)

dequeex()