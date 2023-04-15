import random
import os
# python3 spreadsheetFilebased.py linkedlist tasty commands.in DataGen.txt
def write_txt_file(filename, x, t_range, y_range, u_range):
    # x is the number of rows in the file
    # t_range is the range of values for t,T acts as the row
    # y_range is the range of values for y, Y acts as the column
    # u_range is the range of values for u, U acts as the value
    with open(filename, 'w') as f:
        tmax = 0
        uMax = 0
        valMax = 0

        maxRows = t_range[1]
        maxCols = y_range[1]
        x = sparsity(x)
        values = []
        for i in range(x):
            t = round(random.randint(t_range[0], t_range[1]), 2)
            if t > tmax:
                tmax = t
            y = round(random.randint(y_range[0], y_range[1]), 2)
            if y > uMax:
                uMax = y
            u = round(random.uniform(u_range[0], u_range[1]), 2)
            if u > valMax:
                valMax = u
            values.append((t,y,u))
            f.write(f"{t}\t{y}\t{u}\n")
        print(f"Rows Max: {tmax}, Col Max: {uMax}, Max Val: {valMax}")
        f.write(f"100\t100\t1\n")
    f.close()
    return maxRows, maxCols, values

# sparsity is the percentage of values we will fill for the spreadsheet.
def sparsity(x):
    return int(0.3*x)

def command(fileName, rows,cols,vals):
    #print("Rows: {rows}, Cols: {cols}")
    #print(vals)
    with open(fileName,'w') as f:
        f.write(f"R\n")
        f.write(f"C\n")
        #appending 10% of the rows and cols
        for x in range(int(rows*0.1)):
            f.write(f"AR\n")
        for x in range(int(cols*0.1)):
            f.write(f"AC\n")
        
        #finding values located in rows
        for x in vals:
            #print(x[2])
            f.write(f"F {x[2]}\n")
        
        f.write(f"R\n")
        f.write(f"C\n")

        #updating values in random places
        up = vals[random.randint(0,len(vals)-1): len(vals)-1]
        for x in up:
            f.write(f"U {x[0]} {x[1]} {x[2]}\n")
        f.write(f"E\n")

        #Inserting rows/columns at random points
        for x in range(int(rows*0.1)):
            OMG = random.randint(0,rows-1)
            f.write(f"IR {OMG}\n")
        for x in range(int(cols*0.1)):
            OMG = random.randint(0,cols-1)
            f.write(f"IC {OMG}\n")
        
        #printing the values in the rows and columns
        f.write(f"R\n")
        f.write(f"C\n")
        #printing non empty values
        f.write(f"E\n")
        f.close()



r,c,v = write_txt_file("tasty", 100, (0, 100), (0, 50), (0, 20))
command("commands.in", r,c,v)

def run():
    return os.system("python3 spreadsheetFilebased.py linkedlist tasty commands.in DataGen.txt")
run()
