row_size = int(input("Enter the size of the pattern:"))
row = 0
while row < row_size:
    for n in range(row_size):
        print ("*", end ="")        
    print()
    row += 1