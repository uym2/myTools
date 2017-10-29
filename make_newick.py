#! /usr/bin/env python
# usage: python make_newick.py <file_in> <file_out>


from sys import argv,stdout

filein = argv[1]

if len(argv) > 2:
    fout = open(argv[2],'w')
else:
    fout = stdout

with open(filein,'r') as f:
    s = f.read().rstrip()

stk=[]
s1=''

for c in s:
    if c == '(':
        stk.append(s1)
        stk.append('(')
        s1=''
    elif c == ',':
        stk.append(s1)
        s1=''
    elif c == ')':
        s1='('+s1
        c1=stk.pop()
        while c1 != '(':
            s1=s1+','+c1
            c1=stk.pop()
        s1=s1+')'+stk.pop()
    else:
        s1=s1+c

fout.write(s1)
