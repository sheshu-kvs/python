import os
print(os.path)



f=open("read_file.txt");
# txt = f.read();

# read only the 10 chars
txt = f.read(10);
# print(txt)
# print(txt)
# readline() are used to read only the first line
# f.close()
txtline=f.readline()
# it strictly reads the first line only for ex:: after the , is there in the word 
# means  it will  read the next line
# print(txtline)
txtlines = f.readlines();
# print(txtlines)
# print(type(txt))


# after opening the file we need to close the file, 
# there is a high tendency to close the file, so we can use the ::::with::::

# with open("read_file.txt") as f:
#     txt = f.read();
#     print(txt)


# writing the file, if the file not exits it will create the new file
with open("read_file1.txt","w") as f:
    f.write("This Is the New File");
    print(f)
