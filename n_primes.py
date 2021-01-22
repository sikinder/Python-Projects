n = int(input("Enter a value for n,Range until the prime numbers are needed: "))
def print_primes(n):
    prime_nums = []
    for num in range(n):
        if num > 1: 
            for i in range(2, num//2):
                if (num % i) == 0: 
                    break
            else:
                prime_nums.append(num)
    print(prime_nums)
print_primes(n)
