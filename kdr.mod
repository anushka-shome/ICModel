TITLE Potasium dr type current for RD Traub, J Neurophysiol 89:909-921, 2003

COMMENT

	Implemented by Maciej Lazarewicz 2003 (mlazarew@seas.upenn.edu)

ENDCOMMENT

INDEPENDENT { t FROM 0 TO 1 WITH 1 (ms) }

UNITS { 
	(mV) = (millivolt) 
	(mA) = (milliamp) 
} 

NEURON { 
	SUFFIX kdr
	USEION k READ ek WRITE ik
	RANGE gbar, ik
      RANGE mtau,minf
}

PARAMETER { 
	gbar = 0.086 	(mho/cm2)
	v  		(mV)  
   ek = -90 (mV)
   celsius=34    (degC)
   q10=3
   q10temp = 22 (degC) : From Traub et al. JNeurophys 2002

}
 
ASSIGNED { 
	ik 		(mA/cm2) 
	minf 		(1)
	mtau 		(ms) 
      qt
}
 
STATE {
	m
}

BREAKPOINT { 
	SOLVE states METHOD cnexp
	ik = gbar * m * m * m * m * ( v - ek ) 
}
 
INITIAL { 

     qt=q10^((celsius-q10temp)/10)

	settables(v) 
	m = minf
	m = 0
}
 
DERIVATIVE states { 
	settables(v) 
	m' = ( minf - m ) / mtau 
}

UNITSOFF 

PROCEDURE settables(v) { 
	TABLE minf, mtau FROM -120 TO 40 WITH 641

	:minf  = 1 / ( 1 + exp( ( -v - 29.5 ) / 10 ) )
      minf = 1/(1+ exp((-5.3-v)/10.8)) 
     : minf = 1/(1+exp(-(v-34.3)/12.1))
	if( v < -10.0 ) {
		mtau = (0.25 + 4.35 * exp( ( v + 10 ) / 10 ))
	}else{
		mtau = (0.25 + 4.35 * exp( ( -v - 10 ) / 10 ))
	}
}

UNITSON