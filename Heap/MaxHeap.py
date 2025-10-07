class MaxHeap:
    def __init__(self):
        # Initialize an empty list to store heap elements
        self.heap = []

    def insert(self, value):
        # Append the new value to the heap
        self.heap.append(value)
        # Move the newly added value to its correct position (heapify up)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        # Find the parent index
        parent = (index - 1) // 2
        # If the current node is greater than its parent, swap them
        if index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            # Recursively move up the tree to maintain heap property
            self._heapify_up(parent)

    def delete(self):
        # If the heap is empty, return None
        if len(self.heap) == 0:
            return None
        # If the heap has only one element, remove and return it
        if len(self.heap) == 1:
            return self.heap.pop()
        # Store the maximum value (root of the heap)
        max_value = self.heap[0]
        # Move the last element to the root and remove the last element
        self.heap[0] = self.heap.pop()
        # Restore the heap property by moving the root down
        self._heapify_down(0)
        return max_value

    def _heapify_down(self, index):
        # Find the left and right child indices
        left_child = (2 * index) + 1
        right_child = (2 * index) + 2
        largest = index  # Assume the current node is the largest

        # Compare with the left child
        if left_child < len(self.heap) and self.heap[left_child] > self.heap[largest]:
            largest = left_child
        # Compare with the right child
        if right_child < len(self.heap) and self.heap[right_child] > self.heap[largest]:
            largest = right_child
        # If the largest is not the current node, swap and continue heapifying down
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

    def print_heap(self):
        # Print the heap as a list
        print(self.heap)

# Create a max heap instance
heap = MaxHeap()

# Insert elements into the max heap
heap.insert(10)
heap.insert(20)
heap.insert(5)
heap.insert(30)
heap.insert(15)
heap.insert(150)

print("Max Heap before deletion:")
heap.print_heap()  # Print the heap before deletion

# Delete the maximum element (root of the heap)
print("\nDeleted element:", heap.delete())

print("\nMax Heap after deletion:")
heap.print_heap()  # Print the heap after deletion
