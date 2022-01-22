class Node :
    def __init__(self,value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

my_linked_list = LinkedList(4)
#Node of value 4 is created.

print(my_linked_list.head.value)