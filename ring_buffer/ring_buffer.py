from doubly_linked_list import DoublyLinkedList
from doubly_linked_list import ListNode

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    #once capacity is reached the oldest item in the ringbuffer is replaced with the newest item (overwritten)
    #this means when the linked list reachs capacity
    # the first new item will replace the head
    # the second new item will replace the head.next
    # the 3rd new item will replace head.next.next

   

    def append(self, item):
        print(len(self.storage))
        # new_node = ListNode(item)
        # self.current = self.storage.head
        if len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)
        elif len(self.storage) >= self.capacity:
            # if self.current == self.storage.head:

            self.storage.remove_from_head()
            self.storage.add_to_head(item)
            self.current = self.storage.head.next
            self.current.next = self.current
            # else:
            #     new_node.prev = self.current
            #     self.current.next = new_node
            #     self.current = self.current.next
            #     self.storage.delete(self.current.prev)



         

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        self.current = self.storage.head
        print(self.storage.head.value)
        while self.current != None:
            list_buffer_contents.append(self.current.value)
            self.current = self.current.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass


buffer = RingBuffer(6)
buffer.append(9)
buffer.append(13)
buffer.append(34)
buffer.append(17)
buffer.append(4)
buffer.append(19)
buffer.append(21)
buffer.append(313)
print(buffer.get())
