"""

Linked lists work by having a list of data elements where each data element has a
pointer to the next element. This means that data can only be accessed by starting at
the back of the list and continuing through the elements until the specified element
is reached. This means that linked lists are not as efficient as Python lists in terms of
access, with a time complexity equation of O(n).

However, the major benefit of linked lists is that only one instruction is required to add
or remove an element, O(1), unlike for random access data structures like arrays, where the 
whole array has to be reorganised in order in memory, O(n).

In this linked lists implementation, the relationship between subsequent elements is only
one way, from the previous to the next element, making it a singly linked list. For linked
lists where the relationship is both ways, those are called doubly linked lists which are
not shown here.

The code here is inspired by: Brian Faure, GitHub: bfaure

"""


class node:  # This class is used to create a node for each element in the linked list
    def __init__(self, data=None):
        self.data = data  # Initialises data to None
        self.next = None  # Initialises the next index to be none


class LinkedList:
    def __init__(self):
        self.head = node()  # Makes the head of the list an instance of node, placeholder to allow us to point to first element in the list
        self.tail = self.head  # At the beginning, the head and the tail are both equal as there is no data

    def append(self, data):
        """
        Appends data to the linked list
        :param data: The data to add to the list
        :return: None
        """
        new_node = node(data)  # Creates a new instance of a node with the data specified
        self.tail.next = new_node
        self.tail = new_node  # changes the tail value to the input value

    def length(self):
        """
        Returns the amount of elements in the linked list
        :return:number of elements
        """
        cur = self.head  # A variable to store the node we're currently looking at
        total = 0
        while cur.next is not None:
            total += 1
            cur = cur.next
        return total

    def contents(self):
        """
        returns the contents of the linked list
        :return: list
        """
        elems = []  # Creates an empty placeholder list to hold all the elements in the linked list
        cur_node = self.head  # Sets the current element to the head node (element)
        while cur_node.next is not None:  # Iterates through all the elements until the last element is reached
            cur_node = cur_node.next
            elems.append(cur_node.data)  # Appends each element to the list to be printed later
        return elems

    def get(self, index):
        """
        Returns the element at the specified index
        :param index: index of element
        :return: element
        """
        if index >= self.length():  # Checks if the index specified is out of the range of the linked list
            print("Error")
            return None
        cur_index = 0
        cur_node = self.head  # Starts at the head element
        while True:  # This infinite loop works because we've already checked for a valid index earlier
            cur_node = cur_node.next  # Iterated through all the elements until the index is reached
            if cur_index == index:
                return cur_node.data
            cur_index += 1

    def erase(self, index):
        """
        Removes an element at the specified index by pointing the 'next value' of the last element to the next element
        :param index: index of element
        :return: None
        """
        if index >= self.length():
            print("Error")
            return
        cur_index = 0
        cur_node = self.head
        while True:
            last_node = cur_node  # These two lines iterate through the linked list keeping the instance of each
            cur_node = cur_node.next  # previous element and the current element
            if cur_index == index:
                last_node.next = cur_node.next  # Connects the previous element's 'next pointer' to the next element
                if last_node.next == None:
                    self.tail = last_node  # Here's where we set the tail
                return
            cur_index += 1  # Iterates through the indexes until the specified index is reached

    # Added some 'dunder' (special) methods to allow for better interaction with the objects of this class
    def __repr__(self):  # An unambiguous representation of an instance of this class for developer use
        return "LinkedList()"  # Good idea for this function to return the code used to create the object

    def __str__(self):  # An unambiguous representation of an instance of this class for the end user
        return f"{type(self).__name__} with contents: {self.contents()}"  # First term of the string is the name of the class

    def __add__(self, other):  # Allows the '+' functionality to append two linked list objects
        if isinstance(other, LinkedList):  # Checks if the second object is an instance of the LinkedList class
            elem = []
            for _ in self.contents():  # Iterates through and appends all of the contents of the second object to the first
                elem.append(_)
            for _ in other.contents():
                elem.append(_)
            return elem  # Note the returned object will not be a linked list, I need to address this issue
        else:  # If the second object is not an instance of the LinkedList class, an error is raised
            raise Exception("You cannot add a LinkedList object to objects of another type/class")

    def __len__(self):  # Allows the use of 'len()' to get the length of the linked list
        return self.length()

    def __getitem__(self, index):  # Allows for square bracket list functionality e.g. my_list[i] returns the
        return self.get(index)  # element at the ith index


# Debug/test code
# my_list = LinkedList()
# my_list.append(5)
# my_list.append(6)
# my_list.append(7)
# my_list.append(8)
# print(my_list)
# my_list.erase(2)
# print(my_list)
#
# my_list2 = LinkedList()
# my_list2.append(198)
# my_list2.append(10)
# print(my_list2.contents())
#
# print(f"List 1 + List 2: {my_list + my_list2}")
# print(my_list)




