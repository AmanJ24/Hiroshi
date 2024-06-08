class Node: 
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return f"{self.data}"


class Stack:
    def __init__(self):
        self.pointer = None
        self.size = 0

    def __str__(self):
        if self.pointer is None:
            return "The stack is empty"
        
        to_print = ""
        itr = self.pointer
        while itr is not None:
            to_print += str(itr.data) + "->"
            itr = itr.next
        return to_print[:-2]

    def push(self, value):
        '''Pushing a new item to the stack'''
        if not isinstance(value, Node):
            value = Node(value)

        self.pointer = Node(value, self.pointer)
        self.size += 1

    def pop(self):
        '''Removing the item from the top of the stack'''
        if self.pointer is None:
            return "No item to pop."

        self.pointer = self.pointer.next
        self.size -= 1

    def peek(self):
        '''Retrieving the top item of the stack'''
        if self.pointer is None:
            return "No item to peek."
        
        return self.pointer.data

    def is_empty(self):
        '''Checking if the stack is empty or not'''
        return self.size == 0

    def get_size(self):
        return self.size
    '''Retrieving the total size of the Stack'''



my_list = Stack()

val1 = Node(1)
val2 = Node(2)
val3 = Node(3)
val4 = Node(4)
val5 = Node(5)

my_list.push(val1)
my_list.push(val2)
my_list.push(val3)
my_list.push(val4)
my_list.push(val5)

print(my_list)