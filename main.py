import sys
from math import gcd


def stupid(a, k):
	n = len(a)
	k = (n + k) % n

	_gcd = gcd(n, k)

	for j in range(_gcd):
		i = j

		tmp = a[j + k]
		while i != j + k:
			a[(i + k) % n] = a[i]
			i = (i - k + n) % n

		a[(j + k + k) % n] = tmp
	
	return a


def cool(a, k):
	k %= len(a)

	a.reverse()

	return list(reversed(a[:k])) + list(reversed(a[k:]))


if __name__ == '__main__':	
	n, k = [int(i) for i in sys.argv[1:]]
	
	a = list(range(n))
	
	def pprint(a):	
		if len(a) < 20:
			print (a)

	pprint(a)
	pprint ( cool(list(a), k) ) 
	pprint ( stupid(list(a), k) ) 
	
