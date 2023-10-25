# Node Class to create Node

class Node:
    def __init__(self,item = None,next = None):
        self.item = item
        self.next = next

#----------CLL class to implement circular linked list-----------------#

class CLL:
    def __init__(self,last=None):
        self.last = last

#--------- method to check whether linked list is empty or not ---------#

    def is_empty(self):
        return self.last == None

#------------------ insertion in singly linked list ---------------------#

    def insert_at_start(self,data):
        N = Node(data)
        if self.is_empty():
            N.next = N
            self.last = N
        else:
            N.next = self.last.next
            self.last.next = N

    def insert_at_last(self,data):
        N = Node(data)
        if self.is_empty():
            N.next = N
            self.last = N
        else:
            N.next = self.last.next
            self.last.next = N
            self.last = N

    def insert_after(self,temp,data):
        if temp is not None:
            N = Node(data,temp.next)
            temp.next = N
            if temp == self.last:
                self.last = N
            
# --------------- search function ----------------#
    def search(self,data):
        if self.is_empty():
            return None
        temp = self.last.next
        while temp is not self.last:
            if temp.item == data:
                return temp
            temp = temp.next
        if temp.item == data:
            return temp
        return None
    


#------------ Display ------------#
    def display(self):
        if not self.is_empty():
            temp = self.last.next
            while temp is not self.last:
                print(temp.item,end=" ")
                temp = temp.next 
            print(temp.item)

#------------------ deletion of data in linked list ---------------------#

    def delete_first(self):
        if not self.is_empty():
            if self.last.next == self.last:
                self.last = None
            else:
                self.last.next = self.last.next.next 


    def delete_last(self):
        if not self.is_empty():
            if self.last.next == self.last:
                self.last = None
            else:
                temp = self.last.next
                while temp.next is not self.last:
                    temp = temp.next 
                temp.next = self.last.next
                self.last = temp

    def delete_item(self,data):
        if self.last == None:
            pass
        elif self.last.next == self.last:
            if self.last.item==data:
                self.last = None
        else:
            temp = self.last.next
            if temp.item == data:
                self.last.next = temp.next
            else:
                while temp.next is not self.last:
                    if temp.next.item == data:
                        temp.next = temp.next.next
                        break
                    temp = temp.next 
                if temp.next.item == data:
                    temp.next = self.last.next
                    self.last = temp 

# creating object of CLL class to invoke the methods to insert and delete the data from the list
myList = CLL()

myList.insert_at_start(10)
myList.insert_at_start(8)
myList.insert_at_start(7)
myList.insert_at_start(6)
myList.insert_at_start(5)

myList.insert_after(myList.search(7),9)
myList.insert_at_last(700)

myList.delete_first()
myList.delete_last()

myList.delete_item(10)
myList.display()


                


        
