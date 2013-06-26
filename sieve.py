import math
import sys

"""
	Takes an integer limit and returns a list 
	containing all prime numbers less than it.

	Param:	limit		- int representing the upper limit
	Return:	primes		- list containing all primes less than limit
	Throws:	MemoryError	- if the limit entered is too large
"""
def sieve(limit):
	assert type(limit) == int

	# Booleans represent whether their corresponding indices are prime
	# (Composite numbers are marked false by the algorithm)
	try:
		nums = [True]*(limit)
		nums[0] = nums[1] = False
	except MemoryError as e:
		e.message = "Memory Error: Integer limit passed to function seive() is too large"
		raise

	# Iterate through the possible factors:
	for i in range(2, int(math.sqrt(limit))):

		# If the number hasn't already been marked as composite,
		# mark its multiples false - i.e. composite - beginning at i**2
		# (since all smaller multiples of i will have already been marked)
		if nums[i]:
			for j in range(i**2, limit, i):
				nums[j] = False

	# Put all the primes in a list
	primes = []
	for i in range(limit):
		if nums[i]:
			primes.append(i)

	# Return the list of all primes found:
	return primes
	

## MAIN:

if __name__ == "__main__":
	try:
		limit =	int(sys.argv[1])
	except ValueError as e:
		print "Value Error: Command line argument must be an integer"

	try:
		primes = sieve(limit)

		print "Number of primes found: " + str(len(primes))
		print "Primes:"
		for i in range (len(primes)):
			print str(primes[i]) + "\t",
			if i%10 == 9:
				print
		print

	except Exception as e:
		print e.message


