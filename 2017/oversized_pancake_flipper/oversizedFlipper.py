input_file_name = 'A-small-practice.in'
output_file_name = 'A-small-10.out'

f = open(input_file_name, 'r')
outFile = open(output_file_name, 'w', 0)

# get T, the number of test cases
T = f.readline()
T = int(T)

for t in range(10):
    line = f.readline()
    parts = line.split()
    S = parts[0]
    K = int(parts[1])
    print 'S: {}, K:{}'.format(S, K)
    # convert to boolean values (+ is True)
    s = [c == '+' for c in S]
    print 'original stack: {}'.format(s)
    flips = 0
    count = len(s)
    for p in range(count - K + 1):
        if not s[p]:
            print 'flip at index {}'.format(p)
            flips += 1
            for j in range(p, p+K):
                s[j] = not s[j]
            print s
    if all(s):
        output = 'Case #{}: {}'.format(t+1, flips)
    else:
        output = 'Case #{}: IMPOSSIBLE'.format(t+1)
    print output
    outFile.write(output + "\n")