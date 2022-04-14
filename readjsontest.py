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
    theta = np.arctan2(coords[2, 2], coords[2, 0]);
    rotmaty = np.asarray([[np.cos(theta), 0, np.sin(theta)],[0, 1, 0],[-np.sin(theta), 0, np.cos(theta)]])
    for idx, vector in enumerate(coords):
        vector = vector[np.newaxis, :]
        vector = vector.T
        rotated: np.ndarray = (rotmaty @ vector).T
        coords[idx][:] = rotated
    return coords


with open("aminos.json", 'r') as j:
    test = json.loads(j.read())

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

ala = ala-ala[0][:]
arg = arg-arg[0][:]
asn = asn-asn[0][:]
asp = asp-asp[0][:]
cys = cys-ala[0][:]
gln = gln-gln[0][:]
glu = glu-glu[0][:]
gly = gly-ala[0][:]
his = his-his[0][:]
ile = ile-ile[0][:]
lys = lys-lys[0][:]
met = met-met[0][:]
phe = phe-phe[0][:]
pro = pro-pro[0][:]
ser = ser-ser[0][:]
thr = thr-thr[0][:]
trp = trp-trp[0][:]
tyr = tyr-tyr[0][:]
val = val-val[0][:]

print(ala)
print(rotatey(rotatez(ala)))



