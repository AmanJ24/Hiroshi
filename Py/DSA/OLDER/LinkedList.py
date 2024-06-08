class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return 
        
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception('Index out of range')
        
        if index == 0:
            self.head = self.head.next
            return 
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1 

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception('Index out of range')

        if index == 0:
            self.insert_at_beginning(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

#--> PRACTICE BY ADDING NEW FUNCTIONS IN THE CLASS

    def insert_after_value(self, value, data):
        if self.head is None:
            return
        
        if self.head.data == value:
            self.head.next = Node(value, self.head.next)
            return 
        
        itr = self.head
        while itr:
            if itr.data == value:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next


    def remove_by_value(self, value):
        if self.head is None:
            return 

        if self.head.data == value:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == value:
                itr.next = itr.next.next
                break
            itr = itr.next


if __name__ == '__main__':
    ll = LinkedList()
    ## --> INSERTING AT THE BEGINNING OF THE LIST
    # ll.insert_at_beginning(5)
    # ll.insert_at_beginning(8)

    ## --> INSERTING AT THE END OF THE LIST
    # ll.insert_at_end(12)
    # ll.print()

    ## --> INSERTING VALUES TO A COMPLETELY NEW LIST 
    ll.insert_values(['Banana', 'apple', 'mango', 'orange'])
    ll.print()

    ## --> ACCESSING THE LENGTH OF THE LIST
    # print("length:", ll.get_length())

    ## --> REMOVING A VALUE AT THE GIVEN INDEX
    # ll.remove_at(2)
    # ll.print()

    ## --> INSERTING A VALUE AT THE GIVEN INDEX
    # ll.insert_at(2, 'grape')
    # ll.print()

    # # --> INSERTING VALUES AFTER THE GIVEN VALUE
    # ll.insert_after_value('apple', 'jackfruit')
    # ll.print()

    # --> REMOVING DATA OF THE GIVEN VALUE
    ll.remove_by_value('apple')
    ll.remove_by_value('jackfruit')
    ll.print()