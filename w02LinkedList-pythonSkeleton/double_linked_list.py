import math

class Node:
    '''
    A basic type in linked list
    '''
    def __init__(self, value):
        self.m_value = value
        self.m_next = None
        self.m_prev = None

    def get_value(self):
        return self.m_value

    def get_next(self):
        return self.m_next
    
    def get_prev(self):
        return self.m_prev

    def set_value(self, value):
        self.m_value = value

    def set_next(self, next):
        self.m_next = next

    def set_prev(self, prev):
        self.m_prev = prev

    

class DoubleLinkedList:
    """ 
    Double linked list that implements interface MyList.

    """
    def __init__(self):
        """
        Default constructor.
        """
        self.m_head = None
        self.m_tail = None
        self.m_length = 0
   
    def add(self, new_value):
        """
        Add a new value to the start of the list.
        
        @param newValue Value to add to list.
        """
        # IMPLEMENT ME!

    def insert(self, index, new_value):
        """
        Insert value (and corresponding node) at position 'index'.  Indices start at 0.
        
        @param index Position in list to add new value to.
        @param newValue Value to add to list.
        
        @throws IndexError Index is out of bounds.   
        """
        if index >= self.m_length or index < 0:
            raise IndexError("Supplied index is invalid.")

        # IMPLEMENT ME!


    def get(self, index):
        """ 
        Returns the value stored in node at position 'index' of list.
        
        @param index Position in list to get new value for.
        @return Value of element at specified position in list.
        
        @throws IndexError Index is out of bounds.
        """
        if index >= self.m_length or index < 0:
            raise IndexError("Supplied index is invalid.")

        cur_node = None
        if index < math.ceil(self.m_length / 2):
            cur_node = self.m_head
            for i in range(index): 
                cur_node = cur_node.get_next()
        else:
            cur_node = self.m_tail
            for i in range(self.m_length-1, index, -1): 
                cur_node = cur_node.get_prev()

        return cur_node.get_value()



    def search(self, value):
        """
        Searches for the index that contains value.  If value is not present,
        method returns -1 (NOT_IN_ARRAY).
        If there are multiple values that could be returned, return the one with
        the smallest index.
        
        @param value Value to search for.
        @return Index where value is located, otherwise returns -1 (NOT_IN_ARRAY).  
        """
        cur_node = self.m_head
        for i in range(self.m_length): 
            if cur_node.get_value() == value:
        	    return i
        	
            cur_node = cur_node.get_next()

        return -1



    def remove(self, value):
        """
        Delete given value from list (delete first instance found).
        
        @param value Value to remove.
        @return True if deletion was successful, otherwise false.   
        """
        # IMPLEMENT ME!

        # couldn't find a node with value
        return False


    def remove_by_index(self, index, dummy=None):
        """
        Delete value (and corresponding node) at position 'index'.  Indices start at 0.
        
        @param index Position in list to get new value for.
        @param dummy Dummy variable, serves no use apart from distinguishing overloaded methods.
        @return Value of node that was deleted.
        
        @throws IndexError Index is out of bounds.   
        """
        if index >= self.m_length or index < 0:
            raise IndexError("Supplied index is invalid.")
        
        # IMPLEMENT ME!


    def min(self):    
        """
        Returns the minimum value in the list.
        
        @return Minimum value in the list.
        
        @throws ArithmeticError Index is out of bounds.    
        """
        if self.m_length == 0:
            raise ArithmeticError("Min is not defined for an empty list.")

        # traverse list, looking for the minimum valued element
        min_value = self.m_head.get_value()
        cur_node = self.m_head.get_next()

        while cur_node != None:
            if cur_node.get_value() < min_value:
                min_value = cur_node.get_value()
            cur_node = cur_node.get_next()

        return min_value


    def max(self):
        """
        Returns the maximum value in the list.
        
        @return Maximum value in the list.
        
        @throws ArithmeticError Index is out of bounds.   
        """
        if self.m_length == 0:
            raise ArithmeticError("Max is not defined for an empty list.")

        # traverse list, looking for the minimum valued element
        max_value = self.m_head.get_value();
        cur_node = self.m_head.get_next();

        while cur_node != None:
            if cur_node.get_value() > max_value:
                max_value = cur_node.get_value()
            cur_node = cur_node.get_next()

        return max_value


    def print(self):
        """
        Print the list in head to tail.
        """
        print(self)


    def reverse_print(self):
        """
        Print the list from tail to head.
        """
        # IMPLEMENT ME!


    def __str__(self):
        """
        @return String representation of the list.
        """
        allStr = []
        cur_node = self.m_head
        while cur_node != None:
            allStr.append(str(cur_node.get_value()) + " ")
            cur_node = cur_node.get_next()

        return ' '.join(allStr)   