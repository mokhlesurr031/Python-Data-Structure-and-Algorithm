class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def show_data(self):
        node = self.head
        if node is None:
            print("LL is empty")
        while node is not None:
            print(node.data)
            node = node.next

    def add_data(self, new):
        new_node = Node(new)
        new_node.next = self.head
        self.head = new_node



ll = LinkedList()
#
# elem = Node(1)
# # print(elem.data)
# # print(elem.next)
#
# ll.head = elem
# ll.show_data()
#
#
# elem2 = Node(2)
# ll.head.next = elem2
#
# ll.show_data()

ll.add_data(1)
ll.add_data(2)
ll.add_data(3)
ll.show_data()

