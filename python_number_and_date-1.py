

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


# Question2： Perform precise floating point arithmetic
def perform_precise_floating_point_arithmetic():
    a = 4.2
    b = 2.1
    print((a + b) == 6.3)

    # if you want use precise floating point arithmetic and accept some
    # performance loss. you can use decimal module
    from decimal import Decimal
    a = Decimal('4.2')
    b = Decimal('2.1')
    print((a+b) == Decimal('6.3'))

    # One of the main features of the decimal module is that it allows you to
    # control every aspect of your calculations
    from decimal import localcontext
    a = Decimal('1.3')
    b = Decimal('1.7')
    print(a / b)
    with localcontext() as ctx:
        ctx.prec = 3
        print(a / b)

    with localcontext() as ctx:
        ctx.prec = 50
        print(a / b)

    # You also have to pay attention to the effects of subtraction and the
    # addition of large and small numbers
    nums = [1.23e+18, 1, -1.23e+18]
    print(sum(nums))

    # To fixed it
    import math
    print(math.fsum(nums))


def print_number_of_format():
    x = 1234.56789
    # Two decimal places of accuracy
    print( format(x, '0.2f'))
    # Right justified in 10 chars, one-digit accuracy
    print(format(x, '>10.1f'))
    # Left justified
    print(format(x, '<10.1f'))
    # Centered
    format(x, '^10.1f')
    # Inclusion of thousands separator
    print(format(x, ','))
    print(format(x, '0,.1f'))

    # You can use index notation
    print(format(x, 'e'))
    print(format(x, '0.2E'))

    print('The value is {:0,.2f}'.format(x))

    # When the number of digits is specified, the resulting value is rounded
    # off according to the same rules as the round() function.
    print(format(x, '0.1f'))
    print(format(-x, '0.1f'))

    # If you need to display thousands of spaces by region, you need to
    # investigate the functions in the locale module. You can also use the
    # string's translate() method to exchange thousands of characters.
    swap_separators = {ord('.'): ',', ord(','): '.'}
    print(format(x, ',').translate(swap_separators))

    # Don't use % to represents
    print('%0.2f' % x)
    print('%10.1f' % x)
    print('%-10.1f' % x)


if __name__ == '__main__':
    # rounding_operation_in_floating_point_number()

    # perform_precise_floating_point_arithmetic()

    print_number_of_format()