def trl_zero(k,dNum=0):
	s = str(k)
	if not dNum:
		return s
	dNum = dNum - len(s)
	while dNum > 0:
		s = '0'+s
		dNum = dNum -1
	return s
	
