def is_prime(num):
    if num <2:
        return False

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
number = int(input("Enter your Number: "))

if is_prime(number):
    print(f"{number} is a Prime Number")
else:
    print(f"{number} is not a prime number")