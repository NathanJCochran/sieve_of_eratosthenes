import math
import sys

"""
	Takes an integer limit and returns a list 
	containing all prime numbers less than the limit.

	Param:	limit		- int representing the upper limit
	Return:	primes		- list containing all primes less than limit
	Throws:	MemoryError	- if the limit entered is too large
"""
def sieve(limit):
	assert type(limit) == int

	# The booleans in this array map to possible primes (here, odd numbers >=3 - an optimization)
	# via the _idx_to_num() and _num_to_idx() functions. Booleans corresponding
	# to composite numbers will be marked false by the algorithm:
	try:
		nums = [True]*((limit/2)-1)

	except MemoryError as e:
		e.message = "Memory Error: Integer limit passed to function seive() is too large"
		raise

	# Iterate through the possible factors (odd numbers >= 3 and < sqrt(limit):
	for i in range(3, int(math.sqrt(limit)), 2):

		# If the number hasn't already been marked as composite, it's prime,
		# so mark its multiples false - i.e. composite - beginning at i**2
		# (since all smaller multiples of i will have already been marked)
		# and stepping by 2*i to avoid accidentally attempting to map even numbers:
		if nums[_num_to_idx(i)]:
			for j in range(i**2, limit, 2*i):
				nums[_num_to_idx(j)] = False

	# Put all the primes in a list:
	primes = []
	if limit>2:
		primes.append(2)
	for i in range(len(nums)):
		if nums[i]:
			primes.append(_idx_to_num(i))

	# Return the list of primes:
	return primes
	

"""
	Takes a possible prime (odd number >= 3) and returns
	its corresponding index in the boolean array.
"""
def _num_to_idx(num):
	return (num-3)/2


"""
	Takes an index of the boolean array and returns the
	possible prime (odd number >= 3) it represents.
"""
def _idx_to_num(idx):
	return (idx*2)+3


## MAIN:

if __name__ == "__main__":
	try:
		limit =	int(sys.argv[1])
	except ValueError as e:
		print "Value Error: Command line argument must be an integer"
		sys.exit(0)

	try:
		# Calls sieve():
		primes = sieve(limit)

		# Prints the primes returned, with tabs between numbers:
		print "Primes:"
		for i in range (len(primes)):
			print str(primes[i]) + "\t",

			# Ensures that there are only ten columns per row:
			if i%10 == 9:
				print

		print "\nNumber of primes found: " + str(len(primes))

	except MemoryError as e:
		print e.message


