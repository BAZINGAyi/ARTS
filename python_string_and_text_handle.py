

# Question1： You need to  split a string, but the But the separator and
# the surrounding spaces are not fixed.
# Answer: Use regex split
def split_complex_string():
    line = 'asdf fjdk; afed, fjek,asdf, foo'
    import re
    re.split(r'[;,\s]\s*', line)
    # ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

    # Use parentheses to capture groups
    fields = re.split(r'(;|,|\s)\s*', line)
    print(fields)
    # ['asdf', ' ', 'fjdk', ';', 'afed', ',', 'fjek', ',', 'asdf', ',', 'foo']

    values = fields[::2]
    delimiters = fields[1::2] + ['']
    print(delimiters)

    # Reform the line using the same delimiters
    res = ''.join(v + d for v, d in zip(values, delimiters))
    print(res)

    #  delete delimiters, use (?:...)
    result = re.split(r'(?:,|;|\s)\s*', line)
    print(result)


# Question2: match the head or end in string
def match_the_head_or_end():
    filename = 'spam.txt'
    print(filename.endswith('.txt'))
    print(filename.startswith('file:'))
    url = 'http://www.python.org'
    print(url.startswith('http:'))

    # match more tag
    import os
    filenames = os.listdir('.')
    print(filenames)
    res = [name for name in filenames if name.endswith(('.git', '.py')) ]
    print(res)
    # Check if the required file type exists
    print(any(name.endswith('.py') for name in filenames))

    from urllib.request import urlopen

    # read data from internet or the file
    def read_data(name):
        if name.startswith(('http:', 'https:', 'ftp:')):
            return urlopen(name).read()
        else:
            with open(name) as f:
                return f.read()

    # startwith() must have a tuple as parameter
    choices = ['http:', 'ftp:']
    url = 'http://www.python.org'
    print(url.startswith(tuple(choices)))


# Question3: Match strings with shell wildcards
# Answer: use the fnmatch
def use_strings_with_shell_wildcards():
    from fnmatch import fnmatch, fnmatchcase
    fnmatch('foo.txt', '*.txt')
    # True
    fnmatch('foo.txt', '?oo.txt')
    # True
    fnmatch('Dat45.csv',  'Dat[0-9]*')
    # True
    names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
    [name for name in names if fnmatch(name, 'Dat*.csv')]
    # ['Dat1.csv', 'Dat2.csv']

    # fnmatch() uses the case-sensitive rules of the underlying operating system
    #  (different systems are different) to match the pattern.
    # On OS X (Mac)
    fnmatch('foo.txt', '*.TXT')
    # False
    # On Windows
    fnmatch('foo.txt', '*.TXT')
    # True

    # you can use fnmatchcase to instead of it
    fnmatchcase('foo.txt', '*.TXT')

    addresses = [
        '5412 N CLARK ST',
        '1060 W ADDISON ST',
        '1039 W GRANVILLE AVE',
        '2122 N CLARK ST',
        '4802 N BROADWAY',
    ]

    from fnmatch import fnmatchcase
    print([addr for addr in addresses if fnmatchcase(addr, '* ST')])
    print([addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')])


# Question4: 字符串匹配和搜索
def match_and_search_string():
    text = 'yeah, but no, but yeah, but no, but yeah'
    # match at start or end
    text.startswith('yeah')
    text.endswith('no')
    # Search for the location of the first occurrence
    text.find('no')
    # complicated match
    text1 = '11/27/2012'
    text2 = 'Nov 27, 2012'
    import re
    # match() always matches from the string
    if re.match(r'\d+/\d+/\d+', text1):
        print('yes')
    else:
        print('no')
    # findall() can matches from anywhere
    datepat = re.compile(r'\d+/\d+/\d+')
    text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
    datepat.findall(text)

    # Parentheses are usually used to capture packets
    datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
    m = datepat.match('11/27/2012')
    m.group(0)  # 11/27/2012
    m.group(1)  # 11
    m.group(2)  # 27
    m.group(3)  # 2012
    m.groups()  # ('11', '27', '2012')
    month, day, year = m.groups()
    # Find all matches (notice splitting into tuples)
    datepat.findall(text)
    for month, day, year in datepat.findall(text):
        print('{}-{}-{}'.format(year, month, day))


if __name__ == '__main__':
    # split_complex_string()

    # match_the_head_or_end()

    # use_strings_with_shell_wildcards()

    match_the_head_or_end()



