e = 10**-5


def fx(coefficients: list, point):
    result = 0
    degree = 0
    for i in reversed(coefficients):
        result += i * (point**degree)
        degree += 1
    return result


def derivative(coefficients: list):
    new_coefficients = []
    degree = 0
    for i in reversed(coefficients):
        new_coefficients.append(i * degree)
        degree += 1
    new_coefficients.remove(0)
    new_coefficients.reverse()
    return new_coefficients


def bisection_method(coefs: list, a, b):
    iter = 1
    print("This is bisection method! ")
    while abs(a-b) >= e:
        c = (a + b) / 2
        if (fx(coefs, a) * fx(coefs, c)) <= 0:
            b = c
        elif (fx(coefs, b) * fx(coefs, c)) <= 0:
            a = c
        else:
            print("There is no root in this function!")
            return
        root = (a + b) / 2
        print("Iteration №", iter, ", approximate root value = ", root, ", interval length = ", abs(a-b), sep="")
        iter += 1
    print("Your answer = ", root, end="\n\n")


def chord_method(coefs: list, a, b):
    print("This is chord method! ")
    c = ((a * fx(coefs, b)) - (b * fx(coefs, a))) / (fx(coefs, b) - fx(coefs, a))
    iter = 1
    while abs(fx(coefs, c)) >= e:
        c = ((a * fx(coefs, b)) - (b * fx(coefs, a))) / (fx(coefs, b) - fx(coefs, a))
        if (fx(coefs, a) * fx(coefs, c)) <= 0:
            b = c
        elif (fx(coefs, b) * fx(coefs, c)) <= 0:
            a = c
        else:
            print("There is no root in this function!")
            return
        root = c
        print("Iteration №", iter, ", approximate root value = ", root, ", interval length = ", abs(fx(coefs, c)), sep="")
        iter += 1
    print("Your answer = ", root, end="\n\n")


def newton_method(coefs: list, a, b):
    print("This is newton method! ")
    f1 = fx(coefs, a) * fx(derivative(derivative(coefs)), a)
    if f1 > 0:
        x0 = a
    else:
        x0 = b
    iter = 1
    while abs(fx(coefs, x0) / fx(derivative(coefs), x0)) >= e:
        root = x0 - (fx(coefs, x0) / fx(derivative(coefs), x0))
        x0 = root
        print("Iteration №", iter, ", approximate root value = ", root, ", interval length = ", abs(fx(coefs, x0) / fx(derivative(coefs), x0)), sep="")
        iter += 1
    print("Your answer = ", root)


if __name__ == '__main__':
    bisection_method([1, 1, -2, -9, -3, -2], 0.5432, 4)
    chord_method([1, 1, -2, -9, -3, -2], 0.5432, 4)
    newton_method([1, 1, -2, -9, -3, -2], 0.5432, 4)
