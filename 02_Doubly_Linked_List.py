#--------------Node class to create Node-----------------#
class Node:
    def __init__(self, prev = None, item = None, next = None):
        self.prev = prev 
        self.item = item
        self.next = next

#-------------- DLL class to implement doubly linked list-------------#
class DLL:
    def __init__(self, start = None):
        self.start = start

#-------------- is_empty() method to check whether list is empty or not -------#
    def is_empty(self):
        return self.start == None

#-------------- Insertion in doubly linked list------------------#

    def insert_at_start(self,data):
        N = Node(None,data,self.start)
        if not self.is_empty():
            self.start.prev = N
        self.start = N

    def insert_at_last(self,data):
        N = Node(None,data,None)
        if self.start == None:
            self.start = N
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            N.prev = temp
            N.prev.next = N

    def insert_after(self,temp,data):
        if not self.is_empty():
            if temp is not None:
                N = Node(temp,data,temp.next)
                if temp.next is not None:
                    temp.next.prev = N
                    temp.next = N
                else:
                    temp.next = N 

#-------------- Display function -----------------#
    def display(self):
        if not self.is_empty():
            temp = self.start
            while temp is not None:
                print(temp.item, end=" ")
                temp = temp.next
        

#--------------- deletion in doubly linked list -------------------#
    def delete_start(self):
        if self.start is not None:
            if self.start.next == None:
                self.start = None 
            else:
                self.start.next.prev = None
                self.start = self.start.next

    def delete_last(self):
        if self.start is not None:
            if self.start.next == None:
                self.start = None 
            else:
                temp = self.start 
                while temp.next.next is not None:
                    temp = temp.next
                temp.next.prev = None
                temp.next = None
                
    def delete_item(self,data):
        if self.start == None:
            pass
        else:
            temp = self.start
            while temp is not None:
                if temp.item == data:
                    if temp.next is not None:
                        temp.next.prev = temp.prev
                    if temp.prev is not None:
                        temp.prev.next = temp.next
                    else:
                        self.start = temp.next
                    break
                temp = temp.next



#------------------ search function -------------------#
    def search(self,data):
        if not self.is_empty():
            temp = self.start
            while temp is not None:
                if temp.item == data:
                    return temp
                temp = temp.next
            return None

myList = DLL()

myList.insert_at_start(9)
myList.insert_at_start(8)
myList.insert_at_start(7)
myList.insert_at_start(6)
myList.insert_at_start(5)
myList.delete_item(7)
myList.delete_item(8)
myList.delete_item(9)

myList.display()
