:Author: Carnevale, N.T. and Hines, M.L.(2006) with edits by B.Coventry
:Date 6/11/2013
:Alpha_Synapse.mod 

NEURON {
    POINT_PROCESS alphasyn
    RANGE tau, e, i
    NONSPECIFIC_CURRENT i
}

PARAMETER {
    tau = 0.1  (ms)
    e   = 0    (millivolt)
}

ASSIGNED {
    v (millivolt)
    i (nanoamp)
}

STATE { a (microsiemens) g (microsiemens) }
KINETIC state {
    ~ a <-> g (1/tau, 0)
    ~ g -> (1/tau)
}

BREAKPOINT {
    SOLVE state METHOD sparse
    i = g*(v-e)
}

NET_RECEIVE(weight (microsiemens)) {
    a = a + weight*exp(1)
}
