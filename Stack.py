"""

A stack is very similar to the queue data structure where again each element is
stored in the order it is inserted. However, contrasting the queue, the stack
follows the LIFO (Last In First Out) principle where the last element inserted
would be the first removed, resembling a real life stack of items. One prominent
use is the undo function in many programs.

I tried to manipulate the linked list code to create a stack class but was
unsuccessful, so I used the inbuilt Python list object instead. Due to this,
the efficiency benefits of a stack may not be present, but its function is
correct.

"""


class Stack:
    def __init__(self):
        self.data = []  # Initialises an empty list

    def push(self, data):
        """
        Push method is used to add an item to the top of the stack
        :param data: the data to insert at the top of the stack
        :return: None
        """
        self.data.insert(0, data)  # hence the data is added at the 0th element

    def pop(self):
        """
        Pop removes and returns the item at the top of the stack
        :return: item at the top of the stack
        """
        data = self.data[0]
        self.data.remove(data)  # removes the item at the top of the stack
        return data

    def peek(self):
        """
        Peek is used to see what is at the top of the stack without deletion
        :return: the item at the top of the stack
        """
        return self.data[0]

    def contains(self, data):
        """
        Contains checks if the data specified is in any of the elements of the stack
        :param data: the data to be searched for
        :return: boolean depending on if the data is found or not
        """
        for _ in self.data:
            if _ == data:
                return True
        return False

    def display(self):
        """
        Prints the data of the stack
        :return: None
        """
        print(self.data)


# This is the code I tried to use to create the Stack class using the linked list code but was unsuccessful.
# class node:
#     def __init__(self, data=None):
#         self.data = data
#         self.next = None
#         self.last = None
#
#
# class Stack:
#     def __init__(self):
#         self.head = node()
#         self.tail = self.head
#
#     def push(self, data):
#         new_node = node(data)
#         self.tail.last = self.head
#         self.tail.next = new_node
#         self.tail = new_node
#
#     def pop(self):
#         first = self.tail
#         self.tail = self.tail.last
#         return first.data
#
#     def peek(self):
#         first = self.head
#         return first.data
#
#     def contains(self, data):
#         pass
#
#     def display(self):
#         """
#                 prints the elements of the list
#                 :return: None
#                 """
#         elems = []
#         cur_node = self.head
#         while cur_node.next is not None:
#             cur_node = cur_node.next
#             elems.append(cur_node.data)
#         print(elems)


stack = Stack()

stack.push(5)
stack.push(6)
stack.push(12)
stack.push(16)
stack.display()
print(stack.contains(5))
stack.pop()
stack.display()