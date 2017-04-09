
input_file_name = 'A-large-practice.in'
output_file_name = 'A-large-practice.out'

f = open(input_file_name, 'r')
outFile = open(output_file_name, 'w', 0)

# get T, the number of test cases
T = f.readline()
T = int(T)

def allDigitsFound(digits):
    for d in digits:
        if d == 0:
            return False
    return True

for t in range(T):
    N = f.readline()
    N = N.strip()

    print 'N: {}'.format(N)
    digits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # fall asleep when see all ten digits
    # N, then 2N, then 3N, ...

    if int(N) == 0:
        product = 'INSOMNIA'  # multiply by zero always equals zero

    else:
        # naive approach:  keep increasing the multiplier..
        n = int(N)
        asleep = False
        for i in range(1, 100):
            product = n * i
            # print 'product: {}'.format(product)
            text = str(product)
            for char in text:
                value = int(char)
                count = digits[value]
                count+=1
                digits[value] = count
                # print digits

                # test for all numbers
                if allDigitsFound(digits):
                    print 'Fall asleep at {}'.format(product)
                    asleep = True
                    break
            if asleep:
                break


    output = 'Case #{}: {}'.format((t+1), product)
    print output
    outFile.write(output + "\n")