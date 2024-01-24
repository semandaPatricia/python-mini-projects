

import random

# Generate a list of 6 random numbers between 0 and 20
random_numbers = [random.randint(0, 20) for _ in range(6)]

print("Generated random numbers:", random_numbers)

# Check and print even numbers
even_numbers = []
for num in random_numbers:
    if num % 2 == 0:
        print(f"{num} is an even number.")
        even_numbers.append(num)
    else:
        print(f"{num} is an odd number.")

# Print even numbers separately
if even_numbers:
    print("Even numbers in the list:", even_numbers)
else:
    print("No even numbers found.")


