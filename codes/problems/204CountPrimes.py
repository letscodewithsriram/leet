"""
204. Count Primes

Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

def countPrimes(self, n: int) -> int:
"""

# Using Sieve of Eratosthenes Algorithm
# Runtime: 360 ms, faster than 80.55% of Python3 online submissions for Count Primes.
# Memory Usage: 25.6 MB, less than 79.31% of Python3 online submissions for Count Primes.

def count_primes(max_number) -> int:
    """
    Functions identifies the number of prime numbers within the range
    :param : [integer] - Non-Negative Integer
    :return : [integer] - Count | No of primes below the number
    """

    if max_number <= 2:
        return 0

    if max_number == 3:
        return 1

    prime_counter = 2
    prime_matrix = [True] * max_number

    while prime_counter * prime_counter < max_number:
        if prime_matrix[prime_counter]:
            # print(prime_counter, prime_matrix[prime_counter])
            for i in range(prime_counter * prime_counter, max_number, prime_counter):
                prime_matrix[i] = False
                # print(i, end=" ")

        prime_counter += 1
        # print("\n")

    print("Final List is here!!")

    for prime_idx, prime_flag in enumerate(prime_matrix):
        if prime_flag:
            print(prime_idx, prime_flag, end=" ")
    print("\n")
    return prime_matrix.count(True) - 2


print(count_primes(11))
