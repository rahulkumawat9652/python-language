def is_prime(num):
    factors = 0
    for i in range(1,num + 1):
        if num%i ==0:
            factors +=1
    if factors == 2:
        print("it is a prime number")
    else:
        print("it is a not prime number")
is_prime(10)