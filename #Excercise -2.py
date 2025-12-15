#Excercise -2
#Prime Number Generator


try:
    # Take first number from the user and convert it to integer
    first = int(input("Enter the start of range: "))

    # Take second number from the user and convert it to integer
    second = int(input("Enter the end of range: "))

    # Check if both numbers are positive
    if first <= 0 or second <= 0:
        raise ValueError("Numbers must be positive integers.")

    # Check if start is greater than end
    if first > second:
        raise ValueError("Start value must be less than or equal to end value.")

    # Counter to control printing 10 primes per line
    count = 0

    # Loop through each number in the given range
    for i in range(first, second + 1):

        # Prime numbers must be greater than 1
        if i > 1:

            # Assume the number is prime initially
            is_prime = True

            # Check divisibility from 2 to square root of i
            for j in range(2, int(i ** 0.5) + 1):

                # If i is divisible by j, it is not prime
                if i % j == 0:
                    is_prime = False
                    break  # Exit the loop early

            # If number is prime, print it
            if is_prime:
                print(f"{i:5}", end=" ")
                count += 1  # Increase prime counter

                # Print a new line after every 10 primes
                if count % 10 == 0:
                    print()

    # If no prime numbers were found
    if count == 0:
        print("No prime numbers found in this range.")

# Handle invalid numeric input
except ValueError as ve:
    print("Input Error:", ve)

# Handle any unexpected error
except Exception:
    print("An unexpected error occurred. Please try again.")
