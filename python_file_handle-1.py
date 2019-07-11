import io
from mmap import mmap


# Question1: 现在要处理一个大小为10G的文件，但是内存只有4G，
# 应该如何实现？需要考虑的问题都有那些？

# Answer:
# 内存只有4G无法一次性读入10G文件，需要分批读入分批读入数据要记录每次读入数据的位置。
# 分批每次读取数据的大小，太小会在读取操作花费过多时间。

# Reason:
# 1. 逐行读取解决无法读入 10G 文件的问题

# 2. 对文件的读取操作跨过了页缓存，减少了数据的拷贝次数，用内存读写取代I/O读写，
# 提高了文件读取效率。

# 3. 实现了用户空间和内核空间的高效交互方式。两空间的各自修改操作可以直接反映在映射的区域内
# ，从而被对方空间及时捕捉。

# 4. 提供进程间共享内存及相互通信的方式。不管是父子进程还是无亲缘关系的进程，都可以将
# 自身用户空间映射到同一个文件或匿名映射到同一片区域。从而通过各自对映射区域的改动，
# 达到进程间通信和进程间共享的目的。同时，如果进程A和进程B都映射了区域C，当A第一次读取C时
# 通过缺页从磁盘复制文件页到内存中；但当B再读C的相同页面时，虽然也会产生缺页异常，
# 但是不再需要从磁盘中复制文件过来，而可直接使用已经保存在内存中的文件数据。

# 5. 可用于实现高效的大规模数据传输。内存空间不足，是制约大数据操作的一个方面，
# 解决方案往往是借助硬盘空间协助操作，补充内存的不足。但是进一步会造成大量的文件I/O操作，
# 极大影响效率。这个问题可以通过mmap映射很好的解决。换句话说，但凡是需要用磁盘空间代替
# 内存的时候，mmap都可以发挥其功效。


def get_lines(fp):
    with open(fp, "r+") as f:
        m = mmap(f.fileno(), 0)
        while True:
            line = m.readline()
            if line == b'':
                break
            yield line.decode()

        # tmp = 0
        # for i, char in enumerate(m):
        #     if char == b"\n":
        #         yield m[tmp:i+1].decode()
        #         tmp = i+1


def handle_file():
    for line in get_lines("leetcode-7.py"):
        print(line.rstrip())


# Question2: 遍历文件夹


def print_directory_contents(s_path):
    """
    这个函数接收文件夹的名称作为输入参数
    返回该文件夹中文件的路径
    以及其包含文件夹中文件的路径
    """
    import os
    for s_child in os.listdir(s_path):
        s_child_path = os.path.join(s_path, s_child)
        if os.path.isdir(s_child_path):
            print_directory_contents(s_child_path)
        else:
            print(s_child_path)


def traverse_dir_method1():
    import os

    def get_files(dir, suffix):
        res = []
        for root, dirs, files in os.walk(dir):
            # root: dir path
            # dirs: dictionaries name
            # files: file names list
            for filename in files:
                name, suf = os.path.splitext(filename)
                if suf == suffix:
                    res.append(os.path.join(root, filename))

        print(res)

    get_files("../ARTS", '.py')


def traverse_dir_method2():
    from glob import iglob

    def func(fp, postfix):
        for i in iglob(f"{fp}/**/*{postfix}", recursive=True):
            print(i)

    postfix = ".py"
    func("../ARTS", postfix)


# Question2: read text data
def read_text_data_with_the_correct_encoding():
    # You need to read and write text data of various encodings,
    # such as ASCII, UTF-8 or UTF-16 encoding.
    # Read the entire file as a single string
    # The 't' means text mode
    with open('somefile.txt', 'rt') as f:
        data = f.read()

    # Iterate over the lines of the file
    with open('somefile.txt', 'rt') as f:
        for line in f:
            pass
            # process line
    # write and clear a existed file
    # Write chunks of text data
    with open('somefile.txt', 'wt') as f:
        f.write('text1')
        f.write('text2')

    # Redirected print statement
    with open('somefile.txt', 'wt') as f:
        print('line1', file=f)
        print('line2', file=f)

    # If you want append content to an existed file
    with open('somefile.txt', 'at') as f:
        f.write('text1')
        f.write('text2')

    # the read nad write operation use system encoding by default, in the most
    # of machine uses the utf-8
    import sys
    print(sys.getdefaultencoding())
    with open('somefile.txt', 'rt', encoding='latin-1') as f:
        pass

    # Using latin-1 encoding will never produce an encoding error when reading
    # a unknown encoded text
    # Reading a file with latin-1 encoding may not produce completely correct
    # text decoding data, but it can also extract enough useful data from it.
    # At the same time, if you later write back the data, the original data
    # will still be retained.

    # There is a problem about line break symbol, they are different in the Uinx
    # and Windows. By default, Python recognizes all normal newline characters
    # and converts them into a single '\n' character.
    # Similarly, the line break '\n' is converted to the system default newline
    # when output.

    # If you don't want this way as default handling, you can pass the parameter
    # newline='' to the open() functions
    # like this:
    # Read with disabled newline translation
    with open('somefile.txt', 'rt', newline='') as f:
        pass
    # To prove the difference between the two, I read a windows file on a unix,
    # the file name is `hello world\r\n`
    # Newline translation enabled (the default)
    f = open('hello.txt', 'rt')
    f.read()
    # 'hello world!\n'
    f.close()

    # Newline translation disabled
    g = open('hello.txt', 'rt', newline='')
    g.read()
    # 'hello world!\r\n'

    # The last problem is the coding error that can occur in the text file.
    # If this  error occurs, It usually means that the encoding you specified
    # when reading the text is incorrect.
    # If the encoding error still exists, you can pass an optional errors
    # parameter to the open() function to handle the errors.

    # Replace bad chars with Unicode U+fffd replacement char
    f = open('sample.txt', 'rt', encoding='ascii', errors='replace')
    f.read()
    # Ignore bad chars entirely
    g = open('sample.txt', 'rt', encoding='ascii', errors='ignore')
    g.read()
    f.close()
    g.close()


# Question3: Print to the file
def redirect_print_to_the_file():
    # Mode must be wt, otherwise it will be wrong
    with open('d:/work/test.txt', 'wt') as f:
        print('Hello World!', file=f)


# Question4: Print with other separators or line terminators
def print_with_other_separators():
    print('ACME', 50, 91.5)
    print('ACME', 50, 91.5, sep=',')
    print('ACME', 50, 91.5, sep=',', end='!!\n')
    # use end to forbid wrap
    for i in range(5):
        print(i)

    for i in range(5):
        print(i, end=' ')

    # join only can be used the string
    print(','.join(('ACME', '50', '91.5')))
    row = ('ACME', 50, 91.5)
    # print(','.join(row)) have a error
    print(','.join(str(x) for x in row))


# Question5: read bytes data(like picture, audio and so on)
def read_bytes_data():
    # Read the entire file as a single byte string
    with open('somefile.bin', 'rb') as f:
        data = f.read()

    # Write binary data to a file
    with open('somefile.bin', 'wb') as f:
        f.write(b'Hello World')

    # when we read or write bytes data, we need to indicates that the data is
    # in a byte string format.

    # the return value are bytes value not bytes string when we use the Index
    # and Iterative action
    # Text string
    t = 'Hello World'
    print(t[0])
    for c in t:
        print(c)

    # Byte string
    b = b'Hello World'
    b[0]  # 72

    # If you want to read or write text data from a binary mode file, you must
    # ensure that you want to decode and encode it.
    with open('somefile.bin', 'rb') as f:
        data = f.read(16)
        text = data.decode('utf-8')

    with open('somefile.bin', 'wb') as f:
        text = 'Hello World'
        f.write(text.encode('utf-8'))

    # binary Io have a little-known feature that arrays and C structure types
    # can be written directly
    import array
    nums = array.array('i', [1, 2, 3, 4])
    with open('data.bin', 'wb') as f:
        f.write(nums)

    # This applies to any implementation of what is called a "buffer interface"
    # that expose its underlying memory buffer to handle its operations.
    # Writing binary data is one such operations.

    # Many object admit to use the readinto() method of file object to read
    # directly binary datas to underlying memory buffer
    import array
    a = array.array('i', [0, 0, 0, 0, 0, 0, 0, 0])
    with open('data.bin', 'rb') as f:
        f.readinto(a)

    # Care must be taken when using this method, because it typically has
    # platform dependencies and may depend on word length and byte order
    # (high order first and low order first).


# Question6: Files does not exist to be written
def files_does_not_exists_to_be_written():
    # you want to write data in a file, but the premise must be that the files
    # does not exist on the file system.
    # Use x mode instead of w mode
    with open('somefile', 'xt') as f:
        f.write('Hello\n')

    # Sometimes we cant use it just like this:
    import os
    if not os.path.exists('somefile'):
        with open('somefile', 'wt') as f:
            f.write('Hello\n')
    else:
        print('File already exists!')

    # Notice: x mode is extend for python3. it not exists in Before version


# Question7: the IO operation of String
def the_io_operation_of_string():
    # you want to manipulate text or binary strings using a program that
    # manipulates class file objects
    # use io.stringIO() and io.Bytes()
    s = io.StringIO()
    s.write('Hello World\n')
    print('This is a test', file=s)
    # Get all of the data written so far
    s.getvalue()

    # Wrap a file interface around an existing string
    s = io.StringIO('Hello\nWorld\n')
    s.read(4)
    s.read()

    # io.StringIO can only be used for text. If you want to manipulate binary
    # data, use the io.BytesIO class instead
    s = io.BytesIO()
    s.write(b'binary data')
    s.getvalue()

    # The StringIO or BytesIO is very useful when you want to mock a general
    # file. For example, In uint tesing, you can use StrinIO to crearte a class
    # file object that including test data, this object can be pass to a
    # function that have a parameter is general file


# Question8: reading and writing a compressing files
def read_or_write_a_compressed_files():
    # Use gzip or bz2
    # gzip compression
    import gzip
    with gzip.open('somefile.gz', 'rt') as f:
        text = f.read()

    # bz2 compression
    import bz2
    with bz2.open('somefile.bz2', 'rt') as f:
        text = f.read()

    # the mode also can choose rb or wb
    # If you don't specify the mode, the default is binary mode. and If the
    # program wants to accept text data, it will fail.

    # it can use the compresslevel to specify a compress level when we write
    # a compressed data. the default level is 9 that is the highest level.
    # The lower the level, the better the performance, but the
    # less compressed the data.
    with gzip.open('somefile.gz', 'wt', compresslevel=5) as f:
        f.write(text)

    # Finally, gzip.open() and bz2.open() have a little-understood feature that
    # works on an existing file that opens in binary mode.
    # For example, the following code works:

    import gzip
    f = open('somefile.gz', 'rb')
    with gzip.open(f, 'rt') as g:
        text = g.read()

    # This allows gzip and bz2 modules to work on many file-like objects,
    # such as sockets, pipes, and in-memory files.


# Question9: File iteration for fixed-size records
def file_iteration_for_fixed_size_records():
    # You want to iterate over a collection of fixed-length records or blocks
    # of data, not row by row in a file.
    from functools import partial

    RECORD_SIZE = 32

    with open('somefile.data', 'rb') as f:
        records = iter(partial(f.read, RECORD_SIZE), b'')
        for r in records:
            pass

    # The records object in this example is an iterable object, which will
    #  continuously produce data blocks of fixed size until the end of the file.
    # Note that if the total record size is not an integer multiple of the
    #  block size, the last returned element will have fewer bytes than expected

    # A little-known feature of the iter() function is that if you pass it a
    # callable object and a tag value, it creates an iterator.
    # The iterator calls the incoming callable object until it returns the
    # marked value, at which point the iteration terminates.

    # In the example, functools.partial is used to create a callable object that
    #  reads a fixed number of bytes from the file each time it is invoked.
    # The tag value b '' is the return value when the end of the file is reached


# Question10: read bytes data to Variable buffer
def read_bytes_data_to_variable_buffer():
    import os.path

    def read_into_buffer(filename):
        buf = bytearray(os.path.getsize(filename))
        with open(filename, 'rb') as f:
            f.readinto(buf)
        return buf

    buf = read_into_buffer('sample.bin')
    print(buf)
    buf[0:5] = b'Hello'

    with open('newsample.bin', 'wb') as f:
        f.write(buf)

    # 文件对象的 readinto() 方法能被用来为预先分配内存的数组填充数据，甚至包括由 array
    #  模块或 numpy 库创建的数组。 和普通 read() 方法不同的是， readinto() 填充已存在的
    # 缓冲区而不是为新对象重新分配内存再返回它们。 因此，你可以使用它来避免大量的内存分配操
    # 作。 比如，如果你读取一个由相同大小的记录组成的二进制文件时，你可以像下面这样写：

    record_size = 32  # Size of each record (adjust value)

    buf = bytearray(record_size)
    with open('somefile', 'rb') as f:
        while True:
            n = f.readinto(buf)
            if n < record_size:
                break
            # Use the contents of buf

    # 另外有一个有趣特性就是 memoryview ， 它可以通过零复制的方式对已存在的缓冲区执行切片
    # 操作，甚至还能修改它的内容。比如：
    print(buf)
    m1 = memoryview(buf)
    m2 = m1[-5:]
    print(m2)
    m2[:] = b'WORLD'
    print(buf)

    # 使用 f.readinto() 时需要注意的是，你必须检查它的返回值，也就是实际读取的字节数。
    #
    # 如果字节数小于缓冲区大小，表明数据被截断或者被破坏了(比如你期望每次读取指定数量的字节
    # )。
    #
    # 最后，留心观察其他函数库和模块中和 into 相关的函数(比如 recv_into()
    # ， pack_into() 等)。 Python的很多其他部分已经能支持直接的I/O或数据访问操作，
    # 这些操作可被用来填充或修改数组和缓冲区内容。


# Question11: Memory mapped binary
def memory_mapped_binary():
    # You want to memory map a binary file into a variable byte array, perhaps
    # for random access to its contents or to make some modifications in place.
    # Use mmap to mapping a file.
    import os
    import mmap

    def memory_map(filename, access=mmap.ACCESS_WRITE):
        size = os.path.getsize(filename)
        fd = os.open(filename, os.O_RDWR)
        return mmap.mmap(fd, size, access=access)

    size = 1000000
    with open('data', 'wb') as f:
        f.seek(size - 1)
        f.write(b'\x00')

    # This is a example for using mmap to files
    m = memory_map('data')
    print(len(m))
    print(m[0:10])
    print(m[0])

    # Reassign a slice
    m[0:11] = b'Hello World'
    m.close()

    # Verify that changes were made
    with open('data', 'rb') as f:
        print(f.read(11))


# Question12: the operation of file path
def the_operation_of_path():
    # use os.path to handle path
    import os
    path = '/Users/beazley/Data/data.csv'
    # Get the last component of the path
    os.path.basename(path)  # 'data.csv'

    # Get the directory name
    os.path.dirname(path)  # '/Users/beazley/Data'

    # Join path components together
    os.path.join('tmp', 'data', os.path.basename(path))  # 'tmp/data/data.csv'

    # Expand the user's home directory
    path = '~/Data/data.csv'
    os.path.expanduser(path)  # '/Users/beazley/Data/data.csv'

    # Split the file extension
    os.path.splitext(path)


# Question13: test if the file exists
def test_if_the_file_exists():
    import os
    os.path.exists('/etc/passwd')
    os.path.exists('/tmp/spam')
    # Is a regular file
    os.path.isfile('/etc/passwd')
    # Is a directory
    os.path.isdir('/etc/passwd')
    # Is a symbolic link
    os.path.islink('/usr/local/bin/python3')
    # Get the file linked to
    os.path.realpath('/usr/local/bin/python3')

    # Get the size or modified date of file:
    os.path.getsize('/etc/passwd')
    os.path.getmtime('/etc/passwd')
    import time
    time.ctime(os.path.getmtime('/etc/passwd'))

    # Think about the files problem of permission
    os.path.getsize('/Users/guido/Desktop/foo.txt')





if __name__ == "__main__":
    # handle_file()

    # print_directory_contents('../ARTS')

    # traverse_dir_method1()

    # traverse_dir_method2()

    # redirect_print_to_the_file()

    # redirect_print_to_the_file()

    # print_with_other_separators()

    # read_bytes_data()

    # the_io_operation_of_string()

    # read_bytes_data_to_variable_buffer()

    memory_mapped_binary()
