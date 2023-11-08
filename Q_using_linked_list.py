# Queue using circular linked list concept. 

class Node:
    def __init__(self,item = None, next = None):
        self.item = item
        self.next = next

class Queue:
    def __init__(self,last=None):
        self.last = last
        self.itemCount = 0

    def is_empty(self):
        return self.last == None

    def push(self,data):
        N = Node(data)
        if not self.is_empty():
            N.next = self.last.next
            self.last.next = N
            self.last = N
        else:
            N.next = N
            self.last = N
        self.itemCount+=1


    def pop(self):
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


