

def generateSequence(path):
    sequence = []

    aminos = {'MET': 'M', 'VAL': 'V', 'ALA': 'A', 'LEU': 'L', 'SER': 'S', 'LYS': 'K', 'ILE': 'I', 'GLY': 'G',
              'ASN': 'N', 'ASP': 'D', 'CYS': 'C', 'GLU': 'E', 'GLN': 'Q', 'HIS': 'H', 'PHE': 'F', 'PRO': 'P',
              'THR': 'T', 'TRP': 'W', 'TYR': 'Y', 'ARG': 'R'}

    with open(path) as inputpdb:
        data = inputpdb.readlines()
        for line in data:
            line = line.split()
            if line[0] == 'SEQRES':
                for entry in line[4:]:
                    sequence.append(aminos[entry])
    print("".join(s for s in sequence))
    return sequence

if __name__ == '__main__':
    path = '/Users/sbarnett/Documents/MATLAB/lineariseProtein/humantalin1-AF-Q9Y490-F1-model_v2.pdb'
    sequence = generateSequence(path)

