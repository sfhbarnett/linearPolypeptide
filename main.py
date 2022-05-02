
from generateSequence import generateSequence
from processAminos import processAminos
from generatePeptide import generatePeptide

path = '/Users/sbarnett/Documents/MATLAB/lineariseProtein/humantalin1-AF-Q9Y490-F1-model_v2.pdb'

sequence = generateSequence(path) # get primary sequence from PDB
aminos = processAminos() # Load in amino JSON and correct the position/rotation
d = generatePeptide(sequence, aminos) # Create linear form of protein

f = open(path).readlines()

# inputdata = open('/Users/sbarnett/Documents/MATLAB/lineariseProtein/test3.csv').readlines()
# d = []
# for line in inputdata:
#     line = line.strip('\n').split(',')
#     d.append(line)


output = []
counter = 0
for count, line in enumerate(f):
    if(line[0:4]) != 'ATOM':
        output.append(line)
    else:
        if counter < len(d):
            atom = line.split()
            if len(atom) == 11:
                newline = atom[0:4]
                middle = atom[4]
                newline.append(middle[0])
                newline.append(middle[1:])
                newline = newline + atom[5:]
                atom = newline
            coords = d[counter]
            atom[6] = coords[0]
            atom[7] = coords[1]
            atom[8] = coords[2]
            output.append(atom)
            counter += 1
        else:
            pass

outfilepath = '/Users/sbarnett/Documents/MATLAB/lineariseProtein/out2.pdb'
with open(outfilepath, 'w') as outfile:
    for line in output:
        if line[0] == 'ATOM':
            string = 'ATOM  '
            l = len(line[1])
            pad = 5-l
            string += ' ' * pad + line[1] + '  '
            l = len(line[2])
            pad = 3-l
            string += line[2]+' ' * pad + ' ' + line[3] + ' A'
            l = len(line[5])
            pad = 4 - l
            string += ' ' * pad + line[5]
            l = len(line[6])
            pad = 12-l
            string += ' ' * pad + line[6]
            l = len(line[7])
            pad = 8-l
            string += ' ' * pad + line[7]
            l = len(line[8])
            pad = 8-l
            string += ' ' * pad + line[8] + '  1.00 ' + line[10] + '           ' + line[11] + '  ' + '\n'
            outfile.write(string)
            print(string)
        else:
            print(line)
            outfile.write(line)