from spreadsheet.baseSpreadsheet import BaseSpreadsheet
from spreadsheet.cell import Cell
import time
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
        self.built = False
        # keep track of max column index
        self.columns = 0
        self.abs_tol = 1e-9

    def print_summary(self):
        print("SUM:", self.sumA)
        print("VAL:", self.valA)
        print("COL:", self.colA)
        print()

    def buildSpreadsheet(self, lCells: [Cell]):
        """
        Construct the data structure to store nodes.
        @param lCells: list of cells to be stored
        """
        # assume row is a reasonable value range of [0, n]
        # where 0 is the first row and n = self.rows
        start = time.perf_counter()
        for cell in lCells:
            # UPDATING sumA
            # --------------
            if cell.row > self.rowNum() - 1:
                # extend the end of the array to match with new last row
                # with the repeated value at the end of the original array
                self.sumA.extend([self.sumA[-1]] * (cell.row - self.rowNum() + 1))

            # update sum
            old_sum_val = self.sumA[cell.row + 1]
            for i in range(cell.row + 1, len(self.sumA)):
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
                val_index = 0

                while math.isclose(old_sum_val, curr_sum, abs_tol=self.abs_tol) == False:
                    curr_sum += self.valA[val_index]
                    val_index += 1
                
                # prev_row_index is the index of the first value of the updated row
                prev_val_index = 0
                curr_sum = 0
                while math.isclose(curr_sum, self.sumA[cell.row], abs_tol=self.abs_tol) == False:
                    # first get the last val of the previous row
                    curr_sum += self.valA[prev_val_index]
                    prev_val_index += 1

                for index_to_insert in range(prev_val_index, val_index):
                    if cell.col < self.colA[index_to_insert]:
                        # if not equal but is less than, that means an empty cell
                        # is being updated
                        self.colA.insert(index_to_insert, cell.col)
                        self.valA.insert(index_to_insert, cell.val)
                        break
                    elif cell.col == self.colA[index_to_insert]:
                        old_val = self.valA[index_to_insert]
                        for i in range(cell.row + 1, len(self.sumA)):
                            self.sumA[i] -= old_val
                        # update the new value in valA
                        self.valA[index_to_insert] = cell.val
                        break
                else:
                    # reached the end of the row, meaning this is a previously null cell
                    # and is also the latest column that has a value, so insert appropriately.
                    # val_index has this
                    self.colA.insert(val_index, cell.col)
                    self.valA.insert(val_index, cell.val)
        
        end = time.perf_counter()
        timeTaken = end - start
        print(self.rowNum())
        with open("enuma.txt", "a") as f:
            f.write("For creating a CSR: " +str(timeTaken) + " of size " + str(self.rowNum()) + "x" + str(self.colNum())+"\n")
        f.close()
        self.built = True          

    

    def appendRow(self):
        """
        Appends an empty row to the spreadsheet.

        @return True if operation was successful, or False if not.
        """
        
        start = time.perf_counter()
        if self.sumA != None:
            self.sumA.append(self.sumA[-1])
            end = time.perf_counter()
            timeTaken = end - start
            if self.built:
                with open("enuma.txt", "a") as f:
                    f.write("For appending row: " +str(timeTaken)+"\n")
                f.close()
            return True
        else:
            return False


    def appendCol(self):
        """
        Appends an empty column to the spreadsheet.

        @return True if operation was successful, or False if not.
        """
        start = time.perf_counter()
        if self.colA != None:
            self.columns += 1
            end = time.perf_counter()
            timeTaken = end - start
            if self.built:
                with open("enuma.txt", "a") as f:
                    f.write("For appending col: " +str(timeTaken)+"\n")
                f.close()
            return True
        else:
            return False


    def insertRow(self, rowIndex: int)->bool:
        """
        Inserts an empty row into the spreadsheet.

        @param rowIndex Index of the existing row that will be after the newly inserted row.  If inserting as first row, specify rowIndex to be 0.  If inserting a row after the last one, specify rowIndex to be rowNum()-1.

        @return True if operation was successful, or False if not, e.g., rowIndex is invalid.
        """

        start = time.perf_counter()
        if rowIndex < -1 or rowIndex > self.rowNum():
            return False
        else:
            self.sumA.insert(rowIndex + 1, self.sumA[rowIndex])
            end = time.perf_counter()
            timeTaken = end - start
            if self.built:
                with open("enuma.txt", "a") as f:
                    f.write("For insert row: " +str(timeTaken)+"\n")
                f.close()
            return True
            

    def insertCol(self, colIndex: int)->bool:
        """
        Inserts an empty column into the spreadsheet.

        @param colIndex Index of the existing column that will be after the newly inserted row.  If inserting as first column, specify colIndex to be 0.  If inserting a column after the last one, specify colIndex to be colNum()-1.

        return True if operation was successful, or False if not, e.g., colIndex is invalid.
        """
        start = time.perf_counter()
        self.columns += 1
        if colIndex < -1 or colIndex > self.rowNum():
            return False
        else:
            # update new highest index column
            if colIndex > self.columns:
                self.columns = colIndex

            # all columns after specified column increase by one
            for i in range(len(self.colA)):
                if self.colA[i] > colIndex:
                    self.colA[i] += 1
            end = time.perf_counter()
            timeTaken = end - start
            if self.built:
                with open("enuma.txt", "a") as f:
                    f.write("For insert col: " +str(timeTaken)+"\n")
                f.close()
            return True



    def update(self, rowIndex: int, colIndex: int, value: float) -> bool:
        """
        Update the cell with the input/argument value.

        @param rowIndex Index of row to update.
        @param colIndex Index of column to update.
        @param value Value to update.  Can assume they are floats.

        @return True if cell can be updated.  False if cannot, e.g., row or column indices do not exist.
        """
        start = time.perf_counter()
        if rowIndex < -1 or rowIndex > self.rowNum() or colIndex < -1 or colIndex > self.columns:
            return False
        else:
            # update sum
            for i in range(rowIndex + 1, len(self.sumA)):
                self.sumA[i] += value

            # --------------
            # UPDATING colA and valA
            # because inserts happen at the same place respectively
            # --------------

            curr_sum = 0
            val_index = 0
            
            # val_index is the index of the last val in the row that contains the updated cell
            # but one extra
            while math.isclose(self.sumA[rowIndex + 1] - curr_sum, value, abs_tol=self.abs_tol) == False:
                curr_sum += self.valA[val_index]
                val_index += 1
            

            # prev_row_index is the index of the first value of the updated row
            prev_val_index = 0
            curr_sum = 0
            while math.isclose(curr_sum, self.sumA[rowIndex], abs_tol=self.abs_tol) == False:
                # first get the last val of the previous row
                curr_sum += self.valA[prev_val_index]
                prev_val_index += 1


            for index_to_insert in range(prev_val_index, val_index):
                if colIndex == self.colA[index_to_insert]:
                    # there was already a value in this spreadsheet cell
                    # so subtract what used to be there from sum to fully update
                    for i in range(rowIndex + 1, len(self.sumA)):
                        self.sumA[i] -= self.valA[index_to_insert]
                    # update the new value in valA
                    self.valA[index_to_insert] = value
                    break
                elif colIndex < self.colA[index_to_insert]:
                    # if not equal but is less than, that means an empty cell
                    # is being updated
                    self.colA.insert(index_to_insert, colIndex)
                    self.valA.insert(index_to_insert, value)
                    break
            else:
                # reached the end of the row, meaning this is a previously null cell
                # and is also the latest column that has a value, so insert appropriately.
                # val_index has this
                self.colA.insert(val_index, colIndex)
                self.valA.insert(val_index, value)
            end = time.perf_counter()
            timeTaken = end - start
            if self.built:
                with open("enuma.txt", "a") as f:
                    f.write("For update: " +str(timeTaken)+"\n")
                f.close()
            return True



    def rowNum(self)->int:
        """
        @return Number of rows the spreadsheet has.
        """
        start = time.perf_counter()
        end = time.perf_counter()
        timeTaken = end - start
        if self.built:
            with open("enuma.txt", "a") as f:
                f.write("For rowNum: " +str(timeTaken)+"\n")
            f.close()
        return len(self.sumA) - 1


    def colNum(self)->int:
        """
        @return Number of column the spreadsheet has.
        """
        start = time.perf_counter()
        end = time.perf_counter()
        timeTaken = end - start
        if self.built:
            with open("enuma.txt", "a") as f:
                f.write("For colNum: " +str(timeTaken)+"\n")
            f.close()
        return self.columns + 1


    def find(self, value: float) -> [(int, int)]:
        """
        Find and return a list of cells that contain the value 'value'.

        @param value value to search for.

        @return List of cells (row, col) that contains the input value.
	    """
        start = time.perf_counter()
        matches = []
        curr_sum = 0
        check_change = self.sumA[0]
        # val_index is the same as col_index
        val_index = 0

        for row_index, sum in enumerate(self.sumA):
            # once the next value in sumA changes 
            # (the next non-zero value has been reached)
            if math.isclose(check_change, sum, abs_tol=self.abs_tol) == False:
                curr_sum += self.valA[val_index]
                if self.valA[val_index] == value:
                    matches.append((row_index - 1, self.colA[val_index]))
                # if there are multiple NZVs in one row,
                # the sum of values in valA so far and the current sumA item
                # will not match, so keep going through until it does.
                while math.isclose(curr_sum, sum, abs_tol=self.abs_tol) == False:
                    val_index += 1
                    if self.valA[val_index] == value:
                        matches.append((row_index - 1, self.colA[val_index]))
                    curr_sum += self.valA[val_index]
                
                val_index += 1
                check_change = self.sumA[row_index]
        end = time.perf_counter()
        timeTaken = end - start
        if self.built:
            with open("enuma.txt", "a") as f:
                f.write("For find: " +str(timeTaken)+"\n")
            f.close()
        return matches


    def entries(self) -> [Cell]:
        """
        return a list of cells that have values (i.e., all non None cells).
        """ 

        start = time.perf_counter()
        matches = []
        curr_sum = 0
        check_change = self.sumA[0]
        # val_index is the same as col_index
        val_index = 0

        for row_index, sum in enumerate(self.sumA):
            # once the next value in sumA changes 
            # (the next non-zero value has been reached)
            if math.isclose(check_change, sum, abs_tol=self.abs_tol) == False:
                curr_sum += self.valA[val_index]

                matches.append(Cell(row_index - 1, self.colA[val_index], self.valA[val_index]))
                # if there are multiple NZVs in one row,
                # the sum of values in valA so far and the current sumA item
                # will not match, so keep going through until it does.
                while math.isclose(curr_sum, sum, abs_tol=self.abs_tol) == False:
                    val_index += 1
                    matches.append(Cell(row_index - 1, self.colA[val_index], self.valA[val_index]))
                    curr_sum += self.valA[val_index]
                
                val_index += 1
                check_change = self.sumA[row_index]
        end = time.perf_counter()
        timeTaken = end - start
        if self.built:
            with open("enuma.txt", "a") as f:
                f.write("For entries: " +str(timeTaken)+"\n")
            f.close()
        return matches
