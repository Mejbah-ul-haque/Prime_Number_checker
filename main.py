def is_prime(num):
    if num == 2:
        return True
    if num == 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True

num = int(input("Enter a number: "))
if is_prime((num)):
    print(f"{num} is a Prime Number.")
else:
    print(f"{num} is NOT a Prime Number.")

