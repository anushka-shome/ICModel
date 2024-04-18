:Created on Sun Jan 28 15:51:30 2024

:@author: anushkashome

TITLE Hyperpolarization-Activated Cation (HCN) Current

INDEPENDENT {t FROM 0 TO 1 WITH 1 (ms)} 

NEURON {
    SUFFIX HCN
    NONSPECIFIC_CURRENT i
    RANGE gh, eh
    RANGE m_inf
    RANGE tau_m
    RANGE m_exp
}

UNITS {
	(mA) = (milliamp)
	(mV) = (millivolt)
}

PARAMETER {
	gh = 0.000218 (S/cm2)
	eh  = -40 (mV)
	v (mV)
	celsius = 22 (degC)
}

STATE {
    m
   
}

ASSIGNED {
    i (mA/cm2)
    m_inf
    tau_m
    m_exp
    tadj
}


BREAKPOINT {
	SOLVE states
	i = gh * m * (v-eh)
	
}



PROCEDURE states() {	: this discretized form is more stable
    evaluate_fct(v)
    m = m + m_exp * (m_inf - m)
}

UNITSOFF
INITIAL {
    tadj = 3.0 ^ ((celsius-22)/ 10 ) :Fix later
    evaluate_fct(v)
    m = m_inf
}

PROCEDURE evaluate_fct(v(mV)) {
    m_inf = 1/(1+exp((v+79.5)/9.8))
    tau_m = (1.475 + 1/(exp(-7.647-(0.038*v)) + exp(-1.533+(0.046*v))))/tadj
    
	m_exp = 1-exp(-dt/tau_m)
}

UNITSON