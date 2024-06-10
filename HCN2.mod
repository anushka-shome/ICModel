TITLE I-h channel for IC adapted neurons from Koch and Grothe (2003)

: By Yamini Venkataraman

UNITS {
	(mA) = (milliamp)
	(mV) = (millivolt)

}

PARAMETER {
	v 		(mV)
        eh  		(mV)        
	celsius=34    (degC)
	gh=6.57e-5(mho/cm2)
        q10=4.5 :from MGB model
      q10temp = 32 (degC)
}


NEURON {
	SUFFIX hcn2
	NONSPECIFIC_CURRENT i
        RANGE gh, eh
        GLOBAL hinf,tau
}

STATE {
        h
}

ASSIGNED {
	i (mA/cm2)
        hinf      
        tau (ms)
qt
       
}

INITIAL {
      qt=q10^((celsius-q10temp)/10)

	rate(v)
	h=hinf
}


BREAKPOINT {
	SOLVE states METHOD cnexp
	i = gh*h*(v-eh)

}


DERIVATIVE states {     : exact when v held constant; integrates over dt step
        rate(v)
        h' =  (hinf - h)/tau
}

PROCEDURE rate(v (mV)) { :callable from hoc
        :LOCAL qt
        :qt=q10^((celsius-q10temp)/10)
        hinf = 1/(1+ exp((v+79.5)/9.8))
        tau = (1.475 + 1/(exp(-7.647-0.038*v)+exp(-1.533+0.046*v)))/qt
}