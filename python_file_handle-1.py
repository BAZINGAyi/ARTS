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


if __name__ == "__main__":

    # handle_file()

    # print_directory_contents('../ARTS')

    # traverse_dir_method1()

    traverse_dir_method2()
