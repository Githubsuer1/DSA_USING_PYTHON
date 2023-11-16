# Queue using circular linked list concept. 

class Node:
    def __init__(self,item = None, next = None):
        self.item = item
        self.next = next

class Queue:
    def __init__(self):
        self.front = front
        self.rear = rear
        self.itemCount = 0

    def is_empty(self):
        return self.front == None

    def enqueue(self,data):
        N = Node(data)
        if self.is_empty():
            self.front = N
            self.rear = N
        else:
            self.rear.next = N
            self.rear = N
        self.itemCount+=1


    def dequeue(self):
        if not self.is_empty():
            if self.front == self.rear:
                self.front = None
                self.rear = None
            else:
                self.front = self.front.next
            self.itemCount-=1
        else:
            raise IndexError("Oh oh, queue is empty!")

    def get_front(self):
        if not self.is_empty():
            return self.front.item
        else:
            raise IndexError("Oh oh, queue is empty!")

    def get_rear(self):
        if not self.is_empty(self):
            return self.rear.item
        else:
            raise IndexError("Oh oh, queue is empty!")

    def size(self):
        if not self.is_empty():
            return self.itemCount
        else:
            raise IndexError("Oh oh, queue is empty!")

    def display(self):
        if not self.is_empty():
            temp = self.front
            while temp is not None:
                print(temp.item,end=" ")
                temp = temp.next
        else:
            raise IndexError('oh oh, queue is empty!')



obj = Queue()

obj.enqueue(10)
obj.enqueue(20)
obj.enqueue(30)

obj.dequeue()
obj.dequeue()

print(obj.get_front())
print(obj.get_rear())
obj.display()



