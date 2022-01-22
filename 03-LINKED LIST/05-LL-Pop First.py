
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
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
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self):
        if (self.length == 0):
            return None
        temp = self.head
        pre = self.head
        while (temp.next is not None):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value 
        #temp returns Node location but temp.value reurns value

    def prepend(self, value) :
        new_node = Node(value)
        if(self.head is None):
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def popFirst(self):
        if(self.length == 0): #with no item
            return None
        temp = self.head #more than one
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if(self.length == 0): #with one item
            self.tail = None
        return temp


my_linked_list = LinkedList(2)
my_linked_list.append(1)

print(my_linked_list.popFirst())
print(my_linked_list.popFirst())
print(my_linked_list.popFirst())