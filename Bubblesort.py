def BubbleSort(list1):
    for i in range(1,len(list1)):
        for j in range(len(list1)-i):
            if list1[j]>list1[j+1]:
                list1[j],list1[j+1] = list1[j+1],list1[j]
    return list1
list1 = [21,16,13,28,24,33,9,32]
print(BubbleSort(list1))
