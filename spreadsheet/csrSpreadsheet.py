from spreadsheet.baseSpreadsheet import BaseSpreadsheet
from spreadsheet.cell import Cell

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
            # UPDATING sumA
            # --------------
            if cell.row > len(self.sumA):
                # extend the end of the array to match with new last row
                # with the repeated value at the end of the original array
                self.sumA.extend([self.sumA[-1]] * (cell.row + 1 - len(self.sumA)))
            # update sum
            # need a + 1 because sumA[0] is always 0
            # (sum of everything up to row 0 is always 0 because nothing comes before it)
            for i in range(cell.row, len(self.sumA)):
                self.sumA[i] += cell.val

            # UPDATING colA and valA
            # because inserts happen at the same place respectively
            # --------------
            if cell.col > self.columns:
                # if new max is found, set columns as new max
                self.columns = cell.col
            
            check_sum_change = self.sumA[0]
            num_sum_changes = -1
            # each time the sum changes in sumA, that means a new value
            for curr_row_sum in range(cell.row + 1):
                if self.sumA[curr_row_sum] != check_sum_change:
                    num_sum_changes += 1
                    check_sum_change = self.sumA[curr_row_sum]
            # cases for when data is in the same row as another
            # curr_sum = self.sumA[num_sum_changes]
            # column_order = 0
            # while curr_sum < self.sumA[num_sum_changes]:
            #     curr_sum += self.valA[column_order]
            #     column_order += 1
            # index = num_sum_changes + (column_order - num_sum_changes)




            # attempt 2, kill 2 birds with 1 stone
            if len(self.colA) == 0:
                self.colA.append(cell.col)
                self.valA.append(cell.val)
            else:
                curr_sum = 0
                sum_index = 0

                while self.sumA[cell.row] - curr_sum != cell.val:
                    curr_sum += self.valA[sum_index]
                    sum_index += 1

                self.colA.insert(sum_index, cell.col)
                self.valA.insert(sum_index, cell.val)

        print(self.sumA)
        print(self.colA)
        print(self.valA)


        


    def appendRow(self):
        """
        Appends an empty row to the spreadsheet.

        @return True if operation was successful, or False if not.
        """

        # TO BE IMPLEMENTED
        pass


    def appendCol(self):
        """
        Appends an empty column to the spreadsheet.

        @return True if operation was successful, or False if not.
        """

        # TO BE IMPLEMENTED
        pass


    def insertRow(self, rowIndex: int)->bool:
        """
        Inserts an empty row into the spreadsheet.

        @param rowIndex Index of the existing row that will be after the newly inserted row.  If inserting as first row, specify rowIndex to be 0.  If inserting a row after the last one, specify rowIndex to be rowNum()-1.

        @return True if operation was successful, or False if not, e.g., rowIndex is invalid.
        """

        # REPLACE WITH APPROPRIATE RETURN VALUE
        return True


    def insertCol(self, colIndex: int)->bool:
        """
        Inserts an empty column into the spreadsheet.

        @param colIndex Index of the existing column that will be after the newly inserted row.  If inserting as first column, specify colIndex to be 0.  If inserting a column after the last one, specify colIndex to be colNum()-1.

        return True if operation was successful, or False if not, e.g., colIndex is invalid.
        """

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

        # TO BE IMPLEMENTED

        # REPLACE WITH APPROPRIATE RETURN VALUE
        return True


    def rowNum(self)->int:
        """
        @return Number of rows the spreadsheet has.
        """

        return len(self.sumA) - 1


    def colNum(self)->int:
        """
        @return Number of column the spreadsheet has.
        """
        # TO BE IMPLEMENTED
        return 0




    def find(self, value: float) -> [(int, int)]:
        """
        Find and return a list of cells that contain the value 'value'.

        @param value value to search for.

        @return List of cells (row, col) that contains the input value.
	    """

        # TO BE IMPLEMENTED

        # REPLACE WITH APPROPRIATE RETURN VALUE
        return []




    def entries(self) -> [Cell]:
        """
        return a list of cells that have values (i.e., all non None cells).
        """

        return []
