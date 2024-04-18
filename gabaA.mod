TITLE GABAa synapse

COMMENT
	simple inverted alpha synapse that generates a single PSP
	modified from:  
        *********************************************
        reference:      McCormick, Wang & Huguenard (1993) 
			Cerebral Cortex 3(5), 387-398
        *********************************************
ENDCOMMENT
					       
INDEPENDENT {t FROM 0 TO 1 WITH 1 (ms)}

NEURON {
	POINT_PROCESS ICGABAa
	RANGE e, i, g, w, a1, tauF, tauR, tau, tau1, scale
	NONSPECIFIC_CURRENT i
}

UNITS {
	(nA) 	= (nanoamp)
	(mV)	= (millivolt)
	(nS) 	= (nanomho)
}

PARAMETER {
	tau = 15	(ms)
	tau1 = 3	(ms)
	w= 1				: weight factor for gmaxEPSP
	tauF = .3	(ms)
	tauR = 16.85	(ms)
	:a1 = .95
	:a1 = .75
	:a1 = 1.148
	a1 = 1
	e= -80		(mV)
	:e = -75
	v		(mV)
	celsius		(degC)
	scale = 1.4085
}

ASSIGNED { 
	i 		(nA)  
	g 		(nS)
}

STATE {
	A (nS)
	B (nS)
}

UNITSOFF
INITIAL {

	A = 0
	B = 0
}
BREAKPOINT { 
	SOLVE state METHOD cnexp
	g = (B - A)
	i = scale*g*(v - e)

}
DERIVATIVE state {
	A' = -A/tau1
	B' = -B/tau
}

UNITSON

NET_RECEIVE(weight (nS), t0 (ms)){
LOCAL td
INITIAL {t0 = t}
td = (t-t0)
if (td > 0) {
A = A + .001 * weight  * (1 - a1*exp(-td/tauR)) 
B = B + .001 * weight  * (1 - a1*exp(-td/tauR))
} else {
A = A + .001 * weight
B = B + .001 * weight
}
t0 = t
}