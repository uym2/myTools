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
			print leaf.taxon.label
	if counting:
		print 'Taxa #: ' + str(len(a_tree.leaf_nodes()))
