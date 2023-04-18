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
        # 0.3 would be percentage
        x = sparsity(r*c,0.3)
        values = []

        #generating random values in random rows and cols
        for i in range(x):
            t = round(random.randint(rowRange[0], rowRange[1]), 2)
            if t > tmax:
                tmax = t
            y = round(random.randint(colRange[0], colRange[1]), 2)
            if y > uMax:
                uMax = y
            u = round(random.uniform(u_range[0], u_range[1])*10, 3)
            if u > valMax:
                valMax = u
            values.append((t,y,u))
            f.write(f"{t}\t{y}\t{u}\n")
        #to know where the values are located
        #print(f"Rows Max: {tmax}, Col Max: {uMax}, Max Val: {valMax}")
        f.write(f"{maxRows}\t{maxCols}\t1\n")
    f.close()
    return maxRows, maxCols, values

# sparsity is the percentage of values we will fill for the spreadsheet.
def sparsity(x,y):
    return int(y*x)

def command1(fileName, rows,cols,vals,size):
    
    with open("commands.in", "w") as f:
            #yucky
        for command in listOfCommands:
            if command not in ("F", "U", "IR", "IC"):
                f.write(command)
            if command == "F":
                f.write(f"{command} {vals[random.randint(0,len(vals)-1)][2]}\n")
            if command == "U":
                f.write(f"{command} {vals[random.randint(0,len(vals)-1)][0]} {vals[random.randint(0,len(vals)-1)][1]} {vals[random.randint(0,len(vals)-1)][2]}\n")
            if command == "IR":
                f.write(f"{command} {random.randint(0,size)}\n")
            if command == "IC":
                f.write(f"{command} {random.randint(0,size)}\n") 
        f.close()
#TODO change sizes?
#databaseSizes = [(5,8),(10,7),(50,70),(100,50),(500,70),(1000,1000)]

listOfCommands = ["R\n", "C\n", "AR\n", "AC\n", "F", "U", "IR", "IC", "E\n"]

databaseSizes = [5,10,50,100,250,500]

#holds the randomly generated databases
databaseNames = ["Saber", "Lancer", "Archer", "Rider", "Assassin", "Berserker"]

#hold the results of if the commands worked or not
resultNames = ["Shirou","Kiritsugu","Rin","Sakura","Kirei","Illya"]

#straight forward
databaseTypes = ["csr", "linkedlist", "array"]

#holds the times in the order of databaseTypes
overall = ["enuma.txt","excalibur.txt","gae.txt"]

for i in range (3):
        with open(overall[i], "w") as f:
            f.write(f"Time for {databaseTypes[i]}:\n")
            f.write("_______________________________________________________________\n")
            f.close()
        for x in range(6):
            #r,c,v = write_txt_file(databaseNames[x], databaseSizes[x][0], databaseSizes[x][1],(-20, 20))
            r,c,v = write_txt_file(databaseNames[x], databaseSizes[x], databaseSizes[x],(-20, 20))
            command1("commands.in", r,c,v,databaseSizes[x])
            os.system("python3 spreadsheetFilebased.py " + databaseTypes[i] + " " + databaseNames[x] + " commands.in " + resultNames[x] + ".txt")
            with open(overall[i], "a") as f:
                f.write(f"_____________________________________________________________________________\n")
                f.close()
        print("done with " + databaseTypes[i])

