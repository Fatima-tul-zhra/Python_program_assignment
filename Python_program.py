


name = input("Enter your name: ")

favourite_numbers = []
for i in range(1, 4):
    number = int(input(f"Enter your {i} favorite number: "))
    favourite_numbers.append(number)

print(f"\nHello, {name}! Let's explore your favorite numbers:")

even_odd_num = []
for number in favourite_numbers:
    if number % 2 == 0:
        even_odd_num.append((number, "even"))
    else:
        even_odd_num.append((number, "odd"))

for number, even_odd in even_odd_num:
    print(f"The number {number} is {even_odd}.")


for number in favourite_numbers:
    print(f"The number {number} and its square: ({number}, {number**2})")


sum_of_numbers = sum(favourite_numbers)
print(f"\nAmazing! The sum of your favorite numbers is: {sum_of_numbers}")


def prime_num(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
if prime_num(sum_of_numbers):
    print(f"Wow, {sum_of_numbers} is a prime number!")
else:
    print(f"{sum_of_numbers} is not a prime number.")


