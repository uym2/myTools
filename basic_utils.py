import argparse

def trl_zero(k,dNum=0):
	s = str(k)
	if not dNum:
		return s
	dNum = dNum - len(s)
	while dNum > 0:
		s = '0'+s
		dNum = dNum -1
	return s

	
def parseArg(opts,names=None,requires=None,helps=None):
	parser = argparse.ArgumentParser()
	for i in range(len(opts)):
		opt = "-"+opts[i]
		nm = "--"+names[i] if names else "--"+opts[i]
		rq = requires[i] if requires else False
		hp = helps[i] if helps else "Please fill in " + opt
		parser.add_argument(opt,nm,required=rq,help=hp)

	args = vars(parser.parse_args())
	
	return args

def binary_search(a_list,val,l=0,r=None,do_sort=False):
# by default, we assume that the list is already sorted
# if it is not the case, please call the function with do_sort=True
# note that do_sort WILL MODIFY the input list
	if do_sort:
		a_list.sort()
	if r is None:
		r = len(a_list)-1
	if l > r:
		return False
	med = int((r+l)/2)

	if val < a_list[med]:
		return binary_search(a_list,val,l,med-1)
	elif val > a_list[med]:
		return binary_search(a_list,val,med+1,r)
	else:
		return True
