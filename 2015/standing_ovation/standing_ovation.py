# shyness level S
# Each audience member has shyness level of Si.
# An audience member will wait until at least Si other people are standing
# If Si == 0, audience member always stands and clpas immediately regardless of what anyone else does.

# What is the minimum number of friends you need to invite?

# T = number of test cases
# Each test case has one line with Smax, followed by a string of Smax + 1 digits
# The kth digit of the string represents how many people have shyness level k

# There will always be at least one person in the audience.

# read input file
input_file_name = 'A-large-practice.in'
output_file_name = 'A-large-practice.out'

f = open(input_file_name, 'r')
outFile = open(output_file_name, 'w')

# get T, the number of test cases
T = f.readline()
T = int(T)

# read T lines
for x in range(T):
    line = f.readline()
    Smax, kstr = line.split()

    y = 0  # y is the number of friends to invite
    standing = 0
    for k in range(int(Smax) + 1):
        y = max(y, k - standing)
        n = int(kstr[k])
        standing += n
    case = x+1
    print ('Case #%d:' % case, y)
    outFile.write('Case #' + str(case) + ': ' + str(y) + "\n")
