def pascal_triangle(n):
    if n < 0 : return
    # n = 0
    T = [[1]]
    # loop for the next r = [1:n+1]
    for R in range(1, height + 2):
        # c == 0
        N = [1]
        # caculate [1:r) (exclude r itself)
        for C in range(1, R):
            a = T[R - 1][C - 1]
            b = T[R - 1][C]
            # c = a + b
            N.append(a + b)
        # c == r
        N.append(1)
        T.append(N)
    # print each R, from [0, n+1], total row is n+2
    for R in T:
        # i want to a pyramid, but the last row will
        # still have a single leading space
        print ' ' * (n - len(R) + 2),
        for C in R:
            print C,
        # new line
        print
