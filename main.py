import math

# from pprint import pp
# from test_a import internal


def f11(x, y, z):
    return math.sqrt(35 ** 3 - z ** 7) - (62 * z ** 8 - y ** 7) - (97 * y ** 7 + y ** 2) / (48 * x ** 6 - 5 * z)


# print('1. %.2e' % f1(79, -93, -87))
# print('2. %.2e' % f1(-44, 43, -61))
# print('-')


def f12(x):
    if x < -29:
        return x ** 5 - abs(x) - 11

    elif -29 <= x < 71:
        return (x ** 5 / 47) - x ** 3 - 5
    elif 71 <= x < 89:
        return x - 50 * x ** 2
    elif 89 <= x < 170:
        return (math.log(x) + 5 * x ** 7) ** 4 + math.cos(x)
    elif x >= 170:
        return x ** 8 + 87 * x ** 7 - 4


# print('1. %.2e' % f2(259))
# print('2. %.2e' % f2(254))
# print('-')


def f13(n, m):
    # sum_one = 0
    # sum_two = 0
    # for i in range(1, n+1):
    #     for j in range(1, m+1):
    #         sum_one += 87 * (j) ** 3 - (j) ** 8
    #         sum_two += math.log(i) + 5 * (i) ** 8
    # sum_one *= 24
    # sum_two /= 87
    #
    # return sum_one - sum_two

    return 24 * sum([87 * j ** 3 - j ** 8 for j in range(1, m + 1) for i in range(1, n + 1)]) \
           - sum([math.log(i) + 5 * i ** 8 for j in range(1, m + 1) for i in range(1, n + 1)]) / 87


# print('1. %.2e' % f13(40, 81))
# print('2. %.2e' % f13(87, 85))
# print('-')


def f14(n):
    if n < 0:
        return 0
    elif n == 0:
        return 7
    else:
        return math.sin(f14(n - 1)) + math.tan(f14(n - 1))


# print('1. %.2e' % f4(2))
# print('i2. %.2e' % f4(4))

def f21(x):
    if x[1] == 'coq':
        if x[2] == 'elm':
            if x[0] == 1965:
                if x[3] == 1993:
                    return 0
                elif x[3] == 2000:
                    return 1
            elif x[0] == 1990:
                return 2
        elif x[2] == 'jflex':
            return 3
        elif x[2] == 'diff':
            if x[4] == 'muf':
                if x[0] == 1965:
                    return 4
                elif x[0] == 1990:
                    return 5
            elif x[4] == 'cirru':
                if x[3] == 1993:
                    return 6
                elif x[3] == 2000:
                    return 7
            elif x[4] == 'xojo':
                if x[0] == 1965:
                    return 8
                elif x[0] == 1990:
                    return 9
    elif x[1] == 'terra':
        return 10
    elif x[1] == 'mql4':
        return 11


# print(f21([1965, 'mql4', 'diff', 2000, 'xojo']))
# print(f21([1990, 'terra', 'diff', 2000, 'xojo']))

def f22(code):
    g = (code & ((2 ** 32 - 1) & ~(2 ** 31 - 1))) >> 9
    f = (code & ((2 ** 31 - 1) & ~(2 ** 25 - 1))) >> 25
    e = (code & ((2 ** 25 - 1) & ~(2 ** 21 - 1))) << 2
    d = (code & ((2 ** 21 - 1) & ~(2 ** 12 - 1))) >> 6
    c = (code & ((2 ** 12 - 1) & ~(2 ** 9 - 1))) << 18
    b = (code & ((2 ** 9 - 1) & ~(2 ** 7 - 1))) << 23
    a = (code & (2 ** 7 - 1)) << 15
    return b | c | e | g | a | d | f


# print(f22(0x69223c65))
# print(0x34b288f4)

def f23(table):
    i = 0
    while i < len(table) - 1:
        j = i + 1
        while j < len(table):
            if table[i] == table[j]:
                del table[j]
                j -= 1
            j += 1
        i += 1

    while j < len(table) - 1:
        i = j + 1
        while i < len(table):
            if table[i] == table[j]:
                del table[i]
                i -= 1
            i += 1
        j += 1

    clean = [[val for val in row if val] for row in table]
    split = [[*row[0].split('!')[::-1], row[1]] for row in clean]
    rule = '{}{} ({}{}{}) {}{}{}-{}{}-{}{}'
    # ‐
    pretty = [
        [
            rule.format(*r[0]),
            r[1].split('@')[0],
            '.'.join(r[2][2:].split('/')[::-1])
        ]
        for r in split]
    transp = [list(i) for i in zip(*pretty)]
    result = [transp[0], transp[2], transp[1]]
    return result


# pp(internal[0][0])
# print('-----')
# pp(f23(internal[7][0])[0] + internal[7][1][0])
# pp(f23(internal[0][0]))
# pp(internal[0][1])