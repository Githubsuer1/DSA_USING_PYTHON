def insertionSort(list1):
    for i in range(1,len(list1)):
        temp = list1[i]
        j = i-1

        while(j>=0 and temp<list1[j]):
            list1[j+1] = list1[j]
            j-=1
        list1[j+1] = temp

    return list1

list1 = [13,3,7,10,9]
print(insertionSort(list1))
