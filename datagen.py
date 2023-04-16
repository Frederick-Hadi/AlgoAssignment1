import random
import os
import time
# python3 spreadsheetFilebased.py linkedlist tasty commands.in DataGen.txt
def write_txt_file(filename, r,c, u_range):
    
   
    with open(filename, 'w') as f:
        tmax = 0
        uMax = 0
        valMax = 0

        maxRows = r
        maxCols = c
        rowRange = (0,maxRows)
        colRange = (0,maxCols)

        x = sparsity(r)
        values = []

        #generating random values in random rows and cols
        for i in range(x):
            t = round(random.randint(rowRange[0], rowRange[1]), 2)
            if t > tmax:
                tmax = t
            y = round(random.randint(colRange[0], colRange[1]), 2)
            if y > uMax:
                uMax = y
            u = round(random.uniform(u_range[0], u_range[1]), 2)
            if u > valMax:
                valMax = u
            values.append((t,y,u))
            f.write(f"{t}\t{y}\t{u}\n")
        #to know where the values are located
        print(f"Rows Max: {tmax}, Col Max: {uMax}, Max Val: {valMax}")
        f.write(f"{maxRows}\t{maxCols}\t1\n")
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

#i think we are meant to test features one at a time and see the effect it has on performance one at a time.
def command1():
    with open("commands.in", 'w') as f:
        f.write(f"R\n")
        f.write(f"C\n")
        f.write(f"AR\n")
        f.write(f"AC\n")
        f.write(f"F 5\n")
        f.write(f"U 2 2 5\n")
        f.write(f"IR 2\n")
        f.write(f"IC 2\n")
        f.write(f"E\n")
        f.close()

#TODO change sizes?
#databaseSizes = [(5,8),(10,7),(50,70),(100,50),(500,70),(1000,1000)]
databaseSizes = [5,10,50,100,250,500]

#holds the randomly generated databases
databaseNames = ["Saber", "Lancer", "Archer", "Rider", "Assassin", "Berserker"]

#hold the results of if the commands worked or not
resultNames = ["Shirou","Kiritsugu","Rin","Sakura","Kirei","Illya"]

#straight forward
databaseTypes = ["csr", "linkedlist", "array"]

#holds the times in the order of databaseTypes
overall = ["enuma","excalibur","gae"]


             
for i in range (3):
    with open(overall[i], "w") as f:
        f.write(f"___________________________________________________________\n")
        for x in range(6):
            #r,c,v = write_txt_file(databaseNames[x], databaseSizes[x][0], databaseSizes[x][1],(-20, 20))
            r,c,v = write_txt_file(databaseNames[x], databaseSizes[x], databaseSizes[x],(-20, 20))
            command("commands.in", r,c,v)
            start_time = time.perf_counter()
            os.system("python3 spreadsheetFilebased.py " + databaseTypes[i] + " " + databaseNames[x] + " commands.in " + resultNames[x] + ".txt")
            end_time = time.perf_counter()
            elapsed_time = end_time - start_time
            f.write(f"Iteration {x}: Elapsed time: {elapsed_time} seconds\n")
        f.write(f"___________________________________________________________\n")
        print("done with " + databaseTypes[i])
        f.close()
