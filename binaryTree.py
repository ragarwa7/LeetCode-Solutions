class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_node = None
        self.right_node = None
        
    def insert_right(self,value):
        if self.right_node==None:
            self.right_node = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.right_node = self.right_node
            self.right_node = new_node
            
    def insert_left(self,value):
        if self.left_node==None:
            self.left_node = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.left_node = self.left_node
            self.left_node = new_node

tree = BinaryTree(4)
tree.insert_right(7)
tree.insert_right(6)
tree.insert_right(8)
tree.insert_left(3)
tree.insert_left(2)
tree.insert_left(1)

print(tree.value)
print(tree.left_node.value)
print(tree.right_node)
