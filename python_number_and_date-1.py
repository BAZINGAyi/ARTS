

# Question1: You want to perform a rounding operation with a specified
# precision on a floating point number.
def rounding_operation_in_floating_point_number():
    # Use the round Func
    print(round(1.23, 1))
    print(round(1.27, 1))
    print(round(-1.23, 1))
    print(round(1.25361, 3))

    # when the value is the middle of boundary, round() can returns
    # the even number closest to it.
    print(round(1.5, 0))
    print(round(2.5, 0))

    # The rounding operation will work on ten, hundred, thousand, and so on.
    a = 1627731
    print(round(a, -1))
    print(round(a, -2))
    print(round(a, -3))

    # Don't confuse rounding and formatting output
    x = 1.23456
    print(format(x, '0.2f'))
    print('value is {:0.3f}'.format(x))

    # Don't try to round the floating point value to "fix" the problem
    # that looks correct on the surface.
    a = 2.1
    b = 4.2
    c = a + b
    print(c)
    # Wrong operation
    c = round(c, 2)  # "Fix" result (???)
    print(c)
    # For example, involving financial collars, you need to the decimal module


if __name__ == '__main__':
    rounding_operation_in_floating_point_number()