
def addNumber(a, b):
	sum = a + b
	return sum

def gt(a,b):
	if a>b:
		return a;
	else:
		return b;

def lt(a,b):
	not gt(a,b)

def eval(a, b, fn):
	if (fn(a,b) == a):
		return True
	else:
		return False

print(addNumber(1,2))

print(eval(3,5,gt))
print(eval(5,3,gt))