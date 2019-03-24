#!/bin/python3

from Bio.Seq import Seq

# sequencia 
s = Seq("ATG")
print( s )

# sequencia complementar
complementar = s.complement()
print( complementar )

# sequencia reverso complementar
reverso = s.reverse_complement()
print( reverso )

