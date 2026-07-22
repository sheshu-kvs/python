# arr=[]
# print(12)
# arr.insert(0,5)
# arr.insert(1,10)
# arr.insert(0,6)
# print(arr)
# # itemrem=6;
# arr.remove(6)
# print(arr)
# arr.append(9)
# arr.append(1)
# print(arr)
# arr.sort();
# print(arr)
# arr.pop()
# print(arr);
# arr.reverse();
# print(arr)


# User i/p

if __name__=='__main__':
    n=int(input()).strip();
    arr=[]
    for _ in range(n):
        command_line=input();
        cmd = command_line[0];
        if cmd =="insert":
            item=int(command_line[1]);
            idx=int(command_line[2]);
            arr.insert(idx,item);
        elif cmd=="print":
            print(arr);
        elif cmd =="remove":
            rem=int(command_line[1]);
            arr.remove(rem);
        elif cmd=="append":
            apd=int(command_line[1]);
            arr.append(apd);
        elif cmd=="sort":
            arr.sort();
        elif cmd=="pop":
            arr.pop();
        elif cmd =="reverse":
            arr.reverse();
        else:
            print("Not valid")
