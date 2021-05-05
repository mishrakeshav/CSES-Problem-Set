def main():
    import sys
    input = sys.stdin.readline
    PRINT = sys.stdout.write
    n, m, q = map(int, input().split())
    n += 1
    f = 2**39
    T = n*n*[f]
    for i in range(0,n*n,n+1): T[i] = 0
    for _ in range(m):
        a, b, c = map(int, input().split())
        T[a*n+b] = min(T[a*n+b], c)
        T[b*n+a] = min(T[b*n+a], c)
    for k in range(n):
        K = k*n
        for a in range(n):
            A = a*n
            s = T[A+k]
            for b in range(n):
                T[A+b] = min(T[A+b], s+T[K+b])
    for i in range(n):
        I = i*n
        for j in range(n):
            if T[I+j] == f:
                T[I+j] = -1
    for _ in range(q):
        a, b = map(int, input().split())
        PRINT(str(T[a*n+b])+"\n")
main()