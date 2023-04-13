from spreadsheet.baseSpreadsheet import BaseSpreadsheet
from spreadsheet.cell import Cell


# class ListNode:
#     '''
#     Define a node in the linked list
#     '''
#
#     def __init__(self, word_frequency: WordFrequency):
#         self.word_frequency = word_frequency
#         self.next = None

# ------------------------------------------------------------------------
# This class  is required TO BE IMPLEMENTED
# Linked-List-based spreadsheet implementation.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2023, RMIT University'
# ------------------------------------------------------------------------
class Node:
    #should work without this right?
    '''
    def __init__(self, value):
        self.value = value

        self.next = None
        self.prev = None
    '''

    def __init__(self, value,row = None,col = None):
        self.value = value

        self.row = row
        self.col = col

        self.next = None
        self.prev = None

       

class DoubleLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0


    #add a value to the end of the list
    def append(self, new_data): 
        if self.head == None:
            self.head = new_data
            self.tail = new_data
        else:
            self.tail.next = new_data
            new_data.prev = self.tail
            self.tail = new_data
            self.len =+1

    #insert a value at a certain position
    def insertAt(self, index, value):
        
            #loop from either end of the list
        currNode = None
        if index <= self.len/2:
            currNode = self.head
            #setting the head if inserted as first row
            if index == 0:
                self.head = value
            while index > 0:
                currNode = currNode.next
                index -= 1
        else:
            currNode = self.tail
            #setting the tail if inserted as last row
            if index == self.len:
                self.tail = value
            while index <= self.len:
                currNode = currNode.prev
                index += 1
        
        #insert the value
        value.next = currNode
        value.prev = currNode.prev
        currNode.prev = value
    
        toConstruct = self.head.len
        while toConstruct > 0:
            value.append(Node(None))
            toConstruct -= 1
       

    def updateVal(self,col,val):

        if col > self.len/2:
            currNode = self.tail
            while col <= self.len:
                currNode = currNode.prev
                col += 1
            currNode.val = val
    
    def findVals(self, value):
        currNode = self.head
        listOfNodes = []
        while currNode != None:
            if currNode.value == value:
                listOfNodes.append((currNode.row,currNode.col))
            currNode = currNode.next
        return listOfNodes
    
    def findNonEmpty(self):
        currNode = self.head
        listOfNodes = []
        while currNode != None:
            if currNode.value != None:
                listOfNodes.append((currNode.row,currNode.col))
            currNode = currNode.next
        return listOfNodes
            


class LinkedListSpreadsheet(BaseSpreadsheet):

    def __init__(self):
        # TO BE IMPLEMENTED
        self.spread = DoubleLinkedList()
        


    def buildSpreadsheet(self, lCells: [Cell]):
        """
        Construct the data structure to store nodes.
        @param lCells: list of cells to be stored
        """
        currRow = 0
        #llRow = DoubleLinkedList()
        for val in lCells:
            if val.row != currRow:
                currRow = val.row
                llRow = DoubleLinkedList()
                llRow.append(Node(val))
                self.spread.append(Node(llRow))
            else:
                llRow.append(Node(val.val,val.row, val.col))




    def appendRow(self):
        """
        Appends an empty row to the spreadsheet.
        """
        self.spread.append(Node(None))

        # TO BE IMPLEMENTED
        


    def appendCol(self):
        """
        Appends an empty column to the spreadsheet.

        @return True if operation was successful, or False if not.
        """
        currN = self.spread.head
        while currN.next != None:
            currRowN = currN.value.head
            currRowN.append(Node(None))
        


    def insertRow(self, rowIndex: int)->bool:
        """
        Inserts an empty row into the spreadsheet.

        @param rowIndex Index of the existing row that will be after the newly inserted row.  If inserting as first row, specify rowIndex to be 0.  If inserting a row after the last one, specify rowIndex to be rowNum()-1.

        @return True if operation was successful, or False if not, e.g., rowIndex is invalid.
        """
        if rowIndex < -1 or rowIndex > self.len:
            return False
        
        newNode = Node(None)
        self.spread.insertAt(rowIndex+1, newNode)
        return True
        


    def insertCol(self, colIndex: int)->bool:
        """
        Inserts an empty column into the spreadsheet.

        @param colIndex Index of the existing column that will be before the newly inserted row.  If inserting as first column, specify colIndex to be -1.
        """

        colVals = self.spread.head.len
        if colIndex < -1 or colIndex > colVals:
            return False

        currN = self.spread.head
        while currN.next != None:
            currRowN = currN.value.head
            currRowN.insertAt(colIndex+1, Node(None))
            currN = currN.next

        # REPLACE WITH APPROPRIATE RETURN VALUE
        return True


    def update(self, rowIndex: int, colIndex: int, value: float) -> bool:
        """
        Update the cell with the input/argument value.

        @param rowIndex Index of row to update.
        @param colIndex Index of column to update.
        @param value Value to update.  Can assume they are floats.

        @return True if cell can be updated.  False if cannot, e.g., row or column indices do not exist.
        """

        if rowIndex > self.spread.len or colIndex > self.spread.head.len or rowIndex < 0 or colIndex < 0:
            return False

        currN = self.spread.head
        if rowIndex <= self.spread.len/2:
            while rowIndex > 0:
                currN = currN.next
                rowIndex -= 1
            currN.updateVal(colIndex, value)

        return True


    def rowNum(self)->int:
        """
        @return Number of rows the spreadsheet has.
        """

        # TO BE IMPLEMENTED
        return self.spread.len


    def colNum(self)->int:
        """
        @return Number of column the spreadsheet has.
        """

        # TO BE IMPLEMENTED
        return self.spread.head.len



    def find(self, value: float) -> [(int, int)]:
        """
        Find and return a list of cells that contain the value 'value'.

        @param value value to search for.

        @return List of cells (row, col) that contains the input value.
	    """

        currN = self.spread.head
        values = []
        while currN.next != None:
            values  += currN.findVals(value)
            currN = currN.next


        # REPLACE WITH APPROPRIATE RETURN VALUE
        return values



    def entries(self) -> [Cell]:
        """
        @return A list of cells that have values (i.e., all non None cells).
        """

        # TO BE IMPLEMENTED
        
        #return all non none celss
        currN = self.spread.head
        values = []
        while currN.next != None:
            values  += currN.findNonEmpty()
            currN = currN.next

        # TO BE IMPLEMENTED
        return values
