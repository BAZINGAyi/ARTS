import io
import sys
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


# Question14: get the file list in dic
def get_the_file_list_in_dic():
    import os
    names = os.listdir('somedir')
    # the result will return the all files, sub dictionary and symbol link file.
    # you can use the function of os.path to filter some dat
    import os.path

    # Get all regular files
    names = [name for name in os.listdir('somedir')
             if os.path.isfile(os.path.join('somedir', name))]

    # Get all dirs
    dirnames = [name for name in os.listdir('somedir')
                if os.path.isdir(os.path.join('somedir', name))]

    # use the startwith() or endswith() to filter a dir
    pyfiles = [name for name in os.listdir('somedir')
               if name.endswith('.py')]

    # To match a file name that could be used glob or fnmatch
    import glob
    pyfiles = glob.glob('somedir/*.py')

    from fnmatch import fnmatch
    pyfiles = [name for name in os.listdir('somedir')
               if fnmatch(name, '*.py')]

    # use os.stat() to get more info with files
    import os.path
    import glob

    pyfiles = glob.glob('*.py')

    # Get file sizes and modification dates
    name_sz_date = [(name, os.path.getsize(name), os.path.getmtime(name))
                    for name in pyfiles]
    for name, size, mtime in name_sz_date:
        print(name, size, mtime)

    # Alternative: Get file metadata
    file_metadata = [(name, os.stat(name)) for name in pyfiles]
    for name, meta in file_metadata:
        print(name, meta.st_size, meta.st_mtime)

    # Sometimes we will meet some error that
    # File name that cannot be properly decoded


# Question15: Ignore file name encoding
def ignore_file_name_encoding():
    # You want to perform the I/O operation on the file using the original file
    # name, which means that the file name has not been decoded or encoded by
    # the system default encoding.
    # By default, all the file name according to the sys.getfilesystemencoding()
    # returns the texts of the code to encode or decode.
    print(sys.getfilesystemencoding())  # utf-8

    # If for some reason you want to ignore this encoding, you can use an
    # original byte string to specify a file name.
    # Wrte a file using a unicode filename
    with open('jalape\xf1o.txt', 'w') as f:
        f.write('Spicy!')

    # Directory listing (decoded)
    import os
    os.listdir('.')

    # Directory listing (raw)
    os.listdir(b'.')  # Note: byte string

    # Open file with raw filename
    with open(b'jalapen\xcc\x83o.txt') as f:
        print(f.read())


# Question 16: Print illegal file name
def print_illegal_file_name():
    # 默认情况下，python 会认为所有的文件名都根据 sys.getfilesystemencoding() 编码过了。
    # 但有一些文件系统并没有强制这样做，在创建文件名时没有正确编码文件。
    def bad_filename(filename):
        return repr(filename)[1:-1]

    import os
    files = os.listdir('.')
    files  # ['spam.py', 'b\udce4d.txt', 'foo.txt']
    # 在将错误的文件名给 open() 这样的函数时，一切能正常工作。只有在输出文件名到屏幕或者日志
    # 程序才会崩溃

    for name in files:
        print(name)
    # Traceback (most recent call last):
    #     File "<stdin>", line 2, in <module>
    # UnicodeEncodeError: 'utf-8' codec can't encode character '\udce4' in
    # position 1: surrogates not allowed

    # Method1
    for name in files:
        try:
            print(name)
        except UnicodeEncodeError:
            print(bad_filename(name))

    # Method2:
    def bad_filename(filename):
        temp = filename.encode(sys.getfilesystemencoding(),
                               errors='surrogateescape')
        return temp.decode('latin-1')

    # surrogateescape:
    # 这种是Python在绝大部分面向OS的API中所使用的错误处理器，
    # 它能以一种优雅的方式处理由操作系统提供的数据的编码问题。
    # 在解码出错时会将出错字节存储到一个很少被使用到的Unicode编码范围内。
    # 在编码时将那些隐藏值又还原回原先解码失败的字节序列。
    # 它不仅对于OS API非常有用，也能很容易的处理其他情况下的编码错误。


# Question17: Add or change the encoding of an open file
def add_or_change_the_encoding_of_an_open_file():
    # You want to add or change its Unicode encoding without closing an open
    # file. Use the io.TextIOWrapper() to warp it for Binary mode
    import urllib.request
    import io

    u = urllib.request.urlopen('http://www.python.org')
    f = io.TextIOWrapper(u, encoding='utf-8')
    text = f.read()

    # use detach() to remove existing text layer encoding and replace it with
    # the new encoding for text mode
    import sys
    print(sys.stdout.encoding)
    sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='latin-1')

    # The I/O system is built from a series of levels.
    f = open('sample.txt', 'w')
    print(f)  # <_io.TextIOWrapper name='sample.txt' mode='w' encoding='UTF-8'>
    print(f.buffer)  # <_io.BufferedWriter name='sample.txt'>
    print(f.buffer.raw)  # <_io.FileIO name='sample.txt' mode='wb'>
    # io.TextIOWrapper 是一个编码和解码Unicode的文本处理层
    # io.BufferedWriter 是一个处理二进制数据的带缓冲的I/O层
    # io.FileIO 是一个表示操作系统底层文件描述符的原始文件。
    # 增加或改变文本编码会涉及增加或改变最上面的 io.TextIOWrapper 层

    # 一般来讲，像上面例子这样通过访问属性值来直接操作不同的层是很不安全的。
    #  例如，如果你试着使用下面这样的技术改变编码看看会发生什么：
    print(f)  # <_io.TextIOWrapper name='sample.txt' mode='w' encoding='UTF-8'>
    f = io.TextIOWrapper(f.buffer, encoding='latin-1')
    print(f)  # <_io.TextIOWrapper name='sample.txt' encoding='latin-1'>
    # 可以看到最顶层的 TextIOWrapper 已经改变了
    f.write('Hello')
    # Traceback (most recent call last):
    #     File "<stdin>", line 1, in <module>
    # ValueError: I/O operation on closed file
    # 结果出错了，因为f的原始值已经被破坏了并关闭了底层的文件。
    f = open('sample.txt', 'w')
    print(f)  # <_io.TextIOWrapper name='sample.txt' mode='w' encoding='UTF-8'>
    b = f.detach()
    print(b)  # <_io.BufferedWriter name='sample.txt'>
    f.write('hello')
    # 原因和之前一样，TextIOWrapper 被破坏了
    # Traceback (most recent call last):
    #     File "<stdin>", line 1, in <module>
    # ValueError: underlying buffer has been detached
    # 添加一个新的顶层
    f = io.TextIOWrapper(b, encoding='latin-1')
    print(f)  # <_io.TextIOWrapper name='sample.txt' encoding='latin-1'>

    # 尽管已经向你演示了改变编码的方法， 但是你还可以利用这种技术来改变文件行处理、错误机制
    # 以及文件处理的其他方面。例如：
    sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='ascii',
                                  errors='xmlcharrefreplace')
    print(print('Jalape\u00f1o'))  # Jalape&#241;o
    # 注意下最后输出中的非ASCII字符 ñ 是如何被 &#241; 取代的。


# Question18: write data to text file
def write_data_to_text_file():
    # 你想在文本模式打开的文件中写入原始的字节数据。
    # 將字节数据写入文件的缓冲区
    import sys
    # 默认情况下，sys.stdout 总是以文本模式打开的。
    sys.stdout.write(b'Hello\n')
    # Traceback (most recent call last):
    #     File "<stdin>", line 1, in <module>
    # TypeError: must be str, not bytes
    sys.stdout.buffer.write(b'Hello\n')
    # 还可以通过 buffer 属性来读取二进制数据

    # I/O系统以层级结构的形式构建而成。 文本文件是通过在一个拥有缓冲的二进制模式文件上增加
    # 一个Unicode编码/解码层来创建。 buffer 属性指向对应的底层文件。如果你直接访问它的话
    # 就会绕过文本编码/解码层。


# Question19: Wrap file descriptors into file objects
def wrap_file_description_into_file_objects():
    # 在 操作系统上一个已打开的I/O通道(比如文件、管道、套接字等)的整型文件描述符，
    # 你想将它包装成一个更高层的Python文件对象。

    # 一个文件描述符和一个打开的普通文件是不一样的。 文件描述符仅仅是一个由操作系统指定的
    # 整数，用来指代某个系统的I/O通道。 如果你碰巧有这么一个文件描述符，你可以通过使用
    # open() 函数来将其包装为一个Python的文件对象。 你仅仅只需要使用这个整数值的文件描述符
    # 作为第一个参数来代替文件名即可。例如：

    # Open a low-level file descriptor
    import os
    fd = os.open('somefile.txt', os.O_WRONLY | os.O_CREAT)

    # Turn into a proper file
    f = open(fd, 'wt')
    f.write('hello world\n')
    f.close()

    # 当高层的文件对象被关闭或者破坏的时候，底层的文件描述符也会被关闭。 如果这个并不是你
    # 想要的结果，你可以给 open() 函数传递一个可选的 colsefd=False 。比如：
    # Create a file object, but don't close underlying fd when done
    f = open(fd, 'wt', closefd=False)

    # 在Unix系统中，这种包装文件描述符的技术可以很方便的将一个类文件接口作用于一个以不同
    # 方式打开的I/O通道上， 如管道、套接字等。举例来讲，下面是一个操作管道的例子：

    from socket import socket, AF_INET, SOCK_STREAM

    def echo_client(client_sock, addr):
        print('Got connection from', addr)

        # Make text-mode file wrappers for socket reading/writing
        client_in = open(client_sock.fileno(), 'rt', encoding='latin-1',
                         closefd=False)

        client_out = open(client_sock.fileno(), 'wt', encoding='latin-1',
                          closefd=False)

        # Echo lines back to the client using file I/O
        for line in client_in:
            client_out.write(line)
            client_out.flush()

        client_sock.close()

    def echo_server(address):
        sock = socket(AF_INET, SOCK_STREAM)
        sock.bind(address)
        sock.listen(1)
        while True:
            client, addr = sock.accept()
            echo_client(client, addr)

    # 需要重点强调的一点是，上面的例子仅仅是为了演示内置的 open() 函数的一个特性，并且也
    # 只适用于基于Unix的系统。 如果你想将一个类文件接口作用在一个套接字并希望你的代码可以
    # 跨平台，请使用套接字对象的 makefile() 方法。 但是如果不考虑可移植性的话，那上面的
    # 解决方案会比使用 makefile() 性能更好一点。

    # 你也可以使用这种技术来构造一个别名，允许以不同于第一次打开文件的方式使用它。
    # 例如，下面演示如何创建一个文件对象，它允许你输出二进制数据到标准输出
    # (通常以文本模式打开):
    import sys
    # Create a binary-mode file for stdout
    bstdout = open(sys.stdout.fileno(), 'wb', closefd=False)
    bstdout.write(b'Hello World\n')
    bstdout.flush()

    # 尽管可以将一个已存在的文件描述符包装成一个正常的文件对象， 但是要注意的是并不是所有的
    # 文件模式都被支持，并且某些类型的文件描述符可能会有副作用 (特别是涉及到错误处理、文件结
    # 尾条件等等的时候)。 在不同的操作系统上这种行为也是不一样，特别的，上面的例子都不能在非
    # Unix系统上运行。


# Question20: create temp file or files
def create_temp_file_or_files():
    # Method1:
    from tempfile import TemporaryFile

    with TemporaryFile('w+t') as f:
        # Read/write to the file
        f.write('Hello World\n')
        f.write('Testing\n')

        # Seek back to beginning and read the data
        f.seek(0)
        data = f.read()

    # Temporary file is destroyed

    # Method2:
    f = TemporaryFile('w+t')
    # Use the temporary file
    f.close()
    # File is destroyed

    # TemporaryFile() 的第一个参数是文件模式，通常来讲文本模式使用 w+t ，二进制模式使用
    #  w+b 。 这个模式同时支持读和写操作，在这里是很有用的，因为当你关闭文件去改变模式的时
    # 候，文件实际上已经不存在了。 TemporaryFile() 另外还支持跟内置的 open() 函数一样的
    # 参数。比如：
    with TemporaryFile('w+t', encoding='utf-8', errors='ignore') as f:
        pass

    # 在大多数Unix系统上，通过 TemporaryFile() 创建的文件都是匿名的，甚至连目录都没有。
    # 如果你想打破这个限制，可以使用 NamedTemporaryFile() 来代替。比如：

    from tempfile import NamedTemporaryFile

    with NamedTemporaryFile('w+t') as f:
        print('filename is:', f.name)

    # File automatically destroyed

    # 这里，被打开文件的 f.name 属性包含了该临时文件的文件名。 当你需要将文件名传递给
    # 其他代码来打开这个文件的时候，这个就很有用了。 和 TemporaryFile() 一样，结果文
    # 件关闭时会被自动删除掉。 如果你不想这么做，可以传递一个关键字参数 delete=False
    # 即可。比如：
    with NamedTemporaryFile('w+t', delete=False) as f:
        print('filename is:', f.name)

    # 为了创建一个临时目录，可以使用 tempfile.TemporaryDirectory() 。比如：
    from tempfile import TemporaryDirectory

    with TemporaryDirectory() as dirname:
        print('dirname is:', dirname)
        # Use the directory
        ...
    # Directory and all contents destroyed

    # TemporaryFile() 、NamedTemporaryFile() 和 TemporaryDirectory() 函数
    # 应该是处理临时文件目录的最简单的方式了，因为它们会自动处理所有的创建和清理步骤。
    # 在一个更低的级别，你可以使用 mkstemp() 和 mkdtemp() 来创建临时文件和目录。比如:
    import tempfile
    tempfile.mkstemp()
    tempfile.mkdtemp()

    # 但是，这些函数并不会做进一步的管理了。 例如，函数 mkstemp()
    # 仅仅就返回一个原始的OS文件描述符，你需要自己将它转换为一个真正的文件对象。
    # 同样你还需要自己清理这些文件。

    # 通常来讲，临时文件在系统默认的位置被创建，比如 /var/tmp 或类似的地方。
    # 为了获取真实的位置，可以使用 tempfile.gettempdir() 函数。比如：
    print(tempfile.gettempdir())

    # 所有和临时文件相关的函数都允许你通过使用关键字参数 prefix 、suffix 和 dir 来自定义
    # 目录以及命名规则。比如：
    f = NamedTemporaryFile(prefix='mytemp', suffix='.txt', dir='/tmp')
    print(f.name)

    # 尽可能以最安全的方式使用 tempfile 模块来创建临时文件。 包括仅给当前用户授权访问
    # 以及在文件创建过程中采取措施避免竞态条件。 要注意的是不同的平台可能会不一样。


# Question21: Data communication with the serial port
def data_communication_with_the_serial_port():
    # use pySerial
    import serial
    ser = serial.Serial('/dev/tty.usbmodem641',  # Device name varies
                        baudrate=9600,
                        bytesize=8,
                        parity='N',
                        stopbits=1)

    # 设备名对于不同的设备和操作系统是不一样的。 比如，在Windows系统上，你可以使用0, 1等
    # 表示的一个设备来打开通信端口”COM0”和”COM1”。 一旦端口打开，那就可以使用 read()，
    # readline() 和 write() 函数读写数据了。例如：
    ser.write(b'G1 X50 Y50\r\n')
    resp = ser.readline()

    # 尽管表面上看起来很简单，其实串口通信有时候也是挺麻烦的。 推荐你使用第三方包如
    # pySerial 的一个原因是它提供了对高级特性的支持 (比如超时，控制流，缓冲区刷新，
    # 握手协议等等)。举个例子，如果你想启用 RTS-CTS 握手协议， 你只需要给 Serial()
    # 传递一个 rtscts=True 的参数即可。 其官方文档非常完善，因此我在这里极力推荐这个包。

    # 时刻记住所有涉及到串口的I/O都是二进制模式的。因此，确保你的代码使用的是字节而不是文本
    # (或有时候执行文本的编码/解码操作)。 另外当你需要创建二进制编码的指令或数据包的时候，
    # struct 模块也是非常有用的。


# Question22: Serializing Python objects
def serializing_python_objects():
    # You need to serialize a Python object into a stream of bytes to save it
    # to a file, store it to a file, store it to a database, or transfer it over
    # a network
    # Use the pickle module
    import pickle

    data = ...  # Some Python object
    f = open('somefile', 'wb')
    pickle.dump(data, f)

    # to string
    s = pickle.dumps(data)

    # from, bytes to a object
    # Restore from a file
    f = open('somefile', 'rb')
    data = pickle.load(f)

    # Restore from a string
    data = pickle.loads(s)

    # 果你碰到某个库可以让你在数据库中保存/恢复Python对象或者是通过网络传输对象的话，
    # 那么很有可能这个库的底层就使用了 pickle 模块。

    # pickle 是一种Python特有的自描述的数据编码。 通过自描述，被序列化后的数据包含每个对象
    # 开始和结束以及它的类型信息。 因此，你无需担心对象记录的定义，它总是能工作。 举个例子，
    # 如果要处理多个对象，你可以这样做：

    import pickle
    f = open('somedata', 'wb')
    pickle.dump([1, 2, 3, 4], f)
    pickle.dump('hello', f)
    pickle.dump({'Apple', 'Pear', 'Banana'}, f)
    f.close()
    f = open('somedata', 'rb')
    pickle.load(f)
    pickle.load(f)
    pickle.load(f)

    # 你还能序列化函数，类，还有接口，但是结果数据仅仅将它们的名称编码成对应的代码对象。
    # 例如：
    import math
    import pickle
    pickle.dumps(math.cos)  # b'\x80\x03cmath\ncos\nq\x00.'

    # 当数据反序列化回来的时候，会先假定所有的源数据时可用的。 模块、类和函数会自动按需导入
    # 进来。对于Python数据被不同机器上的解析器所共享的应用程序而言， 数据的保存可能会有问题
    # ，因为所有的机器都必须访问同一个源代码。

    # 千万不要对不信任的数据使用pickle.load()。
    # pickle在加载时有一个副作用就是它会自动加载相应模块并构造实例对象。
    # 但是某个坏人如果知道pickle的工作原理，
    # 他就可以创建一个恶意的数据导致Python执行随意指定的系统命令。
    # 因此，一定要保证pickle只在相互之间可以认证对方的解析器的内部使用。

    # 有些类型的对象是不能被序列化的。这些通常是那些依赖外部系统状态的对象， 比如打开的文件，
    # 网络连接，线程，进程，栈帧等等。 用户自定义类可以通过提供 __getstate__() 和
    # __setstate__() 方法来绕过这些限制。 如果定义了这两个方法，pickle.dump() 就会调用
    #  __getstate__() 获取序列化的对象。 类似的，__setstate__() 在反序列化时被调用。
    # 为了演示这个工作原理， 下面是一个在内部定义了一个线程但仍然可以序列化和反序列化的类：

    # countdown.py
    import time
    import threading

    class Countdown:
        def __init__(self, n):
            self.n = n
            self.thr = threading.Thread(target=self.run)
            self.thr.daemon = True
            self.thr.start()

        def run(self):
            while self.n > 0:
                print('T-minus', self.n)
                self.n -= 1
                time.sleep(5)

        def __getstate__(self):
            return self.n

        def __setstate__(self, n):
            self.__init__(n)

    # 试着运行下面的序列化试验代码：
    c = Countdown(30)
    # T-minus 30
    # T-minus 29

    # After a few moments
    f = open('cstate.p', 'wb')
    import pickle
    pickle.dump(c, f)
    f.close()

    # 然后退出Python解析器并重启后再试验下：
    f = open('cstate.p', 'rb')
    pickle.load(f)
    # T-minus 19
    # T-minus 18

    # 可以看到线程又奇迹般的重生了，从你第一次序列化它的地方又恢复过来。
    # pickle 对于大型的数据结构比如使用 array 或 numpy 模块创建的二进制数组效率并不是
    # 一个高效的编码方式。 如果你需要移动大量的数组数据，你最好是先在一个文件中将其保存为
    # 数组数据块或使用更高级的标准编码方式如HDF5 (需要第三方库的支持)。

    # 由于 pickle 是Python特有的并且附着在源码上，所有如果需要长期存储数据的时候不应该选
    # 用它。 例如，如果源码变动了，你所有的存储数据可能会被破坏并且变得不可读取。 坦白来讲，
    # 对于在数据库和存档文件中存储数据时，你最好使用更加标准的数据编码格式如XML，CSV或JSON
    # 。 这些编码格式更标准，可以被不同的语言支持，并且也能很好的适应源码变更。

    # 对于最常见的使用场景，你不需要去担心这个，但是如果你要在一个重要的程序中使用
    # pickle去做序列化的话， 最好去查阅一下
    # https://docs.python.org/3/library/pickle.html


class StudyInputOrOutput():
    def basic_input_or_output(self):
        name = input('your name:')  # 等待键盘输入，知道回车被按下
        gender = input('you are a boy?(y/n)')

        ###### 输入 ######
        # your name: Jack
        # you are a boy?

        welcome_str = 'Welcome to the matrix {prefix} {name}.'
        welcome_dic = {
            'prefix': 'Mr.' if gender == 'y' else 'Mrs',
            'name': name
        }

        print('authorizing...')
        print(welcome_str.format(**welcome_dic))

        ########## 输出 ##########
        # authorizing...
        # Welcome to the matrix Mr.Jack.

        a = input()
        # 1
        b = input()
        # 2

        print('a + b = {}'.format(a + b))
        ########## 输出 ##############
        # a + b = 12
        # print('type of a is {}, type of b is {}'.format(type(a), type(b)))
        ########## 输出 ##############
        # type of a is <class 'str'>, type of b is < class 'str' >

        print('a + b = {}'.format(int(a) + int(b)))
        ########## 输出 ##############
        # a + b = 3


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

    # memory_mapped_binary()

    # the_operation_of_path()

    # test_if_the_file_exists()

    # get_the_file_list_in_dic()

    # ignore_file_name_encoding()

    # wrap_file_description_into_file_objects()

    # create_temp_file_or_files()

    # data_communication_with_the_serial_port()

    serializing_python_objects()
