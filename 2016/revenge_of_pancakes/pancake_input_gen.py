from random import randint

output_file_name = 'large_pancakes_input.txt'
outFile = open(output_file_name, 'w', 0)

# 100 strings of 100 length
size = 100
for x in range(100):
    pancakes = []
    for y in range(100):    
        p = randint(0,1)        
        if (p):
            pancakes.append('+')
        else:
            pancakes.append('-')

    pancakeStr = ''.join(str(d) for d in pancakes) 
    outFile.write(pancakeStr + "\n")