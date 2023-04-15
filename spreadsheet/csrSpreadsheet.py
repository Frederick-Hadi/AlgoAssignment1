from spreadsheet.baseSpreadsheet import BaseSpreadsheet
from spreadsheet.cell import Cell

import math

# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED
# Trie-based dictionary implementation.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2023, RMIT University'
# ------------------------------------------------------------------------




class CSRSpreadsheet(BaseSpreadsheet):

    def __init__(self):
        self.colA = []
        self.valA = []
        self.sumA = [0]
        # self.rows = 0 (you can do len(self.sumA))
        # keep track of max column index
        self.columns = 0


    def buildSpreadsheet(self, lCells: [Cell]):
        """
        Construct the data structure to store nodes.
        @param lCells: list of cells to be stored
        """
        # assume row is a reasonable value range of [0, n]
        # where 0 is the first row and n = self.rows
        for cell in lCells:
            # --------------
            # UPDATING sumA
            # --------------
            if cell.row > len(self.sumA):
                # extend the end of the array to match with new last row
                # with the repeated value at the end of the original array
                self.sumA.extend([self.sumA[-1]] * (cell.row + 1 - len(self.sumA)))
            # update sum
            for i in range(cell.row, len(self.sumA)):
                self.sumA[i] += cell.val

            # --------------
            # UPDATING colA and valA
            # because inserts happen at the same place respectively
            # --------------
            if cell.col > self.columns:
                self.columns = cell.col

            if len(self.colA) == 0:
                self.colA.append(cell.col)
                self.valA.append(cell.val)
            else:
                curr_sum = 0
                sum_index = 0
                # keep summing the values in valA until we find a place where
                # the current cell value matches the expected values in sumA
                while self.sumA[cell.row] - curr_sum != cell.val:
                    curr_sum += self.valA[sum_index]
                    sum_index += 1
                self.colA.insert(sum_index, cell.col)
                self.valA.insert(sum_index, cell.val)

        


    def appendRow(self):
        """
        Appends an empty row to the spreadsheet.

        @return True if operation was successful, or False if not.
        """
        if self.sumA != None:
            self.sumA.append(self.sumA[-1])
            return True
        else:
            return False


    def appendCol(self):
        """
        Appends an empty column to the spreadsheet.

        @return True if operation was successful, or False if not.
        """
        if self.colA != None:
            self.columns += 1
            return True
        else:
            return False


    def insertRow(self, rowIndex: int)->bool:
        """
        Inserts an empty row into the spreadsheet.

        @param rowIndex Index of the existing row that will be after the newly inserted row.  If inserting as first row, specify rowIndex to be 0.  If inserting a row after the last one, specify rowIndex to be rowNum()-1.

        @return True if operation was successful, or False if not, e.g., rowIndex is invalid.
        """
        

        if rowIndex < -1 or rowIndex > self.rowNum():
            return False
        else:
            print("PREV")
            print(rowIndex)
            print(self.sumA)
            print(self.colA)
            print(self.valA)
            print("------------------")

            # self.sumA.insert(rowIndex, self.sumA[rowIndex - 1])
            self.sumA.insert(rowIndex + 1, self.sumA[rowIndex])
            
            print("AFTER")
            print(self.sumA)
            print(self.colA)
            print(self.valA)
            print("------------------")
            print()

            return True
            

    def insertCol(self, colIndex: int)->bool:
        """
        Inserts an empty column into the spreadsheet.

        @param colIndex Index of the existing column that will be after the newly inserted row.  If inserting as first column, specify colIndex to be 0.  If inserting a column after the last one, specify colIndex to be colNum()-1.

        return True if operation was successful, or False if not, e.g., colIndex is invalid.
        """
        self.columns += 1
        if colIndex < -1 or colIndex > self.rowNum():
            return False
        else:
            print("PREV")
            print(colIndex)
            print(self.sumA)
            print(self.colA)
            print(self.valA)
            print("------------------")
            # update new highest index column
            if colIndex > self.columns:
                self.columns = colIndex
            # for i in range(colIndex, len(self.colA)):
            #     self.colA[i] += 1
            for i in range(len(self.colA)):
                if self.colA[i] > colIndex:
                    self.colA[i] += 1
            print("AFTER")
            print(self.sumA)
            print(self.colA)
            print(self.valA)
            print("------------------")
            print()
            
            return True



    def update(self, rowIndex: int, colIndex: int, value: float) -> bool:
        """
        Update the cell with the input/argument value.

        @param rowIndex Index of row to update.
        @param colIndex Index of column to update.
        @param value Value to update.  Can assume they are floats.

        @return True if cell can be updated.  False if cannot, e.g., row or column indices do not exist.
        """
        if rowIndex < -1 or rowIndex > self.rowNum() or colIndex < -1 or colIndex > self.columns:
            return False
        else:
            # update sum
            for i in range(rowIndex, len(self.sumA)):
                self.sumA[i] += value


            # --------------
            # UPDATING colA and valA
            # because inserts happen at the same place respectively
            # --------------

            curr_sum = 0
            sum_index = 0
            # keep summing the values in valA until we find a place where
            # the current cell value matches the expected values in sumA

            while math.isclose(self.sumA[rowIndex] - curr_sum, value) == False:
                curr_sum += self.valA[sum_index]
                sum_index += 1
            
            sum_index -= 1

            if colIndex == self.colA[sum_index]:
                for i in range(rowIndex, len(self.sumA)):
                    self.sumA[i] -= self.valA[sum_index]
                self.valA[sum_index] = value
            else:
                sum_index += 1
                self.colA.insert(sum_index, colIndex)
                self.valA.insert(sum_index, value)
            return True



    def rowNum(self)->int:
        """
        @return Number of rows the spreadsheet has.
        """

        return len(self.sumA)


    def colNum(self)->int:
        """
        @return Number of column the spreadsheet has.
        """
        # TO BE IMPLEMENTED
        return self.columns + 1


    def find(self, value: float) -> [(int, int)]:
        """
        Find and return a list of cells that contain the value 'value'.

        @param value value to search for.

        @return List of cells (row, col) that contains the input value.
	    """
        matches = []
        # rowIndex = 0
        # colIndex = 0


        # curr_sum = 0
        # sum_index = 0
        # keep summing the values in valA until we find a place where
        # the current cell value matches the expected values in sumA
        # for rowIndex in range (self.rowNum()):
        #     if self.sumA[rowIndex] - curr_sum != value:
        #         matches.append((rowIndex, colIndex))
        #         sum_index += 1
        #     curr_sum += self.valA[sum_index]
        #     rowIndex += 1

        curr_sum = 0
        check_change = self.sumA[0]
        # val_index is the same as col_index
        val_index = 0
        for row_index, sum in enumerate(self.sumA):
            # once the next value in sumA changes 
            # (the next non-zero value has been reached)
            if sum != check_change:
                curr_sum += self.valA[val_index]
                if self.valA[val_index] == value:
                    matches.append((row_index, self.colA[val_index]))
                # if there are multiple NZVs in one row,
                # the sum of values in valA so far and the current sumA item
                # will not match, so keep going through until it does.
                while curr_sum != sum:
                    val_index += 1
                    if self.valA[val_index] == value:
                        matches.append((row_index, self.colA[val_index]))
                    curr_sum += self.valA[val_index]
                
                val_index += 1
                check_change = self.sumA[row_index]

        return matches




    def entries(self) -> [Cell]:
        """
        return a list of cells that have values (i.e., all non None cells).
        """ 
        NZVs = []

        curr_sum = 0
        check_change = self.sumA[0]
        # val_index is the same as col_index
        val_index = 0
        for row_index, sum in enumerate(self.sumA):
            # once the next value in sumA changes 
            # (the next non-zero value has been reached)
            if math.isclose(sum, check_change) == False:
                curr_sum += self.valA[val_index]
                
                NZVs.append(Cell(row_index, self.colA[val_index], self.valA[val_index]))
                # if there are multiple NZVs in one row,
                # the sum of values in valA so far and the current sumA item
                # will not match, so keep going through until it does.
                while math.isclose(curr_sum, sum) == False:
                    val_index += 1
                    # print(self.colA, "trying to access", val_index)
                    NZVs.append(Cell(row_index, self.colA[val_index], self.valA[val_index]))
                    curr_sum += self.valA[val_index]
                
                val_index += 1
                check_change = self.sumA[row_index]

        return NZVs
