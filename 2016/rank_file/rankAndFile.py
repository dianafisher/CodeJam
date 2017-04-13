"""
Problem

When Sergeant Argus's army assembles for drilling, they stand in the shape of
an N by N square grid, with exactly one soldier in each cell. Each soldier has
a certain height.

Argus believes that it is important to keep an eye on all of his soldiers at
all times.  Since he likes to look at the grid from the upper left,
he requires that:

Within every row of the grid, the soldiers' heights must be in strictly
increasing order, from left to right.
Within every column of the grid, the soldiers' heights must be in strictly
increasing order, from top to bottom.
Although no two soldiers in the same row or column may have the same height,
it is possible for multiple soldiers in the grid to have the same height.

Since soldiers sometimes train separately with their row or their column,
Argus has asked you to make a report consisting of 2*N lists of the soldiers'
heights: one representing each row (in left-to-right order) and column
(in top-to-bottom order). As you surveyed the soldiers, you only had small
pieces of paper to write on, so you wrote each list on a separate piece of
paper. However, on your way back to your office, you were startled by a
loud bugle blast and you dropped all of the pieces of paper, and the wind blew
one away before you could recover it!
The other pieces of paper are now in no particular order, and you can't even
remember which lists represent rows and which represent columns,
since you didn't write that down.

You know that Argus will make you do hundreds of push-ups if you
give him an incomplete report.

Can you figure out what the missing list is?

Input

The first line of the input gives the number of test cases, T. T test cases
follow.  Each consists of one line with an integer N, followed by 2*N-1 lines
of N integers each, representing the lists you have, as described in the
statement. It is guaranteed that these lists represent all but one of the rows
and columns from a valid grid, as described in the statement.

Output

For each test case, output one line containing Case #x: y, where x is the
test case number starting from 1) and y is a list of N integers in strictly
increasing order, representing the missing list.

Limits

1 <= T <= 50

1 <= all heights <= 2500
The integers on each line will be in strictly increasing order.
It is guaranteed that a unique valid answer exists.

Small dataset
2 <= N <= 10

Large dataset
2 <= N <= 50
"""

input_file_name = 'B-large-practice.in'
output_file_name = 'B-large-practice.out'

f = open(input_file_name, 'r')
outFile = open(output_file_name, 'w')

# get T, the number of test cases
T = f.readline()
T = int(T)
print ('T = {}'.format(T))

for t in range(T):
    N = f.readline()
    N = int(N)
    print ('N = {}'.format(N))
    numLines = 2*N-1
    frequencies = {}
    for x in range(numLines):
        line = f.readline()
        arr = [int(s) for s in line.split()]
        print (arr)
        for y in range(N):
            value = arr[y]
            if value in frequencies:
                frequencies[value]+=1
            else:
                frequencies[value] = 1

    print (frequencies)

    # find the entries which have odd frequency count
    result = []

    for x in frequencies.keys():
        if frequencies[x] % 2 is not 0:
            result.append(x)

    result = sorted(result)

    text =  (' '.join(str(x) for x in result))
    # print text
    output = 'Case #{}: {}'.format((t+1), text)
    print (output)
    outFile.write(output + "\n")
