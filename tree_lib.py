import sys
from dendropy import Tree
from decompose_tree import decompose_by_diameter
from random import sample, random

def collapse_edges(t, nBr):
# collapse nBr shortest branches in t
   brList = []

   for node in t.postorder_node_iter():
        if not node.is_leaf() and node is not t.seed_node:
            brList.append(node) 
   brList.sort(key=lambda node:node.edge_length)
   
   if nBr > len(brList):
       return False 

   for i in range(nBr):
       print("Collapsing branch " + str(brList[i].label))
       if (collapse_edge(t,brList[i])):
            print("Successed")
       else:
            print("Could not collapse edge!")     

   return True

def collapse_edge(t,v):
# collapse the branch above node v in tree t
    if v.is_leaf() or v is t.seed_node:
        return False
    
    u = v.parent_node
    u.remove_child(v)
    
    Children = v.child_nodes()
    
    for c in Children:
        l = c.edge_length
        v.remove_child(c)
        u.add_child(c)
        c.parent_node = u
        c.edge_length = l
    
    return True    
            	


def sample_and_prune(a_tree, n_ingroups, n_outgroups=1):
    # Note: will prune the tree passed in 
    L = []
    C = a_tree.seed_node.child_nodes()
    current = []
    for node in a_tree.postorder_node_iter():
        if node in C:
            L.append((current,len(current)))
            current = []
        elif node.is_leaf():    
            current.append(node.taxon.label)

    en = 0
    ogs = None
    igs = None
            
    for i,item in enumerate(L):
        # check if we can sample outgroups from L[i] and ingroups from the rest
        listO,sO = item
        sI = sum([item[1] for item in L[:i]+L[i+1:]])

        if sO < n_outgroups or sI < n_ingroups:
            continue
        
        en += 1
        
        # compute the probability that we will pick this combination instead of the previous one
        prob = 1.0/en
        if random() > prob:
            # by chance this combination is not selected
            continue

        # sample n_outgroups from s
        ogs = sample(listO,n_outgroups)    
                             
        # sample n_ingroups from the rest
        listI = []
        for item in L[:i]+L[i+1:] :
            listI += item[0]

        igs = sample(listI,n_ingroups)
    
    if igs is not None and ogs is not None:    
        RS = [ x.taxon.label for x in a_tree.leaf_nodes() if x.taxon.label not in igs and x.taxon.label not in ogs ]
        prune_tree(a_tree,RS)       
        return True, igs,ogs

    return False, None, None    
    

def sample_with_outgroups(a_tree, n_ingroups, n_outgroups=1, n_reps=1):
# sample n_reps trees from a large tree, each has n_ingroups and n_outgroups taxa
    samples = []
    for i in range(n_reps):
        t = Tree(a_tree)
        check, igs, ogs = sample_and_prune(t, n_ingroups, n_outgroups=n_outgroups)
        if not check:
            return False, samples
        samples.append((t,igs,ogs))
        
    return True,samples            

def compute_diameter(tree_list):
    for t in tree_list:
        print(decompose_by_diameter(t)[0].seed_node.diameter)

def prune_node(T,node):
    if node is not T.seed_node:
        p = node.parent_node
        p.remove_child(node)
        if p.num_child_nodes() == 1:
            v = p.child_nodes()[0]
            p.remove_child(v)
            if p is T.seed_node:
                T.seed_node = v
            #    p.remove_child(v)
            else:
                u = p.parent_node
                l = p.edge_length + v.edge_length if v.edge_length is not None else None
                u.remove_child(p)
                u.add_child(v)
                v.edge_length = l



def prune_tree(T,RS):
# prune the taxa in the removing set RS from tree T
    L = list(T.leaf_node_iter())
    for leaf in L:
        if leaf.taxon.label in RS:
            prune_node(T,leaf)

def get_taxa(tree_file,scheme='newick'):
	a_tree = Tree.get_from_path(tree_file,scheme,preserve_underscores=True)
	return [leaf.taxon.label for leaf in a_tree.leaf_nodes()]

def report_taxa(tree_file,scheme='newick',listing=True,counting=True):
	a_tree = Tree()
	a_tree.read_from_path(tree_file,scheme)
	if listing:
		for leaf in a_tree.leaf_nodes():
			print(leaf.taxon.label)
	if counting:
		print('Taxa #: ' + str(len(a_tree.leaf_nodes())))

def tree_as_newick(a_tree,outfile=None,append=False):
# dendropy's method to write newick seems to have problem ...
	if outfile:
		outstream = open(outfile,'a') if append else open(outfile,'w')
	else:
		outstream = sys.stdout

	__write_newick(a_tree.seed_node,outstream)

	outstream.write(";\n")
	if outfile:
		outstream.close()	

def __write_newick(node,outstream):
	if node.is_leaf():
			if node.taxon:
				outstream.write(node.taxon.label)
			else:
				outstream.write(str(node.label))
	else:
		outstream.write('(')
		is_first_child = True
		for child in node.child_node_iter():
			if is_first_child:
				is_first_child = False
			else:
				outstream.write(',')
			__write_newick(child,outstream)
		outstream.write(')')
	if not node.is_leaf() and node.label is not None:
			outstream.write(str(node.label))

	if not node.edge_length is None:
		outstream.write(":"+str(node.edge_length))
