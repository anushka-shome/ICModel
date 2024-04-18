TITLE NMDA Synapse

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
	POINT_PROCESS NMDA_LL_IC_2
	USEION mg READ mgo VALENCE 2
	USEION ca READ eca WRITE ica
	USEION na READ ena WRITE ina
	RANGE e, g, i, w, tau, a1, tauF, tauR, tau1, a2, tauF2, tauR2, fca, fna, vdepscale
	NONSPECIFIC_CURRENT i
}

UNITS {
	(nA) 	= (nanoamp)
	(mV)	= (millivolt)
	(nS) 	= (nanomho)
	(mM)    = (milli/liter)
        F	= 96480 (coul)
        R       = 8.314 (volt-coul/degC)

}

PARAMETER {
	:tau = 71
	:tau = 70
	:tau1 = 24.2056	(ms)
	:tau = 90	(ms)
	tau = 50	(ms)
	:tau1 = 28	(ms)
	tau1 = 32	(ms)
	tauF = .3	(ms)
	tauR = 36.56	(ms)
	tauF2 = .3	(ms)
	tauR2 = 26.32	(ms)
	:fca = .1
	fca = 0
	fna = 0
	a1 = 1.918
	a2 = 1.306
	w= .001				: weight factor for gmaxEPSP
	e= 20		(mV)
	v		(mV)
	mgo		(mM)
	celsius 	(degC)
	vdepscale = 35.7
}

ASSIGNED { 
	i (nA)
	ica (nA)
	ina (nA)
	eca (mV)
	ena (mV)
	g (nS)
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

BREAKPOINT {	LOCAL k
	SOLVE state METHOD cnexp
	:k = 1.07 * exp(2*0.73*v*(.001)*F/(R*(celsius+273.16)))
	k = vdepscale * exp(2*0.73*v*(.001)*F/(R*(celsius+273.16)))	 
	g = (B - A)
	ica = .2257*g*fca*(1-(1/(1+k/mgo)))*(v - eca)
	ina = .2257*g*fna*(1-(1/(1+k/mgo)))*(v - ena)
	:i = .2257*g*(1-fca-fna)*(1-(1/(1+k/mgo)))*(v - e)
	i = .56*g*(1-fca-fna)*(1-(1/(1+k/mgo)))*(v - e)


}
DERIVATIVE state {
	A' = -A/tau1
	B' = -B/tau
}

UNITSON


NET_RECEIVE(weight (nS), t0 (ms), t1 (ms)){
LOCAL td, td2, td3
INITIAL {t0 = t t1 = t}
td = (t-t0)
td2 = (t-t1)
td3 = td2 - td

:A = A + .001 * weight * (1 + (a1*exp(-td/tauR) - a1*exp(-td/tauF))) * (1 + (a2*exp(-td3/tauR2) - a2*exp(-td3/tauF2)))
:B = B + .001 * weight * (1 + (a1*exp(-td/tauR) - a1*exp(-td/tauF))) * (1 + (a2*exp(-td3/tauR2) - a2*exp(-td3/tauF2)))

A = A + .001 * weight 
B = B + .001 * weight
t1 = t0
t0 = t

}