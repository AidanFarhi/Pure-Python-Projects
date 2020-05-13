def gcd(a, b):
    r0 = a
    r1 = b
    while r1:
        r2 = r0 % r1
        r0 = r1
        r1 = r2
    return r0


def num(f):
    f = f.split('/')
    nf = int(f[0])
    return nf


def den(f):
    f = f.split('/')
    if len(f) == 1:
        return 1
    else:
        df = int(f[1])
        return df


def reduce(f):
    n = num(f)
    d = den(f)
    # regularization of the fraction
    g = gcd(n,d)
    n = n//g
    d = d//g
    if d < 0:
        n *= -1
        d *= -1

    if d == 1:
        return str(n)
    else:
        return str(n)+'/'+str(d)


def decimal(f):
    return num(f)/den(f)


def add(f1, f2):
    n1 = num(f1)
    d1 = den(f1)
    n2 = num(f2)
    d2 = den(f2)

    n = n1*d2+d1*n2  # the numerator of the sum
    d = d1*d2 # the denominator of the sum
    f = reduce(str(n) + '/' + str(d))
    return f


def sub(f1, f2):
    n1 = num(f1)
    d1 = den(f1)
    n2 = num(f2)
    d2 = den(f2)

    n = n1 * d2 - d1 * n2
    d = d1 * d2
    f = reduce(str(n) + '/' + str(d))
    return f


def mul(f1, f2):
    n1 = num(f1)
    d1 = den(f1)
    n2 = num(f2)
    d2 = den(f2)

    n = n1 * n2
    d = d1 * d2
    f = reduce(str(n) + '/' + str(d))
    return f

def div(f1, f2):
    n1 = num(f1)
    d1 = den(f1)
    n2 = num(f2)
    d2 = den(f2)

    n = n1 * d2
    d = d1 * n2

    if n == 0:
        return print("Cannot divide by zero")
    elif d == 0:
        return print("Cannot divide by zero")
    else:
        b = reduce(str(n) + '/' + str(d))
        a = print(f"{f1} / {f2} = {b}")
        return a


def main():
    while True:
        ans = input('Press q to quit or a pair of fractions or ints  to continue: ')
        if ans == 'q':
            break
        ans = ans.split(' ')
        f = reduce(ans[0])
        g = reduce(ans[1])

        # addition
        s = add(f, g)
        print('{} + {} = {}'.format(f,g,s))

        fd = decimal(f)
        gd = decimal(g)
        sd = decimal(s)
        print('{} + {} = {}'.format(fd,gd,sd))

        ##########################################
        # place your code here
        # subtraction
        diff = sub(f, g)
        print('{} - {} = {}'.format(f, g, diff))

        # multiplication
        mult = mul(f, g)
        print('{} x {} = {}'.format(f, g, mult))

        # division
        div(f, g)


main()