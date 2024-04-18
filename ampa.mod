TITLE AMPA Synapse

COMMENT
        simple alpha-synapse that generates a single PSP   
        *********************************************
        reference:      McCormick, Wang & Huguenard (1993) 
			Cerebral Cortex 3(5), 387-398
        *********************************************
	Assembled for MyFirstNEURON by Arthur Houweling
ENDCOMMENT
					       
INDEPENDENT {t FROM 0 TO 1 WITH 1 (ms)}

NEURON {
	POINT_PROCESS AMPA_LL_IC
	RANGE e, i, g, w, tau, a1, a2, tauF, tauR, tau1, tauR2, tauR3, a3, a4
	NONSPECIFIC_CURRENT i
}

UNITS {
	(nA) 	= (nanoamp)
	(mV)	= (millivolt)
	(nS) 	= (nanomho)
}

PARAMETER {
	tau1 = .5464	(ms)
	tau = 6		(ms)
	:tau = 18	(ms)
	tauF = .3	(ms)
	:tauR = 25.42	(ms) Original values
	:tauR2 = 25.42	(ms) Original Values
	tauR = 63.73	(ms)
	tauR2 = 3.32	(ms)
	tauR3 = 69.7	(ms)
	tauR4 = 70.46	(ms)


	:a1 = .95
	:a1 = .75
	:a1 = 1.01    Original values
	a1 = .378	: new
	a2 = .622	: new
	:a3 = .9268	: new
	a3 = 115.4
	a4 = 115.3
	:a3 = 0.3

	w= .001				: weight factor for gmaxEPSP
	e= 0.0		(mV)
	v		(mV)
	celsius		(degC)
}

ASSIGNED { 
	i 		(nA)  
	g 		(nS)
	tadj
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
	i = 1.0526*g*(v - e)

}
DERIVATIVE state {
	A' = -A/tau1
	B' = -B/tau
}

UNITSON

NET_RECEIVE(weight (nS), t0 (ms), t1 (ms)){
LOCAL td, td2
INITIAL {t0 = t t1 = t}
td = (t-t0)
td2 = (t-t1)
if (td2 > 0) {
:A = A + .001 * weight * (1 - a1*exp(-td/tauR)) * (1 - a1*exp(-td2/tauR2))
:B = B + .001 * weight * (1 - a1*exp(-td/tauR)) * (1 - a1*exp(-td2/tauR2))
:A = A + .001 * weight * (1 - a1*exp(-td/tauR) - a2*exp(-td/tauR2)) * (1 - a3*exp(-td2/tauR3))
:B = B + .001 * weight * (1 - a1*exp(-td/tauR) - a2*exp(-td/tauR2)) * (1 - a3*exp(-td2/tauR3))
A = A + .001 * weight * (1 - a1*exp(-td/tauR) - a2*exp(-td/tauR2)) * (1 + a3*exp(-td2/tauR3) - a4*exp(-td2/tauR4))
B = B + .001 * weight * (1 - a1*exp(-td/tauR) - a2*exp(-td/tauR2)) * (1 + a3*exp(-td2/tauR3) - a4*exp(-td2/tauR4))
} else if (td > 0) {
:A = A + .001 * weight * (1 - a1*exp(-td/tauR))
:B = B + .001 * weight * (1 - a1*exp(-td/tauR))
A = A + .001 * weight * (1 - a1*exp(-td/tauR) - a2*exp(-td/tauR2))
B = B + .001 * weight * (1 - a1*exp(-td/tauR) - a2*exp(-td/tauR2))

} else {
A = A + .001 * weight
B = B + .001 * weight
}
t1 = t0
t0 = t
}

