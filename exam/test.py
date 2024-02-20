def Ackfun(m, n):
    if m == 0:
        return n + 1
    elif m != 0 & n == 0:
        return Ackfun(m - 1, 1)
    else:
        return Ackfun(m - 1, Ackfun(m, n - 1))


if __name__ == '__main__':
    print(Ackfun(4, 5))
