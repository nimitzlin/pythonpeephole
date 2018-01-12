def fib(n):
	return fib(n - 1) + fib(n - 2) if n > 1 else n
import dis

def test2(n):
	b = n + 1

	return b

def test3(n):
	return

def test4(n):
	return True

dis.dis(fib)
dis.dis(test2)
dis.dis(test3)
dis.dis(test4)
print fib(10) 
print test2(10) 
print test3(10) 
print test4(10) 
