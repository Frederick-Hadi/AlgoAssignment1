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

#python3 spreadsheetFilebased.py linkedlist sampleData.txt sampleCommands.in linkedList.out
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


    def printLL(self):
        currNode = self.head
        while currNode != None:
            x = currNode.value.head
            while x != None:
                print("At row: ",x.row, "column: ",x.col,", the value is: ",x.value)
                x = x.next
            print()
            currNode = currNode.next
        


    def printList(self):
        if(self.head == None):
            print('Empty!')
        else:
            node = self.head
            while(node is not None):
                print(node.value),
                node = node.next 

    #add a value to the end of the list
    def append(self, data,row = False): 

        if row:
            if self.head != None:
                toConstruct = self.head.value.len
                col = 0
                while toConstruct > 0:
                    data.value.append(Node(None, self.len, col))
                    toConstruct -= 1
                    col+=1
            #data.value.printList()
            else:
                data.value.append(Node(None, self.len, 0))

        if self.head == None:
            self.head = data
            self.tail = data
            self.len += 1
        else:
            data.prev = self.tail
            self.tail.next = data
            self.tail = data
            self.len +=1

    #insert a value at a certain position
    def correctValsRows(self, node):
        currN = node.next
        #tempLL = []
        while currN != None:
            currRNode = currN.value.head
            while currRNode != None:
                currRNode.row += 1
                #tempLL.append(currRNode)
                currRNode = currRNode.next
            currN = currN.next


    def insertAt(self, index, value, row=True):
        
        #loop from either end of the list
     
        toConstruct = self.head.value.len
        susOmeter = 0
        while toConstruct > 0:
            value.value.append(Node(None,index,susOmeter))
            susOmeter += 1
            toConstruct -= 1
        #self.len += 1

        if index == self.len-1:
            value.prev = self.tail
            self.tail.next = value
            self.tail = value
            self.correctValsRows(value)
            self.len += 1
            return
    
        elif index == 0:
            value.next = self.head
            self.head.prev = value
            self.head = value
            self.correctValsRows(value)
            self.len += 1
            return
    
        elif index < self.len/2:
            currNode = self.head
            while index > 0:
                currNode = currNode.next
                index -= 1
        else:
            currNode = self.tail
            while index < self.len:
                currNode = currNode.prev
                index += 1
        
        prevN = currNode.prev
        value.next = currNode
        value.prev = prevN
        prevN.next = value
        currNode.prev = value
        self.correctValsRows(value)
        self.len += 1


    def correctValsCols(self, node):
        currNode = node.next
        while currNode != None:
                currNode.col += 1
                currNode = currNode.next
        self.len += 1


    def insertAtCol(self, index, value):
        
        if index == self.len:
            value.prev = self.tail
            self.tail.next = value
            self.tail = value
            self.correctValsCols(value)
            return
    
        elif index == 0:
            value.next = self.head
            self.head.prev = value
            self.head = value
            currNode = self.head
            self.correctValsCols(value)
            return
    
        elif index < self.len/2:
            currNode = self.head
            while index > 0:
                currNode = currNode.next
                index -= 1
        else:
            currNode = self.tail
            while index < self.len:
                currNode = currNode.prev
                index += 1
        
        prevN = currNode.prev
        value.next = currNode
        value.prev = prevN
        prevN.next = value
        currNode.prev = value
        self.correctValsCols(value)
        
       

    def updateVal(self,row,col,val):
        
        if col > self.len/2:
            currNode = self.tail
            while col < self.len-1:
                currNode = currNode.prev
                col += 1
                #print(currNode)
            #print("Updating value at row: ",currNode.row," column: ",currNode.col," from:" ,currNode.value," to: ",val)
            currNode.value = val
        else:
            currNode = self.head
            while col > 0:
                currNode = currNode.next
                col -= 1
            #print("Updating value at row: ",currNode.row," column: ",currNode.col," from:" ,currNode.value," to: ",val)
            currNode.value = val
    
    def findVals(self, value):
        currNode = self.head
        listOfNodes = []
        while currNode != None:
            if currNode.value == value:
                listOfNodes.append((currNode.row,currNode.col))
            currNode = currNode.next
        #print(listOfNodes)
        return listOfNodes
    
    def findNonEmpty(self):
        currNode = self.head
        listOfNodes = []
        while currNode != None:
            if currNode.value != None:
                listOfNodes.append(Cell(currNode.row,currNode.col,currNode.value))
                #print("ran")
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
        currRow = -1
        #llRow = DoubleLinkedList()
        maxRows = 0
        maxCols = 0
        #maybe remove next for loop by getting max rows and cols from last value of l
        # same code, as below in string i just dont loop over lcells twice. 
        for val in lCells:
            if val.row > maxRows:
                diff = val.row - maxRows
                for i in range(diff+1):
                    self.spread.append(Node(DoubleLinkedList()),True)
                maxRows = self.spread.len
            if val.col > maxCols:
                diff = val.col - maxCols
                for i in range(diff):
                    self.appendCol()
                maxCols = self.spread.head.value.len
            if val.row <= maxRows and val.row >= 0:
                if val.col <= maxCols and val.col >= 0:
                    self.update(val.row,val.col,val.val) 
        #'''
        """for val in lCells:
            if val.row > maxRows:
                maxRows = val.row
            if val.col > maxCols:
                maxCols = val.col
        
        for i in range(maxRows+1):
            llRow = DoubleLinkedList()
            for j in range(maxCols+1):
                llRow.append(Node(None, i,j))
            self.spread.append(Node(llRow,i))
        
        for val in lCells:
            #print(val)
            self.update(val.row,val.col,val.val)
            
            #print(x)"""""
        
        #self.spread.printLL()
        #print("sheet built")




    def appendRow(self):
        """
        Appends an empty row to the spreadsheet.
        """
        self.spread.append(Node(DoubleLinkedList()),True)
        #print("after")
        #self.spread.printLL()
        return True
        # TO BE IMPLEMENTED
        


    def appendCol(self):
        """
        Appends an empty column to the spreadsheet.

        @return True if operation was successful, or False if not.
        """
        currN = self.spread.head
        if currN == None:
            return False
        while currN != None:
            currRowN = currN.value
            currRowN.append(Node(None,currRowN.head.row, currRowN.len))
            currN = currN.next
        #print("after append col")
        #self.spread.printLL()
        return True


    def insertRow(self, rowIndex: int)->bool:
        """
        Inserts an empty row into the spreadsheet.

        @param rowIndex Index of the existing row that will be after the newly inserted row.  If inserting as first row, specify rowIndex to be 0.  If inserting a row after the last one, specify rowIndex to be rowNum()-1.

        @return True if operation was successful, or False if not, e.g., rowIndex is invalid.
        """
        if rowIndex < 0 or rowIndex > self.spread.len:
            return False
        
        newNode = DoubleLinkedList()
        self.spread.insertAt(rowIndex, Node(newNode,rowIndex))
        #print("after insert row")
        #self.spread.printLL()
        return True
        


    def insertCol(self, colIndex: int)->bool:
        """
        Inserts an empty column into the spreadsheet.

        @param colIndex Index of the existing column that will be before the newly inserted row.  If inserting as first column, specify colIndex to be -1.
        """
        if self.spread.head ==None:
            return False
        colVals = self.spread.head.value.len
        if colIndex < -1 or colIndex >= colVals:
            return False
        colIndex+=1
        currN = self.spread.head
        while currN != None:
            currRowN = currN.value
            currRowN.insertAtCol(colIndex, Node(None,currRowN.head.row,colIndex))
            currN = currN.next
        #print("after insert col")
        #self.spread.printLL()  
        
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
        #print(self.spread.len)
        #print(self.spread.head.value.len)
        #print("updating row: ",rowIndex," col ",colIndex," with value: ",value)
        #print("current spreadsheet len: ",self.spread.len," and current row len: ",self.spread.head.value.len)
        #print()
        if self.spread.head == None:
            return False
        if rowIndex >= self.spread.len or colIndex >= self.spread.head.value.len or rowIndex < 0 or colIndex < 0:
            return False
        
        row = rowIndex
        col = colIndex
        #print("row: ",row)
        #print("col: ",col)

        #rowIndex+=1
        #colIndex+=1
        if rowIndex < self.spread.len/2:
            currN = self.spread.head
            while rowIndex > 0:
                currN = currN.next
                rowIndex -= 1
            currN.value.updateVal(row,col, value)
        else:
            currN = self.spread.tail
            #rowIndex +=1
            #print("amount of rows in the list: ",self.spread.len)
            while rowIndex < self.spread.len-1:
                currN = currN.prev
                rowIndex += 1
    
            currN.value.updateVal(row ,col, value)
        
        print("after update")
        self.spread.printLL()
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
        return self.spread.head.value.len



    def find(self, value: float) -> [(int, int)]:
        """
        Find and return a list of cells that contain the value 'value'.

        @param value value to search for.

        @return List of cells (row, col) that contains the input value.
	    """

        currN = self.spread.head
        values = []
        while currN != None:
            currRowN = currN.value
            values  += currRowN.findVals(value)
            currN = currN.next

        #print("this was values: ", values)
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
        while currN != None:
            currRowN = currN.value
            values  += currRowN.findNonEmpty()
            currN = currN.next
        #print("this was values, entries: ", values)
        # TO BE IMPLEMENTED
        return values
