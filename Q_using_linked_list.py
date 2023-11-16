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
            if self.last.next == self.last:
                self.last = None
            else:
                self.last.next = self.last.next.next
            self.itemCount-=1
        else:
            raise IndexError("Oh oh, queue is empty!")

    def peek(self):
        if not self.is_empty():
            return self.last.next.item
        else:
            raise IndexError("Oh oh, queue is empty!")

    def size(self):
        if not self.is_empty():
            return self.itemCount
        else:
            raise IndexError("Oh oh, queue is empty!")

    def display(self):
        if not self.is_empty():
            temp = self.last.next
            while(temp != self.last):
                print(temp.item,end=" ")
                temp = temp.next 
            print(temp.item)
        else:
            raise IndexError("Oh oh, queue is empty!")

myq = Queue()
myq.push(10)
myq.push(20)
myq.push(30)
myq.push(40)

myq.pop()
myq.pop()
myq.pop()
myq.pop()

myq.display()

# myq.display()
# print(myq.peek())

# myq.pop()
# myq.display()
# print(myq.peek())


# myq.push(100)
# myq.display()
# print(myq.peek())


# myq.pop()
# myq.display()
# print(myq.peek())
# print(myq.size())

# you can try above function calls to check the working of Queue.


