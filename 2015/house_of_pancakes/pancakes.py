

"""
At the Infinite House of Pancakes, there are only finitely many pancakes, 
but there are infinitely many diners who would be willing to eat them! 
When the restaurant opens for breakfast, among the infinitely many diners, 
exactly D have non-empty plates; the ith of these has Pi pancakes on his 
or her plate. Everyone else has an empty plate.

Normally, every minute, every diner with a non-empty plate will eat one 
pancake from his or her plate. However, some minutes may be special. 
In a special minute, the head server asks for the diners' attention, 
chooses a diner with a non-empty plate, and carefully lifts some number 
of pancakes off of that diner's plate and moves those pancakes onto one 
other diner's (empty or non-empty) plate. No diners eat during a special 
minute, because it would be rude.

You are the head server on duty this morning, and it is your job to decide 
which minutes, if any, will be special, and which pancakes will move where. 
That is, every minute, you can decide to either do nothing and let the diners 
eat, or declare a special minute and interrupt the diners to make a single 
movement of one or more pancakes, as described above.

Breakfast ends when there are no more pancakes left to eat.
How quickly can you make that happen?

The first line of the input gives the number of test cases, T. 
T test cases follow. Each consists of one line with D, the number of 
diners with non-empty plates, followed by another line with D space-separated 
integers representing the numbers of pancakes on those diners' plates.

"""

input_file_name = 'pancakes_input.txt'
output_file_name = 'pancakes_output.txt'

f = open(input_file_name, 'r')
outFile = open(output_file_name, 'w', 0)

# get T, the number of test cases
T = f.readline()
T = int(T)

for x in range(T):
    D = f.readline()  # D is the number of diners with non-empty plates
    D = int(D)
    line = f.readline()
    plates = line.split()
    print 'plates', plates
    print D, line

    counts = [0] * 1005
    
    for p in plates:
        num = int(p)
        value = counts[num]
        counts[num] = value+1
    
    print counts 

    # y is the smallest number of minutes needed to finish breakfast (when pancake count = 0)
    y = 10000

    for x in range(1, 1005):
        moves = 0
        for i in range(1005):
            moves += ((i-1)/x) * counts[i]

        if (moves + x < y):
            y = (moves + x)            

    print 'y = %d' % y
    