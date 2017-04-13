"""
You are a teacher at the brand new Little Coders kindergarten.
You have N kids in your class, and each one has a different student
ID number from 1 through N. Every kid in your class has a single best
friend forever (BFF), and you know who that BFF is for each kid.

BFFs are not necessarily reciprocal -- that is, B being A's BFF
does not imply that A is B's BFF.

Your lesson plan for tomorrow includes an activity in which the participants
must sit in a circle. You want to make the activity as successful as possible
by building the largest possible circle of kids such that each kid in the
circle is sitting directly next to their BFF, either to the left or to the
right. Any kids not in the circle will watch the activity without
participating.

What is the greatest number of kids that can be in the circle?

"""

input_file_name = 'C-sample.in'
output_file_name = 'C-sample.out'

f = open(input_file_name, 'r')
outFile = open(output_file_name, 'w')

# get T, the number of test cases
T = f.readline()
T = int(T)

for t in range(T):
    # each test case consists of two lines
    N = f.readline()
    N = int(N) # N is the total number of kids in the class
    print('N: {}'.format(N))
    line = f.readline() # N integers F1, F2, .. FN
    ids = line.split()
    print('ids: {}'.format(ids))
    for s in range(N):
        bff = ids[s]
        print ('student {} bff is {}'.format(s+1, bff))
