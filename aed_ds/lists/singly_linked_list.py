from .nodes import SingleListNode
from ..exceptions import EmptyListException, InvalidPositionException
from .singly_linked_list_iterator import SinglyLinkedListIterator

class SinglyLinkedList ():

    def __init__ (self):
        self.head = None
        self.tail = None
        self.num_elements = 0

    # Returns true iff the list contains no elements.
    
    def is_empty(self):
        return self.num_elements == 0

    # Returns the number of elements in the list.

    def size(self):
        return self.num_elements

    # Returns the first element of the list.

    # Throws EmptyListException.

    def get_first(self):
        if self.is_empty():
            raise EmptyListException()
        return self.head.get_element()

    # Returns the last element of the list.

    # Throws EmptyListException.

    def get_last(self):
        if self.is_empty():
            raise EmptyListException()
            pass
        return self.tail.get_element()


    # Returns the element at the specified position in the list.

    # Range of valid positions: 0, ..., size()-1.

    def get(self, position):
        if self.is_empty():
            raise EmptyListException()
        pointer = self.head
        index = 0
        while pointer != None:
            if position == index:
                return pointer.get_element()
            pointer = pointer.get_next()
            index = index + 1


    # Returns the position in the list of the

    # first occurrence of the specified element,

    # or -1 if the specified element does not

    # occur in the list.

    def find(self, element):
        pointer = self.head
        index = 0
        while pointer != None:
            if pointer.get_element() == element:
                return index
            pointer = pointer.get_next()
            index = index + 1
        return -1


    # Inserts the specified element at the first position in the list.


    def insert_first(self, element):
        new_node = SingleListNode (element, self.head)
        if self.is_empty():
            self.tail = new_node
            self.head = self.tail
        else:
            self.head = new_node
        self.num_elements = self.num_elements + 1


    # Inserts the specified element at the last position in the list.

    def insert_last(self, element):
        new_node = SingleListNode (element, None)
        if self.is_empty():
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
        self.num_elements = self.num_elements + 1
     


    # Inserts the specified element at the specified position in the list.

    # Range of valid positions: 0, ..., size().

    # If the specified position is 0, insert corresponds to insertFirst.

    # If the specified position is size(), insert corresponds to insertLast.

    # Throws InvalidPositionException.

    def insert(self, element, position):
        if position < 0 or position > self.size():
            raise InvalidPositionException()
        elif position == 0:
            return self.insert_first(element)
        elif position == self.size():
            return self.insert_last(element)
        previous_pointer = self.head
        pointer = self.head
        index = 0
        while previous_pointer != None:
            if index == position:
                new_node = SingleListNode (element, pointer)
                previous_pointer.set_next(new_node)
                self.num_elements = self.num_elements + 1
                break
            previous_pointer = pointer
            pointer = pointer.get_next()
            index = index + 1

    # Removes and returns the element at the first position in the list.

    # Throws EmptyListException.

    def remove_first(self):
        if self.is_empty():
            raise EmptyListException()
        elif self.head == self.tail:
            result  = self.head.get_element()
            self.make_empty()
            return result
        else:
            old_head = self.head
            self.head = self.head.get_next()
            self.num_elements = self.num_elements - 1
            return old_head.get_element()

    # Removes and returns the element at the last position in the list.

    # Throws EmptyListException.

    def remove_last(self):
        if self.is_empty ():
            raise EmptyListException()
        elif self.head == self.tail:
            result = self.head.get_element()
            self.make_empty()
            return result
        pointer = self.head
        while pointer.get_next().get_next() != None:
            pointer = pointer.get_next()
        old_pointer = pointer.get_next().get_element()
        pointer.set_next (None)
        self.tail = pointer
        self.num_elements = self.num_elements - 1
        return old_pointer

    
    # Removes and returns the element at the specified position in the list.

    # Range of valid positions: 0, ..., size()-1.

    # Throws InvalidPositionException.

    def remove(self, position):
        if position < 0 or position > self.size() - 1:
            raise InvalidPositionException()
        elif position == 0:
            return self.remove_first()
        elif position == self.size() - 1:
            return self.remove_last()
        pointer = self.head
        old_pointer = self.head
        index = 0
        while pointer != None:
            if position == index:
                old_pointer.set_next(pointer.get_next())
                result = pointer.get_element()
                break
            old_pointer = pointer
            pointer = pointer.get_next()
            index+=1
        return result

    # Removes all elements from the list.

    def make_empty(self):
        self.head = None
        self.tail = None
        self.num_elements = 0
 
    # Returns an iterator of the elements in the list (in proper sequence).

    def iterator(self):
        return SinglyLinkedListIterator(self)
