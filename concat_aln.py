#! /usr/bin/env python

from sys import argv
from sequence_lib import read_fasta, write_fasta

def add_one_aln(concated,L,newNames, newSeqs):
    for i,name in enumerate(newNames):
        if name in concated:
            l = concated[name][0]
            if l < L:
                concated[name].append((1,L-l))
            concated[name].append((0,newSeqs[i]))
            concated[name][0] = L + len(newSeqs[i])
        else:
            concated[name] = [L+len(newSeqs[i]),(1,L),(0,newSeqs[i])]
    return L + len(newSeqs[0])        


def print_concatenated(concated,L):
    names = []
    seqs = []
    for name in concated:
        names.append(name)
        seq = ''
        l = concated[name][0]

        for f,s in concated[name][1:]:
            if f == 1:
                seq += '-'*s
            else:
                seq += s
        if l < L:
            seq += '-'*(L-l)

        seqs.append(seq)
        
    return names, seqs            
                
def main():
    concated = {}
    L = 0
                    
    for seqfile in argv[1:-1]:
        newNames, newSeqs = read_fasta(seqfile)
        L = add_one_aln(concated,L,newNames,newSeqs)


    names, seqs = print_concatenated(concated,L)
    write_fasta(argv[-1],names,seqs)
    
if __name__=='__main__':
    main()        
