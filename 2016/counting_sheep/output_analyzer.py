input_file_name = 'sheep.out'

f = open(input_file_name, 'r')
table = {}
for i in range(300000):
    line = f.readline()
    values = line.split()
    
    if values[2] != 'INSOMNIA':
        y = int(values[2])        
        if y not in table:
            table[y] = []
            table[y].append(i)
        else:
            table[y].append(i)

st = sorted(table, key=lambda key: table[key])
for k in st:
    print k, table[k]
