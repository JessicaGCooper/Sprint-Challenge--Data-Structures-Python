from doubly_linked_list import DoublyLinkedList
from doubly_linked_list import ListNode

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    #once capacity is reached the oldest item in the ringbuffer is replaced with the newest item (overwritten)
    #a Queue seems the most logical as dequeue removes the last element, the 
    # the new value can be enqueued, the head dequeued, and then the new value (which will be the tail -> can be moved ot the front using the dll move_to_front method)

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
