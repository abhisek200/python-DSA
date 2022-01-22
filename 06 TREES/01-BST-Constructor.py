class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
class BinarySearchTree():
    #approach(2): 
    def __init__(self):
        self.root = None

my_tree = BinarySearchTree()

print(my_tree.root)
