import sys
from dendropy import Tree

def get_taxa(tree_file,scheme='newick'):
	a_tree = Tree()
	a_tree.read_from_path(tree_file,scheme)
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
