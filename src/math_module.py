from math import sin as rsin, cos as rcos, tan as rtan, pi, e, degrees, radians, log, asin as rasin, \
    acos as racos, atan as ratan, sqrt


def sin(x):
    return rsin(radians(x))


def cos(x):
    return rcos(radians(x))


def tg(x):
    return rtan(radians(x))


def ctg(x):
    return 1 / (tg(x))


def arcsin(x):
    return degrees(rasin(x))


def arccos(x):
    return degrees(racos(x))


def arctg(x):
    return degrees(ratan(x))


def arcctg(x):
    return 90 - degrees(ratan(x))


def log2(x):
    return log(x, 2)


def log10(x):
    return log(x, 10)


def calculate(expression, var):
    x = var
    return eval(expression)


if __name__ == '__main__':  # For unit-testing.
    print(calculate(input()))

# Maybe later.
'''def calculate(expression):
    try:
        num = int(expression)
        return num
    except ValueError:
        if '(' in expression and ')' in expression:
            while expression[0] == '(' and expression[-1] == ')':
                expression = expression[1:-1]
            print(expression)'''
