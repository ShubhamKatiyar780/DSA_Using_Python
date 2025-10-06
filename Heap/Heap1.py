class Heap:
    def __init__(self):
        # Initialize an empty list to store heap elements
        self.heap = []
    
    def insert(self, data):
        """ Inserts a new element into the heap """
        self.heap.append(data)  # Add the new element at the end of the heap
        self.heapify_up(len(self.heap) - 1)  # Restore heap property by moving the element up if necessary

    def heapify_up(self, index):
        """ Ensures the heap property is maintained after insertion """
        parent = (index - 1) // 2  # Find the parent index
        while index > 0 and self.heap[index] > self.heap[parent]:  
            # Swap if the current node is greater than its parent (max heap property)
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            index = parent  # Move up the tree
            parent = (index - 1) // 2  # Update parent index

    def delete(self):
        """ Removes and returns the maximum element (root) from the heap """
        if len(self.heap) == 0:
            return None  # Return None if the heap is empty
        if len(self.heap) == 1:
            return self.heap.pop()  # If only one element, remove and return it
        
        max_value = self.heap[0]  # The root (maximum element)
        self.heap[0] = self.heap.pop()  # Replace root with the last element in the heap
        self.heapify_down(0)  # Restore heap property by moving the element down if necessary
        return max_value  # Return the deleted max element

    def heapify_down(self, index):
        """ Ensures the heap property is maintained after deletion """
        while True:
            left_child = 2 * index + 1  # Calculate left child index
            right_child = 2 * index + 2  # Calculate right child index
            largest = index  # Assume the largest is the current node
            
            if left_child < len(self.heap) and self.heap[left_child] > self.heap[largest]:
                largest = left_child  # Update largest if left child is greater
            if right_child < len(self.heap) and self.heap[right_child] > self.heap[largest]:
                largest = right_child  # Update largest if right child is greater
            
            if index == largest:
                break  # Stop if the heap property is satisfied
            
            # Swap the current node with the largest child
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            index = largest  # Move index to the new position

    def __str__(self):
        """ Returns a string representation of the heap """
        return str(self.heap)

# Create a max heap instance
heap = Heap()

# Insert elements into the max heap
heap.insert(10)  # Insert 10
heap.insert(20)  # Insert 20
heap.insert(5)   # Insert 5
heap.insert(30)  # Insert 30
heap.insert(15)  # Insert 15
heap.insert(150) # Insert 150

# Print the heap before deletion
print("\nMax Heap before deletion: ", heap)

# Delete the maximum element (root of the heap)
print("\nDeleted element: ", heap.delete())

# Print the heap after deletion
print("\nMax Heap after deletion: ", heap)
