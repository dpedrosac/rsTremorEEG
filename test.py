
def countdown(n):
    """ very simple function intended to provide a countdown going form n to zero backwards """

    import time
    for count in reversed(range(1, n + 1)):
        print(count)
        time.sleep(1)
    print('Tadaaa!')


def multiplication(k=10, n=5):
    """ simple function which multiplies two values, or - in case only one is defined - one value witha  default """

    result = k*n
    return result
