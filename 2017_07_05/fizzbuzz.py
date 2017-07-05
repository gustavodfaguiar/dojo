from functools import partial

multiple_of = lambda base, num: num % base == 0
multiple_of_5 = partial(multiple_of, 5)
multiple_of_3 = partial(multiple_of, 3)


def fizzbuzz(position):
	say = str(position)

	if multiple_of_3(position) and multiple_of_5(position):
		say = 'fizzbuzz'
	elif multiple_of_3(position):
		say = 'fizz'
	elif multiple_of_5(position):
		say = 'buzz'


	return say


if __name__ == '__main__':
	assert fizzbuzz(1) == '1'
	assert fizzbuzz(2) == '2'
	assert fizzbuzz(4) == '4'

	assert fizzbuzz(3) == 'fizz'
	assert fizzbuzz(6) == 'fizz'
	assert fizzbuzz(9) == 'fizz'

	assert fizzbuzz(5) == 'buzz'
	assert fizzbuzz(10) == 'buzz'
	assert fizzbuzz(20) == 'buzz'

	assert fizzbuzz(15) == 'fizzbuzz'
	assert fizzbuzz(30) == 'fizzbuzz'
	assert fizzbuzz(45) == 'fizzbuzz'