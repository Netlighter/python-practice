import math


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
