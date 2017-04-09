"""
Fractiles

T is number of test cases
Each line contains K, C, and S

K = number of tiles in original
C = complexity number
S = peon count

Solution Notes:

Let us call the original sequence O, and let Ai be the artwork of complexity i for a fixed O.

We have seen that position 1 of any Ai is always equal to position 1 of O.

Consider position 2 of O as an example. It is position 2 in A1 = O. 
When A2 is produced from A1, the tile at position 2 of A1 determines which tiles 
will appear at positions K + 1 through K + K of A2. In particular, the second of 
those tiles, the tile at position K + 2 of A2, is the same as the tile at position 2 of A1. 
Then, it follows that position K + 2 of A2 generates positions K*(K + 2 - 1) + 1 through K*(K + 2) of A3, 
and the second of those tiles, at position K*(K + 2 - 1) + 2 of A3, is also a copy of position 2 of O. 
You can follow this further to discover which position of AC is equal to position 2, or you can write a 
program to do it for you. Similarly, for each position of O there is exactly one "fixed point" position 
in AC that is always equal in value, and you can get those with a program by generalizing the procedure 
described for position 2. If you check out all of those positions, you obtain a different result for 
every possible O, which makes the solution valid.

"""

import math
import itertools

input_file_name = 'D-small.in'
output_file_name = 'D_small.out'

f = open(input_file_name, 'r')
outFile = open(output_file_name, 'w', 0)

# get T, the number of test cases
T = f.readline()
T = int(T)

# Solution as listed in Code Jam anaylsis.
def Solve(k, c, s):
  if c*s > k:
    return []  # returns an empty list for impossible cases
  tiles = []
  # the list for the last tile choice is filled with copies of k
  # i is the first value of the list of the current tile choice
  for i in xrange(1, k + 1, c):
    p = 1
    # j is the step in the current list [i, i+1, ..., i+C-1]
    for j in xrange(c):
      # the min fills the last tile choice's list with copies of k
      p = (p - 1) * k + min(i + j, k)
    tiles.append(p)
  return tiles

for t in range(T):
    line = f.readline()
    values = line.split()
    K = int(values[0])
    C = int(values[1])
    S = int(values[2])

    print 'K = %d' % K, 'C = %d' % C, 'S = %d' % S

    tile_count = math.pow(K, C)
    print 'tile_count = %d' % tile_count

    possibilities_count = math.pow(2, K)
    print 'possibilities_count = %d' % possibilities_count

    # sequences = ["".join(seq) for seq in itertools.product("LG", repeat=K)]
    # print sequences

    # for K = 2, C = 2, need S = 1, look at index 2
    # for K = 3, C = 2, need S = 2, look at index 3 and 6
    # for K = 4, C = 2, need S = 3, look at index 4, 8 and 12

    # for each C, need (K-1) tiles to look at
    

    

