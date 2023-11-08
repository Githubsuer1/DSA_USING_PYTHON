# Queue using list class object

class Queue:
    def __init__(self):
        self.my_queue = []
        self.itemCount = 0

    def is_empty(self):
        return len(self.my_queue) == 0

    def push(self,data):
        self.itemCount+=1
        self.my_queue.append(data)

    def pop(self):
        if not self.is_empty():
            self.itemCount-=1
            return self.my_queue.pop(0)
        else:
            raise IndexError("Oh oh, queue is empty!")

    def peek(self):
        if not self.is_empty():
            return self.my_queue[0]
        else:
            raise IndexError("Oh oh, queue is empty!")
    def size(self):
        if not self.is_empty():
            return self.itemCount
        else:
            raise IndexError("Oh oh, queue is empty!")
    

    def display(self):
        if not self.is_empty():
            print(self.my_queue)
        else:
            raise IndexError("Oh oh, queue is empty!")


qObj= Queue()
qObj.push(10)
qObj.push(20)
qObj.push(30)
qObj.push(40)

qObj.display()

print('deleted item is',qObj.pop())
qObj.display()

print('top of the queue right now =>',qObj.peek())
print('size of the queue is',qObj.size())