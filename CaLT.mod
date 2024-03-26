:Created on Sun Jan 28 14:28:18 2024

:@author: anushkashome

TITLE Low Threshold Calcium Channels

INDEPENDENT {t FROM 0 TO 1 WITH 1 (ms)} 

NEURON {
    SUFFIX CaLT
    USEION ca READ eca WRITE ica
    RANGE it, g
    RANGE m_inf, h_inf
    RANGE tau_m, tau_h
    RANGE m_exp, h_exp

}

:UNITS {
	:(mA) = (milliamp)
	:(mV) = (millivolt)
:}

PARAMETER {
	pcat = 0.0002 (cm/s)
	eca = -70 (mV)
	v (mV)
	celsius = 22 (degC) :Fix
	dt (m/s)
	z = 2
	f = 96485 (C/mol)
	r = 8.314 (J/mol*K)
	cao = 2e-3 (M)
    cai = 2e-4 (M)
	
}

STATE {
    m
    h
	
}

ASSIGNED {
    ica (mA/cm2)
    g (mho/cm2)
    m_inf
    h_inf
    tau_m (ms)
    tau_h (ms)
    m_exp
    h_exp
    tadj
   
	
}


BREAKPOINT {
	SOLVE states
	g = (z^(2)*f^(2)*v/r*(celsius+273.15))*((cai-cao*exp(-z*f*v/r*(celsius+273.15)))/(1-exp(-z*f*v/r*(celsius+273.15))))
	ica = pcat*m^(2)*h*g
	
}



PROCEDURE states() {	: this discretized form is more stable
    evaluate_fct(v)
    m = m + m_exp * (m_inf - m)
    h = h + h_exp * (h_inf - h)
	:VERBATIM
	:return 0;
	:ENDVERBATIM
}

UNITSOFF
INITIAL {
    tadj = 3.0 ^ ((celsius-22)/ 10 ) :Fix later
    evaluate_fct(v)
    m = m_inf
    h = h_inf
}

PROCEDURE evaluate_fct(v(mV)) {
	m_inf = 1/(1+exp(-(v+57)/6.2))
	h_inf = 1/(1+exp((v+81)/4))
	
	tau_m = (0.612 + 1.0/(exp(-(v+132)/16.7) + exp((v+16.8)/18.2)))/tadj
	if (v < -80) {
    	tau_h = (exp((v+467)/66.6))/tadj
    }
    else {
        tau_h = (28 + exp(-(v+22)/10.5))/tadj
    }
	
	m_exp = 1-exp(-dt/tau_m)
	h_exp = 1-exp(-dt/tau_h)
}

UNITSON
