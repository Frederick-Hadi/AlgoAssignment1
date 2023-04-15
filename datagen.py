import random

def write_txt_file(filename, x, t_range, y_range, u_range):
    # x is the number of rows in the file
    # t_range is the range of values for t,T acts as the row
    # y_range is the range of values for y, Y acts as the column
    # u_range is the range of values for u, U acts as the value
    with open(filename, 'w') as f:
        tmax = 0
        uMax = 0
        valMax = 0
        x = sparsity(x)
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
            f.write(f"{t}\t{y}\t{u}\n")
        print(f"Rows Max: {tmax}, Col Max: {uMax}, Max Val: {valMax}")
        f.write(f"100\t100\t1\n")

# sparsity is the percentage of values we will fill for the spreadsheet.
def sparsity(x):
    return int(0.3*x)

write_txt_file("tasty", 100, (0, 100), (0, 50), (0, 20))
