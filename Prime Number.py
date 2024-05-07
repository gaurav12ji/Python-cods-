# Prime Number
def prime_checker(numebr):
    is_prime = True
    for i in range(2,numebr):
        if numebr % i == 0:
            is_prime = False    
    if is_prime:
        print("is prime number")
    else:
        print("it's not prime numner")
n = int(input())
prime_checker(numebr=n)