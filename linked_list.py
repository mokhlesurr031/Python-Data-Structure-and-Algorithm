class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        # print(self.head)

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
            # print(itr.data)
            llstr+= str(itr.data)+ '-->'
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
            count+=1
            itr= itr.next
        print(count)




ll = LinkedList()

# ll.insert_at_beginning(5)
# ll.insert_at_beginning(89)
# ll.insert_at_beginning(25)


# ll.insert_at_end(99)
# ll.insert_at_end(939)
# ll.insert_at_end(9349)

ll.insert_values([1,2,3,4,5])

ll.get_length()

ll.print()



