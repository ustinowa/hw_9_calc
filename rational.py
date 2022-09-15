def r_sum(a, b):
    return a + b


def r_sub(a, b):
    return a - b


def r_mul(a, b):
    return a * b


def r_div(a, b):
    if b == 0:
        print("Нельзя делить на ноль")
        return None

    return a / b