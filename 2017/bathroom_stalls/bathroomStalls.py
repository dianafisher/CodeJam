"""
Problem

A certain bathroom has N + 2 stalls in a single row; the stalls on the left and right ends
are permanently occupied by the bathroom guards. The other N stalls are for users.

Whenever someone enters the bathroom, they try to choose a stall that is as far from other
people as possible. To avoid confusion, they follow deterministic rules:
For each empty stall S, they compute two values LS and RS, each of which is the number of
empty stalls between S and the closest occupied stall to the left or right, respectively.
Then they consider the set of stalls with the farthest closest neighbor, that is, those S
for which min(LS, RS) is maximal. If there is only one such stall, they choose it; otherwise,
they choose the one among those where max(LS, RS) is maximal.
If there are still multiple tied stalls, they choose the leftmost stall among those.

K people are about to enter the bathroom; each one will choose their stall before the next arrives.
Nobody will ever leave.

When the last person chooses their stall S, what will be the values of max(LS, RS) and min(LS, RS) be?

Solving this problem

This problem has 2 Small datasets and 1 Large dataset. You must solve the first Small dataset
before you can attempt the second Small dataset. You will be able to retry either of the Small
datasets (with a time penalty). You will be able to make a single attempt at the Large,
as usual, only after solving both Small datasets.

Input

The first line of the input gives the number of test cases, T. T lines follow.
Each line describes a test case with two integers N and K, as described above.

Output

For each test case, output one line containing Case #x: y z, where x is the test case number (starting from 1),
y is max(LS, RS), and z is min(LS, RS) as calculated by the last person to enter the bathroom for their chosen stall S.

Limits

1 <= T <= 100.
1 <= K <= N.
Small dataset 1

1 <= N <= 1000.

Input

5
4 2
5 2
6 2
1000 1000
1000 1


Output

Case #1: 1 0
Case #2: 1 0
Case #3: 1 1
Case #4: 0 0
Case #5: 500 499

"""
from math import floor
from collections import deque, defaultdict
import heapq

input_file_name = 'C-large-practice.in'
output_file_name = 'C-large-practice.out'

# input_file_name = 'C-small-test.in'
# output_file_name = 'C-small-test.out'


f = open(input_file_name, 'r')
outFile = open(output_file_name, 'w')

# get T, the number of test cases
T = f.readline()
T = int(T)
for t in range(T):
    print ('---------------------')
    line = f.readline()
    N, K = line.split()
    K = int(K)
    N = int(N)
    print('N: {}, K: {}'.format(N, K))

    gap_counts = {N:1}
    queue = [-N]

    while True:
        print('gap_counts', gap_counts)
        print('queue', queue)
        # pop off the biggest gap
        gapSize = -heapq.heappop(queue)
        print('gapSize', gapSize)
        gapCount = gap_counts[gapSize]
        print('gapCount', gapCount)
        del gap_counts[gapSize]
        if K <= gapCount:
            output = 'Case #{}: {} {}'.format(t+1, gapSize // 2, (gapSize-1) // 2)
            print(output)
            outFile.write(output + "\n")
            break
        else:
            K -= gapCount
            left = (gapSize-1) // 2
            right = gapSize // 2
            print('left: {}, right: {}'.format(left, right))
            for g in [left, right]:
                if g not in gap_counts:
                    gap_counts[g] = 0
                    heapq.heappush(queue, -g)
                gap_counts[g] += gapCount
