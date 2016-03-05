

def factorial_rec(n):
	if n == 0:
		return 1
	else:
		return n * factorial_rec (n-1)

def factorial_loop(n):
	result = 1
	for i in range(1,n+1):
		result = result * i
	return result

def multiply (x, y):
	return x * y

def factorial_fun_sim(n):
	return reduce(multiply,[1]+range(1,n+1))

def factorial_fun_lam(n):
	return reduce(lambda x,y:x*y,[1]+range(1,n+1))

def fib_rec(n):
	if n == 0 or n == 1:
		return n 
	else:
		return fib_rec(n-1) + fib_rec(n-2)

def fib_dp(n):
	results = [0,1]
	for i in range(2,n+1):
		results.append(results[i-1] + results[i-2])

	return results[n]

def fib_dp_dic(n):
	dic = {0:0, 1:1}
	for i in range(2,n+1):
		dic[i] = dic[i-1] + dic[i-2]

	return dic[n]


if __name__ == '__main__':
	'''print (factorial_rec(3))
	print (factorial_loop(5))
	print (factorial_fun_sim(6))
	print (factorial_fun_lam(7))
	print (fib_rec(10))
	print (fib_dp(100))
	print (fib_dp_dic(50))
	'''
	print (factorial_fun_sim(4))
