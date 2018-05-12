#! /usr/bin/env python

from dendropy import Tree, TaxonNamespace

def label_primary_tree(t,prefix="I_"):
    label_mapping = {}
    labelID = 1
    t.encode_bipartitions()
    for node in t.preorder_node_iter():
        if not (node is t.seed_node or node.is_leaf()):
            node.label = prefix + str(labelID)
            label_mapping[node.bipartition] = node.label
            labelID += 1

    t.seed_node.label = prefix + str(0)
    
    return label_mapping, labelID
    

def label_secondary_tree(t,label_mapping,startID,prefix="I_"):
    t.encode_bipartitions()
    labelID = startID
    for node in t.preorder_node_iter():
        if not (node is t.seed_node or node.is_leaf()):
            key = node.bipartition            
            if key in label_mapping:
                node.label = label_mapping[key]
            else:
                node.label = prefix + str(labelID)
                label_mapping[key] = node.label
                labelID += 1    

    return label_mapping, labelID
                  
                  
def main():

    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument("-i","--input",required=True,help="Input trees")
    parser.add_argument("-o","--output",required=True,help="Output trees")

    args = vars(parser.parse_args())

    inputfiles = args["input"].split()
    outputfiles = args["output"].split()


    if not (len(outputfiles) == 1 or len(outputfiles) == len(inputfiles)):
        print("The number of output files must either be 1 or the same as the number of input files!")
    else:
        multi_output = len(outputfiles) > 1
         
        if not multi_output:
            fout = open(outputfiles[0],'w')
        
        is_primary = True
        taxa = TaxonNamespace()
            
        for i,filein in enumerate(inputfiles):
            if multi_output:
                fout = open(outputfiles[i],'w')
            with open(filein,'r') as fin:
                strings = fin.readlines()       
                for s in strings:
                    tree = Tree.get(data=s,schema="newick",taxon_namespace=taxa,rooting="force-rooted")
                    if is_primary:
                        label_mapping, labelID = label_primary_tree(tree)
                        is_primary = False
                    else:
                        label_mapping, labelID = label_secondary_tree(tree,label_mapping,labelID)
                    fout.write(tree.as_string("newick"))
            if multi_output:
                fout.close()
        
        if not multi_output:        
            fout.close()                                     

if __name__=="__main__":
    main()                                
