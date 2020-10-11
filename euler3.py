"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


def prime_numbers(number):
	primes = []
	i=2
	while number>i:
		if number%i:
			i+=1

		else:
			number//=i #Floor division -> Lower number 
			primes.append(i)

	if number>1:
		primes.append(number)


	print("El número primo factor más grande es", number)



prime_numbers(600851475143)








