class Node: 
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return f"{self.data}"


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append_val(self, x):
        '''Add to the end of the list'''
        if not isinstance(x, Node):
            x = Node(x)
        if self.head == None:
            self.head = x
        else:
            self.tail.next = x
        self.tail = x

    def __str__(self):
        '''The result of printing the LinkedList'''
        to_print = ""
        curr = self.head
        while curr is not None:
            to_print += str(curr.data) + "->"
            curr = curr.next
        return "[" + to_print[:-2] + "]" if to_print else "[]"   

    def add_to_start(self, x):
        '''Add x to the start of the Linked List'''
        if not isinstance(x, Node):
            x = Node(x)
        self.head = Node(x, self.head)

    def reverse_list_recur(self, current, previous):
        '''Reverse the sequence of node pointers in the linked list'''
        if self.head == None:
            return 
        elif current.next == None:
            self.tail = self.head
            current.next = previous
            self.head = current
        else:
            next = current.next
            current.next = previous
            self.reverse_list_recur(next, current)

    def search_val(self, value):
        itr = self.head
        while itr.next:
            if value == itr.data:
                return f"{value} is in the Linked List."
            else:
                itr = itr.next
        return f"{value} does not exist in the Linked List."

    def remove_val_by_index(self, index):
        if index < 0 or index >= self.length():
            raise Exception("Index out of range")
        
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr.next:
            if index-1 == count:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def length(self):
        count = 0
        if self.head is None:
            return 0
        itr = self.head
        while itr.next:
            count += 1
            itr = itr.next
        return count+1



node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

my_list = LinkedList()


my_list.append_val(node1)
my_list.append_val(node2)
my_list.append_val(node3)
my_list.append_val(node4)
my_list.append_val(node5)
# my_list.add_to_start(7)


my_list.add_to_start(20)
print(my_list)
# print(my_list.search_val(4))
# print(my_list)
# my_list.reverse_list_recur(my_list.head, None)
