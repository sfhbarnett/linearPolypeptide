clear
load aas2
ala = ala-ala(1,:);
arg = arg-arg(1,:);
asn = asn-asn(1,:);
asp = asp-asp(1,:);
cys = cys-cys(1,:);
gln = gln-gln(1,:);
gly = gly-gly(1,:);
glu = glu-glu(1,:);
his = his-his(1,:);
ile = ile-ile(1,:);
lys = lys-lys(1,:);
meth = meth-meth(1,:);
phe = phe-phe(1,:);
pro = pro-pro(1,:);
ser = ser-ser(1,:);
thr = thr-thr(1,:);
trp = trp-trp(1,:);
tyr = tyr-tyr(1,:);
val = val-val(1,:);
leu = leu-leu(1,:);
%%

ala = rotateAA(ala);
arg = rotateAA(arg);
asn = rotateAA(asn);
asp = rotateAA(asp);
cys = rotateAA(cys);
gln = rotateAA(gln);
gly = rotateAA(gly);
glu = rotateAA(glu);
his = rotateAA(his);
ile = rotateAA(ile);
lys = rotateAA(lys);
meth = rotateAA(meth);
phe = rotateAA(phe);
pro = rotateAA(pro);
ser = rotateAA(ser);
thr = rotateAA(thr);
trp = rotateAA(trp);
tyr = rotateAA(tyr);
val = rotateAA(val);
leu = rotateAA(leu);


%%

sequence = 'MVALSLKISIGNVVKTMQFEPSTMVYDACRIIRERIPEAPAGPPSDFGLFLSDDDPKKGIWLEAGKALDYYMLRNGDTMEYRKKQRPLKIRMLDGTVKTIMVDDSKTVTDMLMTICARIGITNHDEYSLVRELMEEKKEEITGTLRKDKTLLRDEKKMEKLKQKLHTDDELNWLDHGRTLREQGVEEHETLLLRRKFFYSDQNVDSRDPVQLNLLYVQARDDILNGSHPVSFDKACEFAGFQCQIQFGPHNEQKHKAGFLDLKDFLPKEYVKQKGERKIFQAHKNCGQMSEIEAKVRYVKLARSLKTYGVSFFLVKEKMKGKNKLVPRLLGITKECVMRVDEKTKEVIQEWNLTNIKRWAASPKSFTLDFGDYQDGYYSVQTTEGEQIAQLIAGYIDIILKKKKSKDHFGLEGDEESTMLEDSVSPKKSTVLQQQYNRVGKVEHGSVALPAIMRSGASGPENFQVGSMPPAQQQITSGQMHRGHMPPLTSAQQALTGTINSSMQAVQAAQATLDDFDTLPPLGQDAASKAWRKNKMDESKHEIHSQVDAITAGTASVVNLTAGDPAETDYTAVGCAVTTISSNLTEMSRGVKLLAALLEDEGGSGRPLLQAAKGLAGAVSELLRSAQPASAEPRQNLLQAAGNVGQASGELLQQIGESDTDPHFQDALMQLAKAVASAAAALVLKAKSVAQRTEDSGLQTQVIAAATQCALSTSQLVACTKVVAPTISSPVCQEQLVEAGRLVAKAVEGCVSASQAATEDGQLLRGVGAAATAVTQALNELLQHVKAHATGAGPAGRYDQATDTILTVTENIFSSMGDAGEMVRQARILAQATSDLVNAIKADAEGESDLENSRKLLSAAKILADATAKMVEAAKGAAAHPDSEEQQQRLREAAEGLRMATNAAAQNAIKKKLVQRLEHAAKQAAASATQTIAAAQHAASTPKASAGPQPLLVQSCKAVAEQIPLLVQGVRGSQAQPDSPSAQLALIAASQSFLQPGGKMVAAAKASVPTIQDQASAMQLSQCAKNLGTALAELRTAAQKAQEACGPLEMDSALSVVQNLEKDLQEVKAAARDGKLKPLPGETMEKCTQDLGNSTKAVSSAIAQLLGEVAQGNENYAGIAARDVAGGLRSLAQAARGVAALTSDPAVQAIVLDTASDVLDKASSLIEEAKKAAGHPGDPESQQRLAQVAKAVTQALNRCVSCLPGQRDVDNALRAVGDASKRLLSDSLPPSTGTFQEAQSRLNEAAAGLNQAATELVQASRGTPQDLARASGRFGQDFSTFLEAGVEMAGQAPSQEDRAQVVSNLKGISMSSSKLLLAAKALSTDPAAPNLKSQLAAAARAVTDSINQLITMCTQQAPGQKECDNALRELETVRELLENPVQPINDMSYFGCLDSVMENSKVLGEAMTGISQNAKNGNLPEFGDAISTASKALCGFTEAAAQAAYLVGVSDPNSQAGQQGLVEPTQFARANQAIQMACQSLGEPGCTQAQVLSAATIVAKHTSALCNSCRLASARTTNPTAKRQFVQSAKEVANSTANLVKTIKALDGAFTEENRAQCRAATAPLLEAVDNLSAFASNPEFSSIPAQISPEGRAAMEPIVISAKTMLESAGGLIQTARALAVNPRDPPSWSVLAGHSRTVSDSIKKLITSMRDKAPGQLECETAIAALNSCLRDLDQASLAAVSQQLAPREGISQEALHTQMLTAVQEISHLIEPLANAARAEASQLGHKVSQMAQYFEPLTLAAVGAASKTLSHPQQMALLDQTKTLAESALQLLYTAKEAGGNPKQAAHTQEALEEAVQMMTEAVEDLTTTLNEAASAAGVVGGMVDSITQAINQLDEGPMGEPEGSFVDYQTTMVRTAKAIAVTVQEMVTKSNTSPEELGPLANQLTSDYGRLASEAKPAAVAAENEEIGSHIKHRVQELGHGCAALVTKAGALQCSPSDAYTKKELIECARRVSEKVSHVLAALQAGNRGTQACITAASAVSGIIADLDTTIMFATAGTLNREGTETFADHREGILKTAKVLVEDTKVLVQNAAGSQEKLAQAAQSSVATITRLADVVKLGAASLGAEDPETQVVLINAVKDVAKALGDLISATKAAAGKVGDDPAVWQLKNSAKVMVTNVTSLLKTVKAVEDEATKGTRALEATTEHIRQELAVFCSPEPPAKTSTPEDFIRMTKGITMATAKAVAAGNSCRQEDVIATANLSRRAIADMLRACKEAAYHPEVAPDVRLRALHYGRECANGYLELLDHVLLTLQKPSPELKQQLTGHSKRVAGSVTELIQAAEAMKGTEWVDPEDPTVIAENELLGAAAAIEAAAKKLEQLKPRAKPKEADESLNFEEQILEAAKSIAAATSALVKAASAAQRELVAQGKVGAIPANALDDGQWSQGLISAARMVAAATNNLCEAANAAVQGHASQEKLISSAKQVAASTAQLLVACKVKADQDSEAMKRLQAAGNAVKRASDNLVKAAQKAAAFEEQENETVVVKEKMVGGIAQIIAAQEEMLRKERELEEARKKLAQIRQQQYKFLPSELRDEH';

string = [];
starting = [0,0,0];
theta = 90-123/2;
opposite = 1.32*asin(deg2rad(theta));
adjacent = 1.32*acos(deg2rad(theta));
for el = 1:numel(sequence)
    el
    letter = sequence(el);
    for amino = 1:size(aminos,2)
        if letter == aminos{amino}.code
            break
        end
    end
    aminocoordinates = aminos{amino}.coords;
    if opposite < 0
        theta = deg2rad(180);
        rotmatx = [1, 0, 0; 0, cos(theta), -sin(theta); 0, sin(theta), cos(theta)];
        for i = 1:size(aminocoordinates,1)
            vec = aminocoordinates(i,:);
            rotated = rotmatx*vec';
            aminocoordinates(i,:) = rotated';
        end
    end
    position = aminocoordinates + [adjacent,0,opposite] + starting;
    opposite = opposite * -1;
    starting = position(3,:);
    string = [string;position];
    
end

theta = deg2rad(125);
rotmatx = [1, 0, 0; 0, cos(theta), -sin(theta); 0, sin(theta), cos(theta)];
endpointc = position(3,:);
endpointo = position(5,:);
trans = endpointo-endpointc;
rotated = rotmatx*trans';
newo = endpointc+rotated'
string = [string;newo];

%%

a = struct('code','A','coords',ala);
r = struct('code','R','coords',arg);
n = struct('code','N','coords',asn);
d = struct('code','D','coords',asp);
c = struct('code','C','coords',cys);
e = struct('code','E','coords',glu);
q = struct('code','Q','coords',gln);
g = struct('code','G','coords',gly);
h = struct('code','H','coords',his);
i = struct('code','I','coords',ile);
l = struct('code','L','coords',leu);
k = struct('code','K','coords',lys);
m = struct('code','M','coords',meth);
f = struct('code','F','coords',phe);
p = struct('code','P','coords',pro);
s = struct('code','S','coords',ser);
t = struct('code','T','coords',thr);
w = struct('code','W','coords',trp);
y = struct('code','Y','coords',tyr);
v = struct('code','V','coords',val);

aminos = {a,r,n,d,c,e,q,g,h,i,l,k,m,f,p,s,t,w,y,v};

%%

string = round(string,5);
stringout = round(string.*100)./100;
dlmwrite('test3.csv', stringout, 'precision', '%.3f')