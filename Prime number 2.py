__author__ = 'Ben'

def prime(a):

    if a == 1:

        return False

    elif a == 2:

        return True

    else:

        for x in range(2,a):

            if a % x == 0:

                return False

            return True

def fact(a):

    factors = []

    if a == 1:

        return [1]

    else:

        for x in range(1,a):


            if a % x == 0:

                if prime(x):

                    if x not in factors:

                        factors.append(x)

    return factors




while 1:
    print fact(int(raw_input("Fact: ")))