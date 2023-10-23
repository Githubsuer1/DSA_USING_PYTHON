# Node Class to create Node
class Node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next 

# SSL class to implement singly linked list
class SLL:
    def __init__(self,start=None):
        self.start = start

#--------- method to check whether linked list is empty or not ---------#
    def is_empty(self):
        return self.start == None

#--------- to search particular data in linked list -----------#
    def search(self,data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None

#------------------ insertion in singly linked list ---------------------#
    def insert_at_start(self,data):
        N = Node(data,self.start)
        self.start = N

    def insert_at_last(self,data):
        N = Node(data,None)
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = N
        else:
            self.start = N

    def insert_after(self,temp,data):
        if temp is not None:
            N = Node(data,temp.next)
            temp.next = N

#------------------ deletion of data in linked list ---------------------#
    def delete_at_start(self):
        if self.start is not None:
            temp = self.start
            self.start = temp.next 
    
    def delete_at_last(self):
        if self.start is not None:
            if self.start.next == None:
                self.start = None
            else:
                temp = self.start
                while temp.next.next is not None:
                    temp = temp.next
                temp.next = None
        else:
            pass

    def delete_specific(self,data):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item == data:
                self.start = None
        else:
            temp = self.start
            if temp.item == data:
                self.start = temp.next
            else:
                while temp is not None:
                    if temp.next.item == data:
                        temp.next = temp.next.next
                        break
                temp = temp.next


#------------ Display ------------#
    def display(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=" ")
            temp = temp.next


# creating object of SLL class to invoke the methods to insert and delete the data from the list
myList = SLL()

#----------- insertion at the start -------------#
myList.insert_at_start(100)
myList.insert_at_start(90)
myList.insert_at_start(80)
myList.insert_at_start(70)
myList.insert_at_start(60)

#----------- insertion after given data ---------#
myList.insert_after(myList.search(60),65)
myList.insert_after(myList.search(70),75)
myList.insert_after(myList.search(80),85)
myList.insert_after(myList.search(90),95)
myList.insert_after(myList.search(100),105)

#------------ insertion in last------------------#
myList.insert_at_last(110)
myList.insert_at_last(115)
myList.insert_at_last(120)
myList.insert_at_last(125)
myList.insert_at_last(130)

#------------- deletion in start-----------------#
# myList.delete_at_start()
# myList.delete_at_start()

# #------------- deletion in last-----------------#
# myList.delete_at_last()
# myList.delete_at_last()

#------------- deletion of specific ------------#
myList.delete_specific(70)
myList.delete_specific(80)
myList.delete_specific(90)
myList.delete_specific(100)
# myList.delete_specific(105)



#----------- displaying the list ----------------#
myList.display()
