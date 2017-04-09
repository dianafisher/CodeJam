"""
Rank and File

T is number of test cases.

Each test case consists of one line with integer N.
Followed by 2N-1 lines of N integers each.

1 <= T <= 50
1 <= heights <= 2500

Small dataset
2 <= N <= 10

Large dataset
2 <= N <= 50
"""

input_file_name = 'B-small-attempt0.in'
output_file_name = 'B-file.out'

f = open(input_file_name, 'r')
outFile = open(output_file_name, 'w', 0)

# get T, the number of test cases
T = f.readline()
T = int(T)

for t in range(3):
    N = f.readline().strip()   
    N = int(N)
    # print N
    lines = []
    count = 2*N-1
    for n in range(count):
        line = f.readline().strip()
        # print 'line:', line
        values = [int(k) for k in line.split()]
        # print 'values:', values
        lines.append(values)

    # print lines
    # find lines that start with the same number to find the top left corner.
    # sort the list of pages
    s = sorted(lines)
    print 'sorted:', s
    elements = []
    for n in range (N):
        listofzeros = [0] * N
        elements.append(listofzeros)
    
    # place the first two lines in elements as a row and column
    col = 0
    for item in s[0]:
        elements[0][col] = item
        col += 1

    col = 0    
    row = 0
    for item in s[1]:
        elements[row][col] = item
        row += 1
        
    print 'elements', elements
    for i in range(2, N):
        line = s[i]
        first = line[0]
        print 'first', first
        # check if there is a column which starts with this value
        col = 0
        foundColumn = False
        for n in elements[0]:            
            if n == first:
                # make sure the column is not already taken
                if elements[1][col] == 0:
                    print 'found match at column %d' % col
                    foundColumn = True
                    break
            col += 1
        if foundColumn:
            # place the items in the column
            row = 0
            for item in line:
                elements[row][col] = item
                row += 1
            print 'elements', elements
        else:
            # look for a row to place the list in
            row = 0            
            foundRow = False
            for n in elements[row]:
                print 'n', n
                if n == first:
                    print 'found match at row %d' % row
                    break
                row += 1


    # row = 0    
    # isRow = True    
    # for values in s:
    #     # values = [int(k) for k in line.split()]
    #     # print 'values', values
        
    #     for v in values:                       
    #         if isRow:
    #             elements[row].append(v)
    #             # print elements        
    #     if isRow:
    #         row += 1
    #         isRow = False
    #     else:
    #         isRow = True

    # # print elements
    # for row in elements:
    #     print row

    # # the missing page will be the last column in the matrix.
    output = ''
    # for n in range(N):
    #     output += str(elements[n][N-1])
    #     if n < N-1:
    #         output += " "
    
    
    print 'Case #%d:' % (t+1), output
    outFile.write('Case #' + str(t+1) + ": " + output + "\n") 
