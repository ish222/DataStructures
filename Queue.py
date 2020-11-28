"""

Queues are a prominent data structure where each element is stored
in the order it is inserted. It follows the FIFO (First In First Out)
principle, resembling a real life queue. A prominent use of the queue
data structure is in printers where the first request for a print is
the first to be executed.

I manipulated the linked list code to program the queue.

"""


class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = node()
        self.tail = self.head

    def enqueue(self, data):
        new_node = node(data)
        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        first = self.head.next
        self.head.next = first.next
        return first.data

    def peek(self):
        first = self.head.next
        return first.data

    def length(self):
        cur = self.head  # Starts at the head index
        total = 0
        while cur.next is not None:  # Checks if the element is the last element, if it is, .next will be None
            total += 1
            cur = cur.next  # changes the current element to the next one to iterate through all elements
        return total

    def contains(self, data):
        cur = self.head  # Starts at head index
        while cur.next is not None:  # While loop checks if the last index is reached
            if cur.data == data:
                return True
            else:
                cur = cur.next  # Changes current element to the next
        return False

    def display(self):
        """
        prints the elements of the list
        :return: None
        """
        elems = []
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)


# Debug/Test code
# queue = Queue()
#
# queue.enqueue(5)
# queue.enqueue(6)
# queue.enqueue(12)
# queue.enqueue(16)
# queue.display()
# print(queue.contains(2))
# print(queue.peek())
# queue.dequeue()
# queue.display()
# print(queue.peek())
# queue.dequeue()
# queue.display()