# Iterate through the numbers from 1-50.
for fizzbuzz in range(51):

    # Check if the numbers are divisible by 3 and 5.
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print('FizzBuzz') # if so print FizzBuzz instead
        continue

    # Check if the numbers are divisible by 3.
    elif fizzbuzz % 3 == 0:
        print ('Fizz') # if so print Fizz instead of the number
        continue

    # Check is divisible by 5.
    elif fizzbuzz % 5 == 0:
        print('Buzz') # prints Buzz if so.
        continue

    print(fizzbuzz) # if none of the conditions are met it prints the number itself.

