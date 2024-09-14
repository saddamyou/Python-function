def bisection_root(x, epsilon=1e-6):
    low = 0.0
    high = x
    guess = (low + high) / 2.0

    while abs(guess**2 - x) >= epsilon:
        if guess**2 < x:
            low = guess
        else:
            high = guess
        guess = (low + high) / 2.0

    return guess

def count_nums_with_sqrt_close_to(n, epsilon):
    count = 0
    for i in range(n ** 3):
        # take the sqrt of i using bisection method
        sqrt = bisection_root(i)
        if abs(n - sqrt) < epsilon:
            # know that sqrt within epsilon
            count += 1
    return count

# Example usage:
n = 5
epsilon = 0.1
print(count_nums_with_sqrt_close_to(n, epsilon))
