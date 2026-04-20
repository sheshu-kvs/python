# removing the list in the pyhton



a=['terra','from','mana','deva','mana'];
a.remove('terra');
print(a);

# removing the 2 items but it removes only the 1
a.remove('mana');
print(a);

# pop keyword are used o remove the specified index but it will also remove the last item if we not specified it will remove the last item
a.pop(0)
print("pop element at the specified index ",a)
# pop keyword with the no index
# a.pop()
print("pop keyword with the no index:",a.pop())


# del
# the del keyword aare used to remove the specified index
# the del keyword are used to remove the entire list

