# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_n
import math

def main():
    N = int(input())
    prime_factors = []
    divided_number = N
    while True:
        divisor = min_divisor(divided_number)
        prime_factors.append(divisor)
        if divisor == divided_number:
            break
        divided_number = int(divided_number / divisor)
    print(' '.join([f'{num}' for num in prime_factors]))
    

def min_divisor(N):
    for i in range(2, int(math.sqrt(N)) + 2):
        if N % i == 0:
            return i
    return N

main()
