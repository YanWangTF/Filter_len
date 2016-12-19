#! /usr/bin/python

#to filter out short multiple sequence alignment file for phylogenomic analyses
#usage: python Filter_len.py length(min) inputfile outputfile

import os
import sys
import numpy
import math
import getopt
from Bio import SeqIO #module from Biopython and good for dealing with FASTA

n = int(float(sys.argv[1]))

input = open(sys.argv[2], 'rU')
out = open(sys.argv[3], 'w')

for record in SeqIO.parse(input, 'fasta'):
	sequence = record.seq
	if len(sequence)>n:
		SeqIO.write(record, out, 'fasta')

input.close()
out.close()
