#! /usr/bin/env python

from dendropy import Tree, TaxonNamespace

def read_label_from_reference_tree(t):
    label_mapping = {}
    t.encode_bipartitions()
    
    for node in t.preorder_node_iter():
        if not node.is_leaf():
            label_mapping[node.bipartition] = node.label
    return label_mapping

def label_tree(t,label_mapping):
    t.encode_bipartitions()
    for node in t.preorder_node_iter():
        if not node.is_leaf():
            key = node.bipartition            
            if key in label_mapping:
                node.label = label_mapping[key]
                  
def main():

    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument("-i","--input",required=True,help="Input trees")
    parser.add_argument("-o","--output",required=True,help="Output trees")
    parser.add_argument("-r","--ref",required=True,help="Reference tree")
    
    args = vars(parser.parse_args())

    inputfiles = args["input"].split()
    outputfiles = args["output"].split()
    refFile = args["ref"] if args["ref"] else None

    if not (len(outputfiles) == 1 or len(outputfiles) == len(inputfiles)):
        print("The number of output files must either be 1 or the same as the number of input files!")
    else:
        multi_output = len(outputfiles) > 1
         
        if not multi_output:
            fout = open(outputfiles[0],'w')
        
        taxa = TaxonNamespace()
   
        tree = Tree.get_from_path(refFile,"newick",taxon_namespace=taxa,rooting="force-rooted")
        label_mapping = read_label_from_reference_tree(tree)

    
    # Although using TreeList provided in Dendropy can be a more convenient solution,
    # I opted out for that because it requires storing a large number of trees in the memory at the same time
    # If the input trees are big then we will run out of memory 
    # Had problem with a set of 7k trees of 10k leaves which required >60G of memory just to store the trees
    # Here I read each tree and label it one-by-one. 
    #Just have to be thoughtful about making the taxon_namespace shared among all the trees
        for i,filein in enumerate(inputfiles):
            if multi_output:
                fout = open(outputfiles[i],'w')
            with open(filein,'r') as fin:
                strings = fin.readlines()       
                for s in strings:
                    tree = Tree.get(data=s,schema="newick",taxon_namespace=taxa,rooting="force-rooted")
                    label_tree(tree,label_mapping)
                    fout.write(tree.as_string("newick"))
            if multi_output:
                fout.close()
        
        if not multi_output:        
            fout.close()                                     

if __name__=="__main__":
    main()                                
