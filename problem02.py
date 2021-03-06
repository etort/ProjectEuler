"""Project Euler Problem 2 by Teddy Tortorici
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2,
the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.
"""


''' -- Old code. But want to make it more efficient
def fibonacci_sequence(a0, a1, x):
    """creates a Fibonacci sequence generated by seeds a0 and a1
    a0 - the first seed
    a1 - the second seed
    x - the number to which the Fibonacci sequence terminates by"""
    seq = [a0, a1]
    next_term = 0
    while next_term < x:
        next_term = seq[-1]+seq[-2]
        seq.append(next_term)
    return seq
'''


def fibonacci_sequence_even_sum(end):
    """Since every 3rd term is even, we can take some short cuts
    end - where the Fibonacci sequence terminates
    output - sum of even terms in the Fibonacci sequence terminating at end"""
    last_term = 1
    next_term = 2
    total = next_term
    while True:
        temp_last_term = last_term + 2 * next_term
        next_term = 2 * last_term + 3 * next_term   # guaranteed to be an even term because every 3rd term is even
        if next_term > end:
            break
        last_term = temp_last_term
        total += next_term
    return total


if __name__ == "__main__":
    print(fibonacci_sequence_even_sum(4e6))
    ''' -- for running with old defintion
    fib_seq = fibonacci_sequence(1, 2, 4e6)
    sum = 0
    for i in fib_seq:
        if i % 2 == 0:
            sum = sum+i
    print(sum)
    '''