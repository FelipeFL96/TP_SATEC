#!/usr/bin/env python3

import circuit.circuit as circ
from circuit.cnf import SatVar, Solver

# circ full_adder {
#      inputs: a, b, cin
#      outputs: s, cout
#      s0 = a ^ b
#      s = s0 ^ cin
#      cout = (a & b) | (s0 & cin)
# }

# Inputs
a = SatVar('a')
b = SatVar('b')
cin = SatVar('cin')

# Outputs
s = SatVar('s')
cout = SatVar('cout')

# Internal variables (if needed)


def mk_adder():
    
    # TODO: Construct CNF for full adder
    return (a | ~a) & (b | ~s) & ~cout & (b | cin)

