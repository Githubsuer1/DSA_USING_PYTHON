def Binarysearch(mylist,key,n):
    l = 0
    u = n-1
    while(l<=u ):
        mid = (l + u)//2

        if(key == mylist[mid]):
            # return mid
            break
        elif (key > mylist[mid]):
            l = mid + 1
        else:
            u = mid - 1

    if (l == n):
        return -1
    elif (u == -1):
        return -1
    else:
        return mid

mylist = []
n = int(input('enter the size of list'))
print("enter the value to list")
for i in range(0,n):
    mylist.append(int(input()))
key = int(input('enter the item to search '))
res = Binarysearch(mylist, key, n)
if res == -1:
    print("element not found")
else:
    print("element found at index ", res)