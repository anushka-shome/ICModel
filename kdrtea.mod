TITLE Potasium dr type current for RD Traub, J Neurophysiol 89:909-921, 2003

: IkdrTEA component

COMMENT

	Implemented by Maciej Lazarewicz 2003 (mlazarew@seas.upenn.edu)

ENDCOMMENT

INDEPENDENT { t FROM 0 TO 1 WITH 1 (ms) }

UNITS { 
	(mV) = (millivolt) 
	(mA) = (milliamp) 
} 

NEURON { 
	SUFFIX kdrtea
	USEION k READ ek WRITE ik
	RANGE gbartea, ik
      RANGE ntau,ninf
}

PARAMETER { 
	gbartea = 0.014 	(mho/cm2)
	v (mV)
	ek = -90 		(mV)  
}
 
ASSIGNED { 
	ik 		(mA/cm2) 
	ninf 		(1)
	ntau 		(ms) 
}
 
STATE {
	n
}

BREAKPOINT { 
	SOLVE states METHOD cnexp
	ik = gbartea * n * n * n * n * ( v - ek ) 
}
 
INITIAL { 
	settables(v) 
	n = ninf
	n = 0
}
 
DERIVATIVE states { 
	settables(v) 
	n' = ( ninf - n ) / ntau 
}

UNITSOFF 

PROCEDURE settables(v) { 
	TABLE ninf, ntau FROM -120 TO 40 WITH 641

	:minf  = 1 / ( 1 + exp( ( -v - 29.5 ) / 10 ) )
      ninf = 1/(1+ exp((-7.2-v)/8.9)) 
     : minf = 1/(1+exp(-(v-34.3)/12.1))
	if( v < -10.0 ) {
		ntau = 0.25 + 4.35 * exp( ( v + 10 ) / 10 )
	}else{
		ntau = 0.25 + 4.35 * exp( ( -v - 10 ) / 10 )
	}
}

UNITSON