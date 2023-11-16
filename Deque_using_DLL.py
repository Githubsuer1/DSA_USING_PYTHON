class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev = prev
        self.item = item 
        self.next = next

class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.itemCount = 0

    def is_empty(self):
        return self.front == None

    def insert_front(self,data):
        N = Node(None,data,None)
        if self.is_empty():
            self.front = N
            self.rear = N
        else:
            self.front.prev = N
            self.front.prev.next = self.front
            self.front = N 
        self.itemCount+=1

    def insert_rear(self,data):
        N = Node(None,data,None)
        if self.is_empty():
            self.front = N
            self.rear = N
        else:
            self.rear.next = N
            self.rear.next.prev = self.rear
            self.rear = N 
        self.itemCount+=1

    def delete_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty!")
        elif self.front == self.rear:
            self.front = None 
            self.rear = None
        else:
            self.front.next.prev = None
            self.front = self.front.next 
        self.itemCount-=1

    def delete_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty!")
        elif self.rear == self.front:
            self.rear = None
            self.front = None
        else:
            self.rear.prev.next = None 
            self.rear = self.rear.prev 
        self.itemCount-=1

    def get_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty!")
        else:
            return self.front.item

    def get_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty!")
        else:
            return self.rear.item

    def size(self):
        if self.is_empty():
            raise IndexError('Deque is empty!')
        else:
            return self.itemCount

    def display(self):
        if self.is_empty():
            raise IndexError("Deque is empty!")
        else:
            temp = self.front
            while temp is not None:
                print(temp.item,end=" ")
                temp = temp.next 

obj = Deque()

obj.insert_front(20)
obj.insert_front(15)
obj.insert_front(10)
obj.insert_front(5)

# obj.delete_rear()
# obj.delete_rear()
# obj.delete_rear()
# obj.delete_front()

print('before deletion')
print('front item is',obj.get_front())
print('rear item is',obj.get_rear())
obj.display()

print('after deletion')
obj.delete_front()
obj.delete_rear()

print('front item is',obj.get_front())
print('rear item is',obj.get_rear())

obj.delete_front()

print('front item is',obj.get_front())
print('rear item is',obj.get_rear())
obj.display()