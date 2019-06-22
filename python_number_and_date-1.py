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
    print((a + b) == Decimal('6.3'))

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
    print(format(x, '0.2f'))
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


# Question3: You need to format or print the Integer in binary,
# octal, or hexadecimal
def format_or_print_the_number():
    x = 1234
    print(bin(x))
    print(oct(x))
    print(hex(x))
    print(format(x, 'b'))
    print(format(x, 'o'))
    print(format(x, 'x'))
    # if you don't want to print the '0b' or '0o' or '0x', you can use the
    # format()
    print(format(x, 'b'))
    print(format(x, 'o'))
    print(format(x, 'x'))
    # If the integers are signed, so If you are dealing with negative numbers,
    # the output will contain a negative sign.
    x = -1234
    print(format(x, 'b'))
    print(format(x, 'x'))
    # If you want to produce a unsigned value, you need to add a indicate to
    # represents the value of the most length
    x = -1234
    print(format(2 ** 32 + x, 'b'))
    print(format(2 ** 32 + x, 'b'))
    print(format(2 ** 32 + x, 'x'))
    # transfer string to int
    print(int('4d2', 16))
    print(int('10011010010', 2))
    # But there are special in octal look like this:
    import os
    os.chmod('.test', 0o755)


# Question4: You have a byte string and want to extract it to an integer.
#  Or, you need to convert a large integer to a byte string.
def convert_or_extract_byte_string():
    """
     计算机中唯一存储的是字节，如果想要存储一些东西，必须将其转为字节。但字节并不是人类可以
     读的。比如你想存储音乐，要使用 MP3，WAV 的编码方式。要存储文本，要使用 ASCII 和 UTF8
     等编码方式。
     比如定义一个字节码字符串 a = b'Hello World'. 使用 print 打印后，会输出
     b`Hello World`. 但实际上，这时 python 编码之后输出的版本，真实的内容不无法阅读的
    """
    data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
    # To int
    len(data)  # 16
    print(int.from_bytes(data, 'little'))
    print(int.from_bytes(data, 'big'))
    # To byte string
    x = 94522842520747284487117727783387188
    print(x.to_bytes(16, 'big'))
    print(x.to_bytes(16, 'little'))
    # you also can use the struct module, but this module have a limit with
    # the size of  integer
    import struct
    hi, lo = struct.unpack('>QQ', data)
    print((hi << 64) + lo)

    # The byte order rule (little or big) only specifies the low order
    # alignment of the bytes when constructing the integer.
    x = 0x01020304
    print(x.to_bytes(4, 'big'))
    print(x.to_bytes(4, 'little'))

    # If you try to package an integer into a byte string, then it is not
    #  appropriate and you will get an error. If you need to, you can use the
    # int.bit_length() method to determine how many bytes are needed to store
    #  this value.
    x = 523 ** 23
    print(x)
    # x.to_bytes(16, 'little')
    nbytes, rem = divmod(x.bit_length(), 8)
    if rem:
        nbytes += 1
    print(x.to_bytes(nbytes, 'little'))


# Question5: test gigantic and NaN
def use_gigantic_and_NaN():
    a = float('inf')
    b = float('-inf')
    c = float('nan')
    print(a)
    print(b)
    print(c)
    import math
    print(math.isinf(a))
    print(math.isnan(c))

    print(float('inf') + 45)
    print(float('inf') * 45)
    print(10 / float('inf'))

    a = float('inf')
    print(a / a)
    # nan
    b = float('-inf')
    print(a + b)
    # nan

    # NaN values will propagate in all operations without exceptions
    c = float('nan')
    print(c + 23)
    print(c - 23)
    print(c * 23)
    print(math.sqrt(c))

    # compare nan and nan will be returned a false
    c = float('nan')
    d = float('nan')
    print(c == d)
    print(c is d)
    print(math.isnan(c))


# Question6: Large array operation
def large_array_operation():
    # Numpy is good choice
    import numpy as np
    ax = np.array([1, 2, 3, 4])
    ay = np.array([5, 6, 7, 8])
    print(ax * 2)
    print(ax + 10)
    print(ax + ay)
    print(ax * ay)

    def f(x):
        return 3 * x ** 2 - 2 * x + 7

    print(f(ax))
    print(np.sqrt(ax))
    print(np.cos(ax))

    # NumPy arrays use C or Fortran language mechanisms to allocate memory.
    # That is, they are a very large contiguous area of memory consisting of
    # the same type of data.
    # so construct a Two-dimensional array of floating point numbers of
    # 1000*1000 is easy things.
    grid = np.zeros(shape=(10000, 10000), dtype=float)
    grid += 10
    np.sin(grid)

    # Numpy also have good index function for Multidimensional Arrays
    a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    print(a)
    # select row 1
    print(a[1])
    # Select column 1
    print(a[:, 1])
    # Select a subregion and change it
    print(a[1:3, 1:3])
    a[1:3, 1:3] += 10
    print(a)
    # Broadcast a row vector across an operation on all rows
    print(a + [100, 101, 102, 103])
    # Conditional assignment on an array
    print(np.where(a < 10, a, 10))


# Question7: Random Choice
def extract_random_elements_in_list_or_generate_some_random_elements():
    # Use Mersenne Twister Algorithm
    import random
    values = [1, 2, 3, 4, 5, 6]
    print(random.choice(values))
    print(random.choice(values))
    print(random.choice(values))
    print(random.sample(values, 2))
    print(random.sample(values, 3))

    # Disrupt the order of the elements in the sequence
    random.shuffle(values)
    print(values)

    # Generate random int
    print(random.randint(0, 10))

    # Generate floating number in the range of 0 to 1
    print(random.random())

    # To get random number of N
    print(random.getrandbits(200))

    # change init seed
    random.seed()  # Seed based on system time or os.urandom()
    random.seed(12345)  # Seed based on integer given
    random.seed(b'bytedata')  # Seed based on byte data

    # but the random packages should not use the program about Cryptography
    # Use the ssl.RAND_bytes()
    import ssl
    ssl.RAND_bytes()


# Question8: Basic date and time conversion
def basic_date_and_time_conversion():
    # Use the datetime module, In order to perform conversions and calculations
    # for different time units.
    from datetime import timedelta
    a = timedelta(days=2, hours=6)
    b = timedelta(hours=4.5)
    c = a + b
    print(c.days)
    print(c.seconds)
    print(c.seconds / 3600)
    print(c.seconds / 3600)

    from datetime import datetime
    a = datetime(2012, 9, 23)
    print(a + timedelta(days=10))
    b = datetime(2012, 12, 21)
    d = b - a
    print(d.days)
    now = datetime.today()
    print(now)
    print(now + timedelta(minutes=10))

    # Datetime will automatically process leap years
    a = datetime(2012, 3, 1)
    b = datetime(2012, 2, 28)
    print(a - b)
    print((a - b).days)
    c = datetime(2013, 3, 1)
    d = datetime(2013, 2, 28)
    print((c - d).days)

    # if you want to calculate more complicated operation, Use the dateutil
    from dateutil.relativedelta import relativedelta
    print(a + relativedelta(months=+1))
    print(a + relativedelta(months=+4))
    # Time between two dates
    b = datetime(2012, 12, 21)
    d = b - a
    print(d)
    print(d.days)


# Question9: calculate the date of the last Friday
def calculate_the_date_of_the_last_friday():
    from datetime import datetime, timedelta

    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                'Friday', 'Saturday', 'Sunday']

    def get_previous_byday(dayname, start_date=None):
        if start_date is None:
            start_date = datetime.today()
        # what day is today?
        day_num = start_date.weekday()
        # The target date is what day of the week
        day_num_target = weekdays.index(dayname)
        days_ago = (7 + day_num - day_num_target) % 7
        if days_ago == 0:
            days_ago = 7
        target_date = start_date - timedelta(days=days_ago)
        return target_date

    datetime.today()
    print(get_previous_byday('Monday'))
    print(get_previous_byday('Tuesday'))  # Previous week, not today
    print(get_previous_byday('Friday'))
    print(get_previous_byday('Sunday'))
    print(get_previous_byday('Sunday', datetime(2012, 12, 21)))

    # If you have a large of calculation about date, had better to
    # install python-dateutil instead of it.
    # from datetime import datetime
    # from dateutil.relativedelta import relativedelta
    # from dateutil.rrule import *
    # d = datetime.now()
    # print(d)
    # # Next Friday
    # print(d + relativedelta(weekday=FR))
    # # Last Friday
    # print(d + relativedelta(weekday=FR(-1)))


# Question10: calculate the range of current month
def calculate_the_range_of_current_month():
    from datetime import date, timedelta
    import calendar

    def get_month_range(start_date=None):
        if start_date is None:
            start_date = date.today().replace(day=1)
        _, days_in_month = calendar.monthrange(start_date.year,
                                               start_date.month)
        end_date = start_date + timedelta(days=days_in_month)
        return (start_date, end_date)

    a_day = timedelta(days=1)
    first_day, last_day = get_month_range()
    while first_day < last_day:
        print(first_day)
        first_day += a_day

    # Method2:
    def date_range(start, stop, step):
        while start < stop:
            yield start
            start += step

    from datetime import datetime
    for d in date_range(datetime(2012, 9, 1),
                        datetime(2012, 10, 1),
                        timedelta(hours=6)):
        print(d)


# Question 11: convert string to date
def convert_string_to_date():
    from datetime import datetime
    text = '2012-09-20'
    y = datetime.strptime(text, '%Y-%m-%d')
    z = datetime.now()
    diff = z - y
    print(diff)

    nice_z = datetime.strftime(z, '%A %B %d, %Y')
    print(nice_z)

    # The performance of strptime() is very poor, If you want to have a good
    # Performance that can do it by yourself

    from datetime import datetime
    def parse_ymd(s):
        year_s, mon_s, day_s = s.split('-')
        return datetime(int(year_s), int(mon_s), int(day_s))


if __name__ == '__main__':
    # rounding_operation_in_floating_point_number()

    # perform_precise_floating_point_arithmetic()

    # print_number_of_format()

    # format_or_print_the_number()

    # convert_or_extract_byte_string()

    # use_gigantic_and_NaN()

    # large_array_operation()

    # extract_random_elements_in_list_or_generate_some_random_elements()

    # basic_date_and_time_conversion()

    # calculate_the_date_of_the_last_friday()

    # calculate_the_range_of_current_month()

    convert_string_to_date()
