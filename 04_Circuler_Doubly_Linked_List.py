# Node Class to create Node
class Node:
    def __init__(self,prev = None, item = None, next = None):
        self.prev = prev
        self.item = item
        self.next = next

# CDLL class to implement circular doubly linked list
class CDLL:
    def __init__(self, start = None):
        self.start = start

#--------- method to check whether linked list is empty or not ---------#
    def is_empty(self):
        return self.start == None

#------------------ insertion in circular doubly linked list ---------------------#
    def insert_at_start(self,data):
        N = Node(None,data,None)
        if self.is_empty():
            N.next = N
            N.prev = N
            self.start = N
        else:
            N.next = self.start
            N.prev = self.start.prev
            self.start.prev.next = N 
            self.start.prev = N 
            self.start = N

    def insert_at_last(self,data):
        N = Node(None,data,None)
        if self.is_empty():
            N.next = N 
            N.prev = N 
            self.start = N
        else:
            N.next = self.start 
            N.prev = self.start.prev 
            self.start.prev.next = N 
            self.start.prev = N

#--------- to search particular data in linked list -----------#
    def search(self,data):
        if self.start is not None:
            temp = self.start
            if temp.item == data:
                return temp
            else:
                temp = temp.next
            
            while temp is not self.start:
                if temp.item == data:
                    return temp
                temp = temp.next
            return None
        else:
            return None


    def insert_after(self,temp,data):
        if temp is not None:
            N = Node(None,data,None) 
            N.next = temp.next 
            N.prev = temp 
            temp.next.prev = N
            temp.next = N

#------------------ deletion of data in linked list ---------------------#
    def delete_first(self):
        if not self.is_empty():
            if self.start.next == self.start:
                self.start = None
            else:
                self.start.prev.next = self.start.next 
                self.start.next.prev = self.start.prev
                self.start = self.start.next
    
    def delete_last(self):
        if not self.is_empty():
            if self.start.next == self.start:
                self.start = None
            else:
                self.start.prev.prev.next = self.start
                self.start.prev = self.start.prev.prev

    def delete_item(self,data):
        if self.start is not None:
            temp = self.start 
            if temp.item == data:
                self.delete_first()
            else:
                temp = temp.next 
                while temp.next is not self.start:
                    if temp.item == data:
                        temp.prev.next = temp.next
                        temp.next.prev = temp.prev
                        break
                    temp = temp.next 
    
#------------ Display ------------#
    def display(self):
        if not self.is_empty():
            temp = self.start 
            print(temp.item, end = " ")
            temp = temp.next
            while temp is not self.start: 
                print(temp.item, end = " ")
                temp = temp.next 

# creating object of CDLL class to invoke the methods to insert and delete the data from the list
myList = CDLL()
myList.insert_at_start(10)
myList.insert_at_start(9)
myList.insert_at_start(8)
myList.insert_at_start(7)
myList.insert_at_start(6)

myList.delete_first()
myList.delete_first()
myList.delete_first()
myList.delete_first()

myList.insert_at_last(11)
myList.insert_at_last(12)

myList.insert_after(myList.search(10),30)
myList.insert_after(myList.search(30),31)

myList.delete_item(31)
myList.delete_last()
myList.display()