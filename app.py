class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
   
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    
    def _insert(self, node, value):
        queue = [node]
        while queue:
            current = queue.pop(0)
            
            if current.left is None:
                current.left = Node(value)
                break
            else:
                queue.append(current.left)

            if current.right is None:
                current.right = Node(value)
                break
            else:
                queue.append(current.right)

    
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.value, end=' ')
            self.inorder(node.right)
    
    
    def preorder(self, node):
        if node:
            print(node.value, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)
    
   
    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value, end=' ')

bt = BinaryTree()


values = [20, 10, 11, 4, 3]
for val in values:
    bt.insert(val)


print("Inorder Traversal:")
bt.inorder(bt.root)  
print()


print("Preorder Traversal:")
bt.preorder(bt.root)  
print()


print("Postorder Traversal:")
bt.postorder(bt.root)  
print()