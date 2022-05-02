import json
import numpy as np

def rotatez(coords):
    theta = np.deg2rad(360 - np.rad2deg(np.arctan2(coords[2, 1], coords[2, 0])) + 180)
    rotmatz = np.asarray([[np.cos(theta), -np.sin(theta), 0], [np.sin(theta), np.cos(theta), 0], [0, 0, 1]])
    for idx, vector in enumerate(coords):
        vector = vector[np.newaxis, :]
        vector = vector.T
        rotated: np.ndarray = (rotmatz @ vector).T
        coords[idx][:] = rotated
    return coords

def rotatey(coords):
    theta = np.arctan2(coords[2, 2], coords[2, 0])
    rotmaty = np.asarray([[np.cos(theta), 0, np.sin(theta)],[0, 1, 0],[-np.sin(theta), 0, np.cos(theta)]])
    for idx, vector in enumerate(coords):
        vector = vector[np.newaxis, :]
        vector = vector.T
        rotated: np.ndarray = (rotmaty @ vector).T
        coords[idx][:] = rotated
    return coords

def rotatex(coords):
    theta = np.deg2rad((360 - (np.rad2deg(np.arctan2(coords[1, 2], coords[1, 1])) + 180)) + 90)
    rotmatx = np.asarray([[1, 0, 0],[0, np.cos(theta), -np.sin(theta)],[0, np.sin(theta), np.cos(theta)]])
    for idx, vector in enumerate(coords):
        vector = vector[np.newaxis, :]
        vector = vector.T
        rotated: np.ndarray = (rotmatx @ vector).T
        coords[idx][:] = rotated
    return coords

def processAminos():
    with open("aminos.json", 'r') as j:
        test = json.loads(j.read())

    # Read in aminos coordinates from json file

    ala = np.reshape(np.asarray(test["ALA"]), [len(test["ALA"])//3, 3])
    arg = np.reshape(np.asarray(test["ARG"]), [len(test["ARG"])//3, 3])
    asn = np.reshape(np.asarray(test["ASN"]), [len(test["ASN"])//3, 3])
    asp = np.reshape(np.asarray(test["ASP"]), [len(test["ASP"])//3, 3])
    cys = np.reshape(np.asarray(test["CYS"]), [len(test["CYS"])//3, 3])
    gln = np.reshape(np.asarray(test["GLN"]), [len(test["GLN"])//3, 3])
    glu = np.reshape(np.asarray(test["GLU"]), [len(test["GLU"])//3, 3])
    gly = np.reshape(np.asarray(test["GLY"]), [len(test["GLY"])//3, 3])
    his = np.reshape(np.asarray(test["HIS"]), [len(test["HIS"])//3, 3])
    ile = np.reshape(np.asarray(test["ILE"]), [len(test["ILE"])//3, 3])
    lys = np.reshape(np.asarray(test["LYS"]), [len(test["LYS"])//3, 3])
    met = np.reshape(np.asarray(test["MET"]), [len(test["MET"])//3, 3])
    phe = np.reshape(np.asarray(test["PHE"]), [len(test["PHE"])//3, 3])
    pro = np.reshape(np.asarray(test["PRO"]), [len(test["PRO"])//3, 3])
    ser = np.reshape(np.asarray(test["SER"]), [len(test["SER"])//3, 3])
    thr = np.reshape(np.asarray(test["THR"]), [len(test["THR"])//3, 3])
    trp = np.reshape(np.asarray(test["TRP"]), [len(test["TRP"])//3, 3])
    tyr = np.reshape(np.asarray(test["TYR"]), [len(test["TYR"])//3, 3])
    val = np.reshape(np.asarray(test["VAL"]), [len(test["VAL"])//3, 3])
    leu = np.reshape(np.asarray(test["LEU"]), [len(test["LEU"])//3, 3])


    # Process amino acid coordinates
    # First translate aminos to 0,0. Then rotate in y and z so they are aligned on the same axis.

    ala = rotatex(rotatey(rotatez(ala-ala[0][:])))
    arg = rotatex(rotatey(rotatez(arg-arg[0][:])))
    asn = rotatex(rotatey(rotatez(asn-asn[0][:])))
    asp = rotatex(rotatey(rotatez(asp-asp[0][:])))
    cys = rotatex(rotatey(rotatez(cys-ala[0][:])))
    gln = rotatex(rotatey(rotatez(gln-gln[0][:])))
    glu = rotatex(rotatey(rotatez(glu-glu[0][:])))
    gly = rotatex(rotatey(rotatez(gly-ala[0][:])))
    his = rotatex(rotatey(rotatez(his-his[0][:])))
    ile = rotatex(rotatey(rotatez(ile-ile[0][:])))
    lys = rotatex(rotatey(rotatez(lys-lys[0][:])))
    met = rotatex(rotatey(rotatez(met-met[0][:])))
    phe = rotatex(rotatey(rotatez(phe-phe[0][:])))
    pro = rotatex(rotatey(rotatez(pro-pro[0][:])))
    ser = rotatex(rotatey(rotatez(ser-ser[0][:])))
    thr = rotatex(rotatey(rotatez(thr-thr[0][:])))
    trp = rotatex(rotatey(rotatez(trp-trp[0][:])))
    tyr = rotatex(rotatey(rotatez(tyr-tyr[0][:])))
    val = rotatex(rotatey(rotatez(val-val[0][:])))
    leu = rotatex(rotatey(rotatez(leu-leu[0][:])))

    aminos = {'A': ala, 'R': arg, 'N': asn, 'D': asp, 'C': cys, 'Q': gln, 'E': glu, 'G': gly,'H': his,'I': ile, 'K': lys, 'M': met, 'F': phe, 'P': pro,
        'S': ser, 'T': thr, 'W': trp, 'Y': tyr, 'V': val, 'L': leu}

    return aminos


if __name__ == "__main__":
    aminos = processAminos()


