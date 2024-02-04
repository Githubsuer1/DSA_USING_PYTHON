def linearsearch(mylist,key,n):
    for i in range(0,n):
        if (mylist[i] == key):
            return i
    return -1
mylist = []
n = int(input("enter the size of list"))
print("enter the value to list")
for i in range(0,n):
    mylist.append(int(input()))
key = int(input("enter the num to search"))
res = linearsearch(mylist,key,n)
if res == -1:
    print("element not found ")
else:
    print("element found at index",res)