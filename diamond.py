import sys
import random


class Diamond():
	def __init__(self, size, randomm=False):
		self.size=size
		self.randomm = randomm

	def __str__(self):
		return str(self.get())

	def get_line(self, size, i, charr="*"):
		obj = (" "*(size-i))+(charr*i)+(charr*(i-1))
		obj += "\n"
		return obj

	def get_rand_line(self, size, i, seed=random.randrange(33,127)):
		obj = (" "*(size-i))+(chr(seed)*i)+(chr(seed)*(i-1))
		obj += "\n"
		return obj

	def get(self, true_random=False, charr="*"):
		buff=""
		if self.randomm:
			for i in range(size):
				buff += self.get_rand_line(size, i)
			for i in range(size, 0, -1):
				buff += self.get_rand_line(size, i)
		else:
			for i in range(size):
				if true_random:
					buff += self.get_rand_line(size, i, random.randrange(33,127))
				else:
					buff += self.get_line(size, i, charr)
			for i in range(size, 0, -1):
				if true_random:
					buff += self.get_rand_line(size, i, random.randrange(33,127))
				else:
					buff += self.get_line(size, i, charr)
		return buff


# defaults
size = 5
true_rand = False
charr="*"

if len(sys.argv) > 1:
	size = int(sys.argv[1])

if len(sys.argv) > 2:
	charr = str(sys.argv[2])

if len(sys.argv) > 3:
	true_rand = bool(str(sys.argv[3]))

if __name__ == "__main__":
	dd = Diamond(size)
	print(dd.get(true_rand, charr))  # prints the diamond
