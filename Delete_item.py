def delete_item(self, data):
    temp = self.start  # Start traversing from the head of the list
    while temp is not None:  # Loop through the list until we reach the end
        if temp.item == data:  # If the current node contains the data to be deleted
            if temp.prev is not None:  # If the current node is not the first node
                temp.prev.next = temp.next  # Update the previous node's `next` to skip the current node
            if temp.next is not None:  # If the current node is not the last node
                temp.next.prev = temp.prev  # Update the next node's `prev` to skip the current node
            if temp == self.start:  # If the current node is the head of the list
                self.start = temp.next  # Update the head to the next node
            to_delete = temp  # Save the current node for deletion
            temp = temp.next  # Move to the next node before deleting the current one
            del to_delete  # Delete the current node from memory
        else:  # If the current node does not contain the data to be deleted
            temp = temp.next  # Move to the next node in the list