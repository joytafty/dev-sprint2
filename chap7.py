# Enter your answrs for chapter 7 here
# Name: Tharathorn (Joy) Rimchala


# Ex. 7.5
def estimate_pi():
	from math import sqrt
	k = 0
	x = SRsum(k)
	lastterm = x
	coef = 2*sqrt(2)/9801
	while True:
		if (lastterm < 1e-15):
			print "Done!"
			break
		else:
			k = k+1
			lastterm = SRsum(k+1)
			x = x + lastterm
			print "k = " + str(k) + " : est = " + str(1.0/(coef*x))

def SRsum(k):
	from math import factorial
	num1 = factorial(4*k)
	num2 = 1103.0 + 26390.0*k
	den1 = factorial(k)**(4.0)
	den2 = 396**(4*k)
	out = (num1*num2)/(den1*den2)
	return out

estimate_pi()