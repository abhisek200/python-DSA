class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None :
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0 :
            return None
        temp = self.tail
        if(self.length == 1):
            self.head = None
            self.tail = None
        else:
            self.tail = temp.previous
            self.tail.next = None
            temp.previous = None
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0 :
            self.head = new_node
            self.tail = new_node
        else:
            self.head.previous = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def popFirst(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = temp.next
            self.head.previous = None
            temp.next = None
        self.length -= 1
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        #optimise code in comparable to SLL
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1,index,-1):
                temp = temp.previous
        return temp

    def set_values(self, index, value):
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        return False

my_doubly_linked_list = DoublyLinkedList(11)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(23)
my_doubly_linked_list.append(7)

my_doubly_linked_list.print_list()

print('\n',my_doubly_linked_list.set_values(1,4),'\n')

my_doubly_linked_list.print_list()

