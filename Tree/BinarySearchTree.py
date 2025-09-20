class Node:
    """
    Represents a node in the Binary Search Tree (BST).
    Each node contains an item (value) and references to its left and right children.
    """
    def __init__(self, item, left=None, right=None):
        self.item = item  # The value stored in the node
        self.left = left  # Reference to the left child node
        self.right = right  # Reference to the right child node


class BST:
    """
    Represents a Binary Search Tree (BST).
    Supports insertion, deletion, searching, and traversal operations.
    """
    def __init__(self):
        self.root = None  # The root node of the BST

    def insert(self, data):
        """
        Inserts a new value into the BST.
        """
        self.root = self._insert_recursively(self.root, data)

    def _insert_recursively(self, root, data):
        """
        Helper method to insert a value recursively into the BST.
        """
        if root is None:
            return Node(data)  # Create a new node if the current node is None
        if data < root.item:
            root.left = self._insert_recursively(root.left, data)  # Insert into the left subtree
        elif data > root.item:
            root.right = self._insert_recursively(root.right, data)  # Insert into the right subtree
        else:
            print(f"Duplicate value {data} is not allowed in BST.")  # Handle duplicate values
        return root

    def search(self, data):
        """
        Searches for a value in the BST.
        Returns the node containing the value if found, otherwise returns None.
        """
        return self._search_recursively(self.root, data)

    def _search_recursively(self, root, data):
        """
        Helper method to search for a value recursively in the BST.
        """
        if root is None or root.item == data:
            return root  # Return the node if found or None if not found
        if data < root.item:
            return self._search_recursively(root.left, data)  # Search in the left subtree
        else:
            return self._search_recursively(root.right, data)  # Search in the right subtree

    def in_order_traversal(self):
        """
        Performs an in-order traversal of the BST and prints the values.
        In-order traversal visits nodes in the order: left -> root -> right.
        """
        print("------------- In-Order Traversal --------------")
        result = []
        self._in_order_recursively(self.root, result)
        return result

    def _in_order_recursively(self, root, result):
        """
        Helper method to perform in-order traversal recursively.
        """
        if root is not None:
            self._in_order_recursively(root.left, result)  # Traverse the left subtree
            # print(root.item, end=' ')  # Print the current node's value
            result.append(root.item)   # Append the current node's value to the list
            self._in_order_recursively(root.right, result)  # Traverse the right subtree

    def pre_order_traversal(self):
        """
        Performs a pre-order traversal of the BST and prints the values.
        Pre-order traversal visits nodes in the order: root -> left -> right.
        """
        print("------------- Pre-Order Traversal --------------")
        self._pre_order_recursively(self.root)
        print()

    def _pre_order_recursively(self, root):
        """
        Helper method to perform pre-order traversal recursively.
        """
        if root is not None:
            print(root.item, end=' ')  # Print the current node's value
            self._pre_order_recursively(root.left)  # Traverse the left subtree
            self._pre_order_recursively(root.right)  # Traverse the right subtree

    def post_order_traversal(self):
        """
        Performs a post-order traversal of the BST and prints the values.
        Post-order traversal visits nodes in the order: left -> right -> root.
        """
        print("------------- Post-Order Traversal --------------")
        self._post_order_recursively(self.root)
        print()

    def _post_order_recursively(self, root):
        """
        Helper method to perform post-order traversal recursively.
        """
        if root is not None:
            self._post_order_recursively(root.left)  # Traverse the left subtree
            self._post_order_recursively(root.right)  # Traverse the right subtree
            print(root.item, end=' ')  # Print the current node's value

    def minimum_value(self, root=None):
        """
        Finds and returns the minimum value in the BST.
        """
        if root is None:
            root = self.root
        current = root
        while current.left is not None:
            current = current.left  # Traverse to the leftmost node
        return current.item

    def maximum_value(self, root=None):
        """
        Finds and returns the maximum value in the BST.
        """
        if root is None:
            root = self.root
        current = root
        while current.right is not None:
            current = current.right  # Traverse to the rightmost node
        return current.item

    def delete(self, data):
        """
        Deletes a value from the BST.
        """
        self.root = self._delete_recursively(self.root, data)

    def _delete_recursively(self, root, data):
        """
        Helper method to delete a value recursively from the BST.
        """
        if root is None:
            return root  # Return None if the node is not found
        if data < root.item:
            root.left = self._delete_recursively(root.left, data)  # Delete from the left subtree
        elif data > root.item:
            root.right = self._delete_recursively(root.right, data)  # Delete from the right subtree
        else:
            # Node with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            # Node with two children: Get the in-order successor (smallest in the right subtree)
            root.item = self.minimum_value(root.right)
            # Delete the in-order successor
            root.right = self._delete_recursively(root.right, root.item)
        return root
    
    def size(self):
        """
        Returns the number of nodes in the BST.
        """
        return len(self.in_order_traversal())
        
        
if __name__ == "__main__":
    bst = BST()
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(80)
    bst.insert(40)
    print(bst.in_order_traversal())  # Output: 20 30 40 50 70 80
    bst.pre_order_traversal()  # Output: 50 30 20 40 70 80
    bst.post_order_traversal()  # Output: 20 40 30 80 70 50

    print("Minimum value in the BST:", bst.minimum_value())  # Output: 20
    print("Maximum value in the BST:", bst.maximum_value())  # Output: 80

    bst.delete(30)
    print(bst.in_order_traversal())  # Output: 20 40 50 70 80
    print("Size of BST is:", bst.size())    # Output: Size of the BST is: 5