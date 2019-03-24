#!/bin/python3

from Bio.Seq import Seq

# sequencia
s = Seq("GATACA")
rna = s.transcribe()

print(s)
print(rna)

