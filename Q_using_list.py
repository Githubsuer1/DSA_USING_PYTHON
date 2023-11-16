# Queue using list class object

class Queue:
    def __init__(self):
        self.my_queue = []
        self.itemCount = 0

    def is_empty(self):
        return len(self.my_queue) == 0

    def enqueue(self,data):
        self.my_queue.append(data)
        self.itemCount+=1

    def dequeue(self):
        if not self.is_empty():
            return self.my_queue.pop(0)
        else:
            raise IndexError("Oh oh, queue is empty!")
        self.itemCount-=1

    def get_front(self):
        if not self.is_empty():
            return self.my_queue[0]
        else:
            raise IndexError("Oh oh, queue is empty!")

    def get_rear(self):
        if not self.is_empty():
            return self.my_queue[-1]
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
try:
    print(qObj.front())
except IndexError as e:
    print(e.args[0])

qObj.enqueue(10)
qObj.enqueue(20)
qObj.enqueue(30)
qObj.enqueue(40)

print(qObj.my_queue)

qObj.dequeue()

print(qObj.my_queue)
