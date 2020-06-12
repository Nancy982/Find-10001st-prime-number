#Nancy Medina
#Math330 Section 2
#PE07

#Project Euler: Problem 7
#What is the 10001st prime number?

#create a funtion named isPrime, this will check if a number is prime or not
def isPrime(n):
    if n < 2: return 0
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

#create a funtion named primeNumber, this will check the prime number you want.
def primeNumber(n):
    a = 0
    prime = 1

    #create a while loop that will go through every prime number until it reaches the one you chose.
    while a < n:
        prime += 1
        if isPrime(prime):
            a += 1
    return prime

#print the 10001st prime number
print("The 10001st prime number is",primeNumber(10001))
