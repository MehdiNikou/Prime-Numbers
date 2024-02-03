# Count the number of prime numbers and Show all prime numbers.
import datetime
a = datetime.datetime.now()
 
def primeNumbers(n):
    count_prime_numbers = 0
    for num in range(2, n+1):
        x = 0
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                x = +1
                break
        if x == 0:
            count_prime_numbers += 1    # Count the number of prime numbers.
            print(f"{num}")    # Show all prime numbers.
    print(f"{count_prime_numbers}")

n = 100000
primeNumbers(n)        

b = datetime.datetime.now()
c = b - a
print(f"{c.total_seconds()} Seconds\n")