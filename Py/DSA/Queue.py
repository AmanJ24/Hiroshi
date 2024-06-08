class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Queue:
    def __init__(self):
        self.head = None
        self.rear = None
        self.size = 0

    '''Inserting the value from the rear'''
    def enqueue(self, value):
        if self.rear == None:
            self.head = Node(value)
            self.rear = self.head
        else:            
            self.rear.next = Node(value)
            self.rear = self.rear.next

    '''Removing the value from the top'''
    def dequeue(self):
        if self.head == None:
            return "No item to dequeue"
        return_data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return return_data

    '''Retrieving the value at the top'''
    def peek(self):
        if self.head == None:
            return None
        else:
            return self.head.data

    '''Retrieving the value at the end'''
    def rear(self):
        return self.rear

    '''Checking if the queue is empty or not'''
    def isEmpty(self):
        return "Empty" if self.size == 0 else "Empty"

    '''Checking the number of items in queue'''
    def size(self):
        return self.size


my_list = Queue()

val1 = Node(1)
val2 = Node(2)
val3 = Node(3)
val4 = Node(4)
val5 = Node(5)

my_list.enqueue(val1)
my_list.enqueue(val2)
my_list.enqueue(val3)
my_list.enqueue(val4)
my_list.enqueue(val5)

print(my_list)

