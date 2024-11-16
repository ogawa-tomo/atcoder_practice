def main():
    K = int(input())
    A, B = list(map(int, input().split()))
    n = A // K
    nK = n * K
    if nK == A or nK + K <= B:
        print("OK")
    else:
        print("NG")

main()