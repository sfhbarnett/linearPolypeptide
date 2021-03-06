import numpy as np
import copy
from linearPolypeptide.processAminos import processAminos


def generatePeptide(sequence,aminos):
    string = []
    starting = [0, 0, 0]
    theta = 90 - 123 / 2
    opposite = 1.32 * np.arcsin(np.deg2rad(theta))
    adjacent = 1.32 * np.arccos(np.deg2rad(theta))

    for el in range(len(sequence)):
        letter = sequence[el]
        amino = aminos[letter]
        coords = np.copy(amino)
        if opposite < 0:
            theta = np.deg2rad(180)
            rotmatx = [[1, 0, 0], [0, np.cos(theta), -np.sin(theta)], [0, np.sin(theta), np.cos(theta)]]
            for idx, vector in enumerate(coords):
                vector = vector[np.newaxis, :]
                vector = vector.T
                rotated: np.ndarray = (rotmatx @ vector).T
                coords[idx][:] = rotated
        position = coords + np.array([adjacent, 0, opposite]) + np.array(starting)
        opposite *= -1
        starting = position[2][:]
        string.append(position)

    theta = np.deg2rad(125)
    rotmatx = np.asarray([[1, 0, 0], [0, np.cos(theta), -np.sin(theta)], [0, np.sin(theta), np.cos(theta)]])
    endpointc = position[2, :]
    endpointo = position[4, :]
    trans = endpointo - endpointc
    rotated = rotmatx @ trans  # I don't think this is right yet, need to rotate the C also?
    newo = endpointc + rotated
    string.append([newo])
    output = []
    for aa in string:
        for el in aa:
            output.append(['{:.3f}'.format(coord) for coord in el.tolist()])
    return output




if __name__ == "__main__":
    sequence = 'MVALSLKISIGNVVKTMQFEPSTMVYDACRIIRERIPEAPAGPPSDFGLFLSDDDPKKGIWLEAGKALDYYMLRNGDTMEYRKKQRPLKIRMLDGTVKTIMVDDSKTVTDMLMTICARIGITNHDEYSLVRELMEEKKEEITGTLRKDKTLLRDEKKMEKLKQKLHTDDELNWLDHGRTLREQGVEEHETLLLRRKFFYSDQNVDSRDPVQLNLLYVQARDDILNGSHPVSFDKACEFAGFQCQIQFGPHNEQKHKAGFLDLKDFLPKEYVKQKGERKIFQAHKNCGQMSEIEAKVRYVKLARSLKTYGVSFFLVKEKMKGKNKLVPRLLGITKECVMRVDEKTKEVIQEWNLTNIKRWAASPKSFTLDFGDYQDGYYSVQTTEGEQIAQLIAGYIDIILKKKKSKDHFGLEGDEESTMLEDSVSPKKSTVLQQQYNRVGKVEHGSVALPAIMRSGASGPENFQVGSMPPAQQQITSGQMHRGHMPPLTSAQQALTGTINSSMQAVQAAQATLDDFDTLPPLGQDAASKAWRKNKMDESKHEIHSQVDAITAGTASVVNLTAGDPAETDYTAVGCAVTTISSNLTEMSRGVKLLAALLEDEGGSGRPLLQAAKGLAGAVSELLRSAQPASAEPRQNLLQAAGNVGQASGELLQQIGESDTDPHFQDALMQLAKAVASAAAALVLKAKSVAQRTEDSGLQTQVIAAATQCALSTSQLVACTKVVAPTISSPVCQEQLVEAGRLVAKAVEGCVSASQAATEDGQLLRGVGAAATAVTQALNELLQHVKAHATGAGPAGRYDQATDTILTVTENIFSSMGDAGEMVRQARILAQATSDLVNAIKADAEGESDLENSRKLLSAAKILADATAKMVEAAKGAAAHPDSEEQQQRLREAAEGLRMATNAAAQNAIKKKLVQRLEHAAKQAAASATQTIAAAQHAASTPKASAGPQPLLVQSCKAVAEQIPLLVQGVRGSQAQPDSPSAQLALIAASQSFLQPGGKMVAAAKASVPTIQDQASAMQLSQCAKNLGTALAELRTAAQKAQEACGPLEMDSALSVVQNLEKDLQEVKAAARDGKLKPLPGETMEKCTQDLGNSTKAVSSAIAQLLGEVAQGNENYAGIAARDVAGGLRSLAQAARGVAALTSDPAVQAIVLDTASDVLDKASSLIEEAKKAAGHPGDPESQQRLAQVAKAVTQALNRCVSCLPGQRDVDNALRAVGDASKRLLSDSLPPSTGTFQEAQSRLNEAAAGLNQAATELVQASRGTPQDLARASGRFGQDFSTFLEAGVEMAGQAPSQEDRAQVVSNLKGISMSSSKLLLAAKALSTDPAAPNLKSQLAAAARAVTDSINQLITMCTQQAPGQKECDNALRELETVRELLENPVQPINDMSYFGCLDSVMENSKVLGEAMTGISQNAKNGNLPEFGDAISTASKALCGFTEAAAQAAYLVGVSDPNSQAGQQGLVEPTQFARANQAIQMACQSLGEPGCTQAQVLSAATIVAKHTSALCNSCRLASARTTNPTAKRQFVQSAKEVANSTANLVKTIKALDGAFTEENRAQCRAATAPLLEAVDNLSAFASNPEFSSIPAQISPEGRAAMEPIVISAKTMLESAGGLIQTARALAVNPRDPPSWSVLAGHSRTVSDSIKKLITSMRDKAPGQLECETAIAALNSCLRDLDQASLAAVSQQLAPREGISQEALHTQMLTAVQEISHLIEPLANAARAEASQLGHKVSQMAQYFEPLTLAAVGAASKTLSHPQQMALLDQTKTLAESALQLLYTAKEAGGNPKQAAHTQEALEEAVQMMTEAVEDLTTTLNEAASAAGVVGGMVDSITQAINQLDEGPMGEPEGSFVDYQTTMVRTAKAIAVTVQEMVTKSNTSPEELGPLANQLTSDYGRLASEAKPAAVAAENEEIGSHIKHRVQELGHGCAALVTKAGALQCSPSDAYTKKELIECARRVSEKVSHVLAALQAGNRGTQACITAASAVSGIIADLDTTIMFATAGTLNREGTETFADHREGILKTAKVLVEDTKVLVQNAAGSQEKLAQAAQSSVATITRLADVVKLGAASLGAEDPETQVVLINAVKDVAKALGDLISATKAAAGKVGDDPAVWQLKNSAKVMVTNVTSLLKTVKAVEDEATKGTRALEATTEHIRQELAVFCSPEPPAKTSTPEDFIRMTKGITMATAKAVAAGNSCRQEDVIATANLSRRAIADMLRACKEAAYHPEVAPDVRLRALHYGRECANGYLELLDHVLLTLQKPSPELKQQLTGHSKRVAGSVTELIQAAEAMKGTEWVDPEDPTVIAENELLGAAAAIEAAAKKLEQLKPRAKPKEADESLNFEEQILEAAKSIAAATSALVKAASAAQRELVAQGKVGAIPANALDDGQWSQGLISAARMVAAATNNLCEAANAAVQGHASQEKLISSAKQVAASTAQLLVACKVKADQDSEAMKRLQAAGNAVKRASDNLVKAAQKAAAFEEQENETVVVKEKMVGGIAQIIAAQEEMLRKERELEEARKKLAQIRQQQYKFLPSELRDEH'
    aminos = processAminos()
    string = []
    starting = [0,0,0]
    theta = 90 - 123/2
    opposite = 1.32*np.arcsin(np.deg2rad(theta))
    adjacent = 1.32*np.arccos(np.deg2rad(theta))
    c = 0

    for el in range(len(sequence)):
        letter = sequence[el]
        amino = aminos[letter]
        coords = np.copy(amino)
        if opposite < 0:
            theta = np.deg2rad(180)
            rotmatx = [[1, 0, 0], [0, np.cos(theta), -np.sin(theta)], [0, np.sin(theta), np.cos(theta)]]
            for idx, vector in enumerate(coords):
                vector = vector[np.newaxis, :]
                vector = vector.T
                rotated: np.ndarray = (rotmatx @ vector).T
                coords[idx][:] = rotated
        position = coords + np.array([adjacent, 0, opposite]) + np.array(starting)
        opposite *= -1
        starting = position[2][:]
        string.append(position)
        c += len(coords)

    theta = np.deg2rad(125)
    rotmatx = np.asarray([[1, 0, 0], [0, np.cos(theta), -np.sin(theta)], [0, np.sin(theta), np.cos(theta)]])
    endpointc = position[2, :]
    endpointo = position[4, :]
    trans = endpointo-endpointc
    rotated = rotmatx @ trans # I don't think this is right yet, need to rotate the C also?
    newo = endpointc+rotated
    string.append([newo])

    print(string[-2])
    print(string[-1])

    with open("test.csv", 'w') as f:
        for a in string:
            a = list(a)
            for line in a:
                print(line)
                f.write(", ".join([str(el) for el in line]))
                f.write("\n")
