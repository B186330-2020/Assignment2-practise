#!/bin/python3
import os, subprocess, shutil
protein_seqs = open("proteins.fa")
protein_seqs_contents = protein_seqs.read()
stripped_seqs = protein_seqs_contents.rstrip("\n")
listy = []
count = 0
copy = False
for seqs in stripped_seqs:
    if seqs == '':
            print("Empty input")
    elif seqs == ']':
            copy = False
            target1 = count-1
            listy.append(stripped_seqs[target2:target1])
    elif seqs == '[':
            copy = True
            target2 = count+1
    count += 1

prev = []
for x in listy:
    if x not in prev:
            prev.append(x)
print(prev)

print(" total number of proteins = ", len(listy), '\n','total number of proteins from distinct species = ', len(prev))
