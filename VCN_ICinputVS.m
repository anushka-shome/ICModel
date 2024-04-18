function vs = VCN_ICinputVS(freq)

a = -2.053e-008;
b =       2.373;
c =      0.6087;

vs = a*freq.^b+c;