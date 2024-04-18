TITLE GABAb synapse

COMMENT
        simple alpha-synapse that generates a single PSP   
        *********************************************
        reference:   	McCormick, Wang & Huguenard (1993) 
			Cerebral Cortex 3(5), 387-398
        found in:       cat reticular nucleus of thalamus
        *********************************************
	Assembled for MyFirstNEURON by Arthur Houweling
ENDCOMMENT
					       
INDEPENDENT {t FROM 0 TO 1 WITH 1 (ms)}

NEURON {
	POINT_PROCESS ICGABAb3
	RANGE e, g, i, tau, a1, tauF, tauR, tau1, tau2, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, f1, f2, f3, f4, f5, f6, tauR2, b1
	NONSPECIFIC_CURRENT i
}

UNITS {
	(nA) 	= (nanoamp)
	(mV)	= (millivolt)
	(nS) 	= (nanomho)
}

PARAMETER {
	:a1 = .6237
	tauF = .4157	(ms)
	tauR = 45	(ms)
	tauR2 = 13.34	(ms)
	:tau = 18	(ms)
	:tau1 = 1.9604	(ms)
	a1 = 1
	b1 = 19.98

	:tauF = 4.016	(ms)
	:tauR = 345.9	(ms)
	tau = 1026	(ms)
	tau1 = 283	(ms)
	tau2 = 112	(ms)
	e = -85		(mV)
	v		(mV)
	celsius		(degC)
	:t1 = 283
	:t1 = 230
	:t2 = 1026
	:t2 = 425
	:t3 = 25.4791
	:t4 = 46.7493
	:t5 = 80.243
	:t6 = 27.2562
	:t7 = 53.1017
	:t8 = 100.9772
	:t9 = 32.9823
	:t10 = 36.0226

	t1 = 215.78
	t2 = 419.07
	t3 = 28.706
	t4 = 51.68
	t5 = 65.056
	t6 = 29.17
	t7 = 42.772
	t8 = 80.711
	t9 = 41.132
	t10 = 42.585

	f1 = 2.2528
	f2 = 0.17354
	f3 = 17.074
	f4 = 10.71
	f5 = 3.1687
	f6 = 1.8296

	:f1 = 84/31
	:f2 = 16/31
	:f3 = 504/31
	:f4 = 336/31
	:f5 = 96/31
	:f6 = 64/31


}

ASSIGNED { 
	i 		(nA)  
	g 		(nS)
}

STATE {
	A	(nS)
	B	(nS)
	C	(nS)
	D	(nS)
	E	(nS)
	F	(nS)
	G	(nS)
	H	(nS)
	I	(nS)
	J	(nS)
}

UNITSOFF
INITIAL {

	A = 0
	B = 0
	C = 0
	D = 0
	E = 0
	F = 0
	G = 0
	H = 0
	I = 0
	J = 0
}

BREAKPOINT { 
	SOLVE state METHOD cnexp
	g = f1*A + f2*B + f1*C + f3*D - f4*E + f2*F + f5*G - f6*H - f4*I - f6*J
	i = g*(v - e)
}

DERIVATIVE state {
	A' = -A/t1
	B' = -B/t2
	C' = -C/t3
	D' = -D/t4
	E' = -E/t5
	F' = -F/t6
	G' = -G/t7
	H' = -H/t8
	I' = -I/t9
	J' = -J/t10
}

UNITSON


NET_RECEIVE(weight (nS), t0 (ms), t1 (ms)){
LOCAL td, td2
INITIAL {t0 = t t1 = t}
td = (t-t0)
td2 = (t-t1)

if (td > 0) {
    A = A + .001 * weight * (1 - (a1*exp(-td/tauR) - a1*exp(-td/tauF)))
    B = B + .001 * weight * (1 - (a1*exp(-td/tauR) - a1*exp(-td/tauF)))
    C = C + .001 * weight * (1 - (a1*exp(-td/tauR) - a1*exp(-td/tauF)))
    D = D + .001 * weight * (1 - (a1*exp(-td/tauR) - a1*exp(-td/tauF)))
    E = E + .001 * weight * (1 - (a1*exp(-td/tauR) - a1*exp(-td/tauF)))
    F = F + .001 * weight * (1 - (a1*exp(-td/tauR) - a1*exp(-td/tauF)))
    G = G + .001 * weight * (1 - (a1*exp(-td/tauR) - a1*exp(-td/tauF)))
    H = H + .001 * weight * (1 - (a1*exp(-td/tauR) - a1*exp(-td/tauF)))
    I = I + .001 * weight * (1 - (a1*exp(-td/tauR) - a1*exp(-td/tauF)))
    J = J + .001 * weight * (1 - (a1*exp(-td/tauR) - a1*exp(-td/tauF)))
} else if (td2 > 0) {
    A = A + .001 * weight * (1 - (exp(-td/tauR)-exp(-td/tauF))*(1 + b1*exp(-td2/tauR2)))
    B = B + .001 * weight * (1 - (exp(-td/tauR)-exp(-td/tauF))*(1 + b1*exp(-td2/tauR2)))
    C = C + .001 * weight * (1 - (exp(-td/tauR)-exp(-td/tauF))*(1 + b1*exp(-td2/tauR2)))
    D = D + .001 * weight * (1 - (exp(-td/tauR)-exp(-td/tauF))*(1 + b1*exp(-td2/tauR2)))
    E = E + .001 * weight * (1 - (exp(-td/tauR)-exp(-td/tauF))*(1 + b1*exp(-td2/tauR2)))
    F = F + .001 * weight * (1 - (exp(-td/tauR)-exp(-td/tauF))*(1 + b1*exp(-td2/tauR2)))
    G = G + .001 * weight * (1 - (exp(-td/tauR)-exp(-td/tauF))*(1 + b1*exp(-td2/tauR2)))
    H = H + .001 * weight * (1 - (exp(-td/tauR)-exp(-td/tauF))*(1 + b1*exp(-td2/tauR2)))
    I = I + .001 * weight * (1 - (exp(-td/tauR)-exp(-td/tauF))*(1 + b1*exp(-td2/tauR2)))
    J = J + .001 * weight * (1 - (exp(-td/tauR)-exp(-td/tauF))*(1 + b1*exp(-td2/tauR2)))
} else {
    A = A + .001 * weight 
    B = B + .001 * weight
    C = C + .001 * weight
    D = D + .001 * weight
    E = E + .001 * weight
    F = F + .001 * weight
    G = G + .001 * weight
    H = H + .001 * weight
    I = I + .001 * weight
    J = J + .001 * weight
}
t1 = t0
t0 = t
}