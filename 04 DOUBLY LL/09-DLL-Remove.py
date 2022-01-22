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

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next

        new_node.previous = before
        before.next = new_node
        new_node.next = after 
        after.previous = new_node

        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.popFirst()
        if index == self.length-1:
            return self.pop()
        
        # approach(1) is before and after as we did 
        # approach(2) is below

        temp = self.get(index)
        temp.next.previous = temp.previous
        temp.previous.next = temp.next
        temp.next = temp.previous = None

        self.length -= 1
        return temp

my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)

my_doubly_linked_list.print_list()

print('\n',my_doubly_linked_list.remove(1),'\n')

my_doubly_linked_list.print_list()

