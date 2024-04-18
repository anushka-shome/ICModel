TITLE Hippocampal HH channels
:
: Fast Na+ and K+ currents responsible for action potentials
: Iterative equations
:
: Equations modified by Traub, for Hippocampal Pyramidal cells, in:
: Traub & Miles, Neuronal Networks of the Hippocampus, Cambridge, 1991
:
: range variable vtraub adjust threshold
:
: Written by Alain Destexhe, Salk Institute, Aug 1992
:

INDEPENDENT {t FROM 0 TO 1 WITH 1 (ms)}

NEURON {
	SUFFIX Isodium
	USEION na READ ena WRITE ina
	RANGE gnabar, vtraub
	RANGE m_inf, h_inf
	RANGE tau_m, tau_h
	RANGE m_exp, h_exp
}


UNITS {
	(mA) = (milliamp)
	(mV) = (millivolt)
}

PARAMETER {
	gnabar	= 0.1	(mho/cm2)
	


	ena	= 50	(mV)
	
	celsius = 34    (degC)
	dt              (ms)
	v               (mV)
	vtraub	= -63	(mV)
}

STATE {
	m h 
}

ASSIGNED {
	ina	(mA/cm2)
	
	il	(mA/cm2)
	m_inf
	h_inf

	tau_m
	tau_h
	m_exp
	h_exp
	tadj
}


BREAKPOINT {
	SOLVE states
	ina = gnabar * m*m*m*h * (v - ena)

}


:DERIVATIVE states {   : exact Hodgkin-Huxley equations
:	evaluate_fct(v)
:	m' = (m_inf - m) / tau_m
:	h' = (h_inf - h) / tau_h
:	n' = (n_inf - n) / tau_n
:}

PROCEDURE states() {	: exact when v held constant
	evaluate_fct(v)
	m = m + m_exp * (m_inf - m)
	h = h + h_exp * (h_inf - h)

	VERBATIM
	return 0;
	ENDVERBATIM
}

UNITSOFF
INITIAL {
	m = 0
	h = 0
:
:
:  Q10 was assumed to be 3 for both currents
:
: original measurements at roomtemperature?

	tadj = 3.0 ^ ((celsius-36)/ 10 )
}

PROCEDURE evaluate_fct(v(mV)) { LOCAL a,b,v2

	v2 = v - vtraub : convert to traub convention

	a = 0.32 * (13-v2) / ( exp((13-v2)/4) - 1)
	b = 0.28 * (v2-40) / ( exp((v2-40)/5) - 1)
	tau_m = 1 / (a + b) / tadj
	m_inf = a / (a + b)

	a = 0.128 * exp((17-v2)/18)
	b = 4 / ( 1 + exp((40-v2)/5) )
	tau_h = 1 / (a + b) / tadj
	h_inf = a / (a + b)

	a = 0.032 * (15-v2) / ( exp((15-v2)/5) - 1)
	b = 0.5 * exp((10-v2)/40)


	m_exp = 1 - exp(-dt/tau_m)
	h_exp = 1 - exp(-dt/tau_h)

}

UNITSON
