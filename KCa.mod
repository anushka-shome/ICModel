:Created on Thu Feb  1 23:42:09 2024

:@author: anushkashome

TITLE Calcium Dependent Potassium Channels

INDEPENDENT {t FROM 0 TO 1 WITH 1 (ms)} 

NEURON {
    SUFFIX KCa
    USEION ca READ eca WRITE ica
    USEION k READ ek WRITE ik
    RANGE ik, ica
    RANGE gbk, gsk
    RANGE aq, bq, br
    RANGE q, r, s
    

}

:UNITS {
	:(mA) = (milliamp)
	:(mV) = (millivolt)
:}

PARAMETER {
	eca = -70 (mV)
	ek = -90 (mV)
	v (mV)
	celsius = 22 (degC) :Fix
	dt (m/s)
    cai = 2e-4 (M)
    gbkbar = 0.00226 (S/cm2)
    gskbar = 0.03 (S/cm2)
	
}

STATE {
    q
    r
	s
}

ASSIGNED {
    ica (mA/cm2)
    ik (mA/cm2)
    gbk (mho/cm2)
    gsk (mho/cm2)
    tadj
    aq
    bq
    br
   
	
}


BREAKPOINT {
	SOLVE states
	ik = (gbk+gsk)*(v-ek)
	gbk = gbkbar * r * s^(2)
    gsk = gskbar * q^(2)
	
}



PROCEDURE states() {	: this discretized form is more stable
    evaluate_fct(v)
    q = aq/(aq+bq)
    r = 7.5/(7.5+br)
    s = 1/(1+4/(1000*cai))
	:VERBATIM
	:return 0;
	:ENDVERBATIM
}

UNITSOFF
INITIAL {
    tadj = 3.0 ^ ((celsius-22)/ 10 ) :Fix later
    evaluate_fct(v)
    q = aq/(aq+bq)
    r = 7.5/(7.5+br)
    s = 1/(1+4/(1000*cai))
}

PROCEDURE evaluate_fct(v(mV)) {
	aq = 0.00246/(exp(12*log(10*cai)+28)/-4.5)
	bq = 0.006/(exp(12*log(10*cai)+60.4)/35)
	br = 0.11/exp((v-35)/14.9)
	
}

UNITSON
