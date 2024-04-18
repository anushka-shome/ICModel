:Created on Mon Jan 22 20:41:38 2024

:@author: anushkashome


TITLE High Threshold Calcium Channels

INDEPENDENT {t FROM 0 TO 1 WITH 1 (ms)} 

NEURON {
    SUFFIX CaHT
    USEION ca READ eca WRITE ica
    RANGE ica, g
    RANGE m_inf
    RANGE tau_m
    RANGE m_exp
    RANGE am, bm

}

:UNITS {
	:(mA) = (milliamp)
	:(mV) = (millivolt)
:}

PARAMETER {
	pcal = 0.00001 (cm/s)
	eca = -70 (mV)
	v (mV)
	celsius = 22 (degC) :Fix
	dt (m/s)
	z = 2
	f = 96485 (C/mol)
	r = 8.314 (J/mol*K)
	cao = 2e-3 (M)
    cai = 5e-8 (M)
	
}

STATE {
    m
	
}

ASSIGNED {
    ica (mA/cm2)
    g (mho/cm2)
    m_inf
    tau_m (ms)
    m_exp
    am
    bm
    tadj
   
	
}


BREAKPOINT {
	SOLVE states
	g = (z^(2)*f^(2)*v/r*(celsius+273.15))*((cai-cao*exp(-z*f*v/(r*(celsius+273.15))))/(1-exp(-z*f*v/(r*(celsius+273.15)))))
	ica = pcal*m^(2)*g :and h if needed
	
}



PROCEDURE states() {	: this discretized form is more stable
    evaluate_fct(v)
    m = m + m_exp * (m_inf - m)
	:VERBATIM
	:return 0;
	:ENDVERBATIM
}

UNITSOFF
INITIAL {
    tadj = 3.0 ^ ((celsius-22)/ 10 ) :Fix later
    evaluate_fct(v)
    m = m_inf
}

PROCEDURE evaluate_fct(v(mV)) {
	am = 1.6/(1+exp(-0.072(v-5.0)))
	bm = 0.02(v-1.31)/(exp((v-1.31)/5.38)-1)
	m_inf = am/(am+bm)
	tau_m = (1/(am+bm))/tadj
	
	m_exp = 1-exp(-dt/tau_m)
}

UNITSON