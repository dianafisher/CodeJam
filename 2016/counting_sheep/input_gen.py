output_file_name = 'large_sheep_input.txt'
outFile = open(output_file_name, 'w', 0)

maximum = 1000001
for x in range(maximum):
    print x
    outFile.write(str(x) + "\n")