def prob_1 (a):
	return (a%2==0)

def prob_2 (f):
	return((f-32)/1.8)

def prob_3 (b,p):
	return (b**p)

def prob_4 (h,l):
	inz=(l-len(h))
	der=l-(inz+len(h))
	return inz+h+der

def prob_5 (a,b),(c,d):
	return ((a*c)+(b*d))