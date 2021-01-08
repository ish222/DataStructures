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


# class Stack:
#     def __init__(self):
#         self.data = []  # Initialises an empty list
#
#     def push(self, data):
#         """
#         Push method is used to add an item to the top of the stack
#         :param data: the data to insert at the top of the stack
#         :return: None
#         """
#         self.data.insert(0, data)  # hence the data is added at the 0th element
#
#     def pop(self):
#         """
#         Pop removes and returns the item at the top of the stack
#         :return: item at the top of the stack
#         """
#         data = self.data[0]
#         self.data.remove(data)  # removes the item at the top of the stack
#         return data
#
#     def peek(self):
#         """
#         Peek is used to see what is at the top of the stack without deletion
#         :return: the item at the top of the stack
#         """
#         return self.data[0]
#
#     def contains(self, data):
#         """
#         Contains checks if the data specified is in any of the elements of the stack
#         :param data: the data to be searched for
#         :return: boolean depending on if the data is found or not
#         """
#         for _ in self.data:
#             if _ == data:
#                 return True
#         return False
#
#     def display(self):
#         """
#         Prints the data of the stack
#         :return: None
#         """
#         print(self.data)


# This is the code I tried to use to create the Stack class using the linked list code but was unsuccessful.

class Stack:

    class Node:
        def __init__(self, data, next):
            self.data = data
            self.next = next

    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, data):
        """
        Pushes a new element to the top of the stack
        :param data: the new element
        :return: None
        """
        self.head = self.Node(data, self.head)
        self.size += 1

    def isEmpty(self):
        """
        Checks if the stack is empty
        """
        return self.size == 0

    def pop(self):
        """
        Returns and removes the top element of the stack
        """
        if self.isEmpty():
            raise Exception("The stack is empty, no elements to pop.")
        result = self.head.data
        self.head = self.head.next
        self.size -= 1
        return result

    def peek(self):
        """
        Returns the top element of the stack without removal
        """
        if self.isEmpty():
            raise Exception("The stack is empty, no elements to pop.")
        return self.head.data

    def display(self):
        """
        Returns a list containing all the elements of the stack
        """
        elems = []
        cur_node = self.head
        while cur_node.next is not None:
            elems.append(cur_node.data)
            cur_node = cur_node.next
        elems.append(cur_node.data)
        return elems

    def contains(self, data):
        """
        Checks if the stack contains a specified element
        :param data: the element to search for
        :return: a boolean
        """
        cur = self.head
        while cur.next is not None:
            if cur.data == data:
                return True
            else:
                cur = cur.next
        if cur.data == data:
            return True
        return False
    
    def length(self):
        """
        returns the size of the stack
        """
        return self.size


stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)
print(stack.pop())
print(stack.peek())
print(stack.display())
print(stack.contains(10))
print(stack.length())
