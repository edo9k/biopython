#!/bin/python3

from Bio.Seq import Seq

# sequencia
s = Seq("GATACA")
print(s)

# transcricao
rna = s.transcribe()
print(rna)

# traducao
protein = rna.translate()
print(protein)

