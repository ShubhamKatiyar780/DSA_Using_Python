class Node:
    def __init__(self, item, left = None, right = None):
        self.item = item
        self.left = left
        self.right = right
class BST:
    def __init__(self):
        self.root = None
    def insertion(self, data):
        self.root = self.insert_recursively(self.root, data)
    def insert_recursively(self, root, data):
        if root is None:
            return Node(data)
        if data < root.item:
            root.left = self.insert_recursively(root.left, data)
        elif data > root.item:
            root.right = self.insert_recursively(root.right, data)
        else:
            print(f"Duplicate value {data} is not allowed in BST.")
        return root
    def search(self, data):
        return self.search_recursively(self.root, data)
    def search_recursively(self, root, data):
        if root is None or root.item == data:
            return root
        if data < root.item:
            return self.search_recursively(root.left, data)
        else:
            return self.search_recursively(root.right, data)
    def in_order_traversal(self):
        print("-------------In-Order Traversing--------------")
        self.in_order_recursively(self.root)
        print()
    def in_order_recursively(self, root):
        if root is not None:
            self.in_order_recursively(root.left)
            print(root.item, end=' ')
            self.in_order_recursively(root.right)
    def pre_order_traversal(self):
        print("-------------Pre-Order Traversing--------------")
        self.pre_order_recursively(self.root)
        print()
    def pre_order_recursively(self, root):
        if root is not None:
            print(root.item, end=' ')
            self.pre_order_recursively(root.left)
            self.pre_order_recursively(root.right)
    def post_order_traversal(self):
        print("-------------Post-Order Traversing--------------")
        self.post_order_recursively(self.root)
        print()
    def post_order_recursively(self, root):
        if root is not None:
            self.post_order_recursively(root.left)
            self.post_order_recursively(root.right)
            print(root.item, end=' ')
    def minimum_value(self, root = None):
        if root is None:
            root = self.root
        current = root
        while current.left is not None:
            current = current.left
        return current.item
    def maximum_value(self, root = None):
        if root is None:
            root = self.root
        current = root
        while current.right is not None:
            current = current.right
        return current.item
    def delete(self, data):
        self.root = self.delete_recursively(self.root, data)
    def delete_recursively(self, root, data):
        if root is None:
            return root
        if data < root.item:
            root.left = self.delete_recursively(root.left, data)
        elif data > root.item:
            root.right = self.delete_recursively(root.right, data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.item = self.minimum_value(root.right)
            root.right = self.delete_recursively(root.right, root.item)
        return root
obj = BST()
obj.insertion(50)
obj.insertion(30)
obj.insertion(70)
obj.insertion(20)
obj.insertion(80)
obj.insertion(40)
obj.in_order_traversal()
obj.pre_order_traversal()
obj.post_order_traversal()
print("Minimum value in the BST:", obj.minimum_value(obj.root))
print("Maximum value in the BST:", obj.maximum_value(obj.root))
obj.delete(30)
obj.in_order_traversal()
print("Minimum value in the BST:", obj.minimum_value())
print("Maximum value in the BST:", obj.maximum_value(obj.root))