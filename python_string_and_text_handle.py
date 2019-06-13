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
    res = [name for name in filenames if name.endswith(('.git', '.py'))]
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
    fnmatch('Dat45.csv', 'Dat[0-9]*')
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
    print([addr for addr in addresses if
           fnmatchcase(addr, '54[0-9][0-9] *CLARK*')])


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


# Question5: search and replace string
def search_and_replace_text():
    # simple way
    text = 'yeah, but no, but yeah, but no, but yeah'
    text.replace('yeah', 'yep')

    # complex way
    text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
    import re
    # this sec param represents the position of the group
    result = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
    print(result)
    # you can use the callback function for more complicated situation
    from calendar import month_abbr
    datepat = re.compile(r'(\d+)/(\d+)/(\d+)')

    def change_date(m):
        # the m is match object,like the object that match() or find() returned
        mon_name = month_abbr
        return '{} {} {}'.format(m.group(2), mon_name, m.group(3))[
            int(m.group(1))]

    datepat.sub(change_date, text)
    # you also can get the count that how many result was replaced
    newtext, n = datepat.subn(r'\3-\1-\2', text)
    print(newtext, n)


def search_and_replaces_text_that_is_case_insensitive():
    import re
    text = 'UPPER PYTHON, lower python, Mixed Python'
    re.findall('python', text, flags=re.IGNORECASE)
    re.sub('python', 'snake', text, flags=re.IGNORECASE)

    # the second example That reveals a small flaw, The replacement string is
    # not automatically consistent with the case of the matched string.
    def matchcase(word):
        def replace(m):
            text = m.group()
            if text.isupper():
                return word.upper()
            elif text.islower():
                return word.lower()
            elif text[0].isupper():
                return word.capitalize()
            else:
                return word

        return replace

    re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE)


def the_shortest_match_mode():
    import re
    str_pat = re.compile(r'"(.*)"')
    text1 = 'Computer says "no."'
    str_pat.findall(text1)  # ['no.']

    text2 = 'Computer says "no." Phone says "yes."'
    # The * operator is greedy, so the match finds the longest possible match.
    str_pat.findall(text2)  # ['no." Phone says "yes.']

    # To fix that, use the '?'
    str_pat = re.compile(r'"(.*?)"')
    str_pat.findall(text2)
    #  ['no.', 'yes.']


def multi_line_matching_mode():
    # sometimes, we need to match a string in a multi-lines.
    import re
    comment = re.compile(r'/\*(.*?)\*/')
    text1 = '/* this is a comment */'
    text2 = '''/* this is a
    multiline comment */
    '''
    comment.findall(text1)  # [' this is a comment ']
    comment.findall(text2)  # ['']

    # To fix that, Ues the `(?:.|\n)` to indicate a Non-capture group.
    # It defines a group that is only used for matching,
    # not by individual capture or numbering.
    comment = re.compile(r'/\*((?:.|\n)*?)\*/')
    comment.findall(text2)  # [' this is a\n multiline comment ']

    # Or you can use `re.DOTALL`, let '.' to march Any character
    # including line breaks. But It’s best to define your own
    # regular expression pattern.
    comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
    comment.findall(text2)  # [' this is a\n multiline comment ']


# Question6: delete unwanted characters in a string
def delete_unwanted_characters_in_a_string():
    s = ' hello world \n'
    print(s.strip())
    print(s.lstrip())
    print(s.rstrip())

    # Character stripping
    t = '-----hello====='
    print(t.lstrip('-'))
    print(t.strip('-='))

    # If you want deal space in the middle, you can replace method or regex()
    print(s.replace(' ', ''))
    import re
    print(re.sub('\s+', ' ', s))

    # clear space in files. This method is very efficient because it does not
    # require all data to be read in advance to be placed in a temporary list.
    # It just creates a generator and performs a strip operation each time it
    # returns a row.
    with open('leetcode-1.py') as f:
        lines = (line.strip() for line in f)
        for line in lines:
            print(line)


# Question7: convert  "123" of string  to 123 of int
def convert_string_to_int():
    # Method1: Use the str()
    def atoi(s):
        num = 0
        for v in s:
            for j in range(10):
                if v == str(j):
                    num = num * 10 + j

    # Method2: use ord()
    def atoi_1(s):
        num = 0
        for v in s:
            num = num * 10 + ord(v) + ord('0')
        return num

    # Method3: use eval()
    def atoi_2(s):
        num = 0
        for v in s:
            t = "%s * 1" % v
            n = eval(t)
            num = num * 10 + n
        return num

    # Method4: use reduce:
    from functools import reduce

    def sum_x_y(x, y):
        return x * 10 + ord(y) - ord('0')

    def atoi_3(s):
        return reduce(sum_x_y, s, 0)

    # lamba Anonymous functions
    def atoi_4(s):
        return reduce(lambda x, y: x * 10 + ord(y) - ord('0'), s, 0)


# Question8: Unicode processing
def standardize_unicode_text():
    # you're dealing with Unicode strings, you need to make sure that all
    # strings have the same representation at the bottom.
    # As blow, some characters can be represented by multiple legal codes.
    # use to  overall characters ”ñ”(U+00F1) to represent
    # use to Latin letters(U+0303) to represent
    s1 = 'Spicy Jalape\u00f1o'
    s2 = 'Spicy Jalapen\u0303o'
    print(s1)
    print(s2)
    print('s1 == s2', str(s1 == s2))
    print(len(s1))
    print(len(s2))

    # To Fix that you can use unicodedata to standardize text
    # NFC represents the character should be the overall composition
    import unicodedata
    t1 = unicodedata.normalize('NFC', s1)
    t2 = unicodedata.normalize('NFC', s2)
    print('t1 == t2', str(t1 == t2))
    print('the charater type is', ascii(t1))
    # NFD represents the character should be decomposed into multiple combined
    # character representations
    t3 = unicodedata.normalize('NFD', s1)
    t4 = unicodedata.normalize('NFD', s2)
    print('t3 == t4', str(t3 == t4))
    print('the charater type is', ascii(t3))
    # python also support the standardization of NFKC and NFKD, it add some
    # compatible features to some special characters.
    s = '\ufb01'  # A single character
    print(s)
    # single character
    print(unicodedata.normalize('NFD', s))
    # separated character
    print(unicodedata.normalize('NFKD', s))
    print(unicodedata.normalize('NFKC', s))

    # use the tool function to check if a character is a some type of character.
    # eg: check if the character is number and so on.
    t1 = unicodedata.normalize('NFD', s1)
    print(''.join(c for c in t1 if not unicodedata.combining(c)))


def match_unicode_in_regex():
    # By default, re module have some basic support with Unicode
    import re
    num = re.compile('\d+')
    # ASCII digits
    res = num.match('123')
    print(res.group())
    # Arabic digits
    res = num.match('\u0661\u0662\u0663')
    print(res.group())

    # Include the specified Unicode character in the pattern
    arabic = re.compile('[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]+')
    pat = re.compile('stra\u00dfe', re.IGNORECASE)
    s = 'straße'
    res = pat.match(s)  # Matches
    print(res.group())

    # When performing matching and search operations, it is best to standardize
    # and clean up all text into a standardized format. Also note some special
    # cases, such as behavior when ignoring case matching and case conversion.
    pat.match(s.upper())  # Doesn't match
    print(s.upper())  # Case folds


def clean_text_string():
    # some boring childish hackers enter the text "pýtĥöñ" in your website
    # page form, and then you want to clean them up.
    s = 'pýtĥöñ\fis\tawesome\r\n'
    remap = {
        ord('\t'): ' ',
        ord('\f'): ' ',
        ord('\r'): None  # Deleted
    }
    a = s.translate(remap)
    print(a)

    import unicodedata
    import sys
    cmb_chrs = dict.fromkeys(
        c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
    print(cmb_chrs)
    b = unicodedata.normalize('NFD', a)
    print(b)
    c = b.translate(cmb_chrs)
    print(c)

    # mapping unicode character to ASCII
    digitmap = {c: ord('0') + unicodedata.digit(chr(c))
                for c in range(sys.maxunicode)
                if unicodedata.category(chr(c)) == 'Nd'}
    print(digitmap)
    print(len(digitmap))

    # Arabic digits
    x = '\u0661\u0662\u0663'
    print(x.translate(digitmap))

    # use I/O encode() and decode()
    b = unicodedata.normalize('NFD', a)
    c = b.encode('ascii', 'ignore').decode('ascii')
    print(c)


# Question9: String alignment
def string_alignment():
    text = 'Hello World'
    print(text.ljust(20))
    print(text.rjust(20))
    print(text.center(20))
    print(text.rjust(20, '='))
    print(text.center(20, '='))

    # Use format()
    print(format(text, '>20'))
    print(format(text, '<20'))
    print(format(text, '^20'))
    print(format(text, '=>20s'))
    print(format(text, '*^20'))
    # Multiple values
    print('{:>10s} {:>10s}'.format('Hello', 'World'))
    # format number
    x = 1.2345
    print(format(x, '>10'))
    print(format(x, '^10.2f'))

    # you awalays look the ‘%’ to format str in the old version code
    print('%-20s' % text)
    # But you should prefer to use the format() method


# Question10： Merge splicing string
def merge_multiple_string_to_a_big_one():
    # if the string that you want to merge is in the sequence or the iterable,
    # you should use the join().
    parts = ['Is', 'Chicago', 'Not', 'Chicago?']
    print(' '.join(parts))
    print(','.join(parts))
    print(''.join(parts))
    # If you are just merging a few strings,
    # using a plus sign (+) is usually sufficient.
    a = 'Is Chicago'
    b = 'Not Chicago?'
    print(a + ' ' + b)
    print('{} {}'.format(a, b))
    print(a + ' ' + b)
    # Simplified version
    a = 'Hello' 'World'
    print(a)
    a, b, c = 'a', 'b', 'c'
    # Ugly
    print(a + ':' + b + ':' + c)
    # Still ugly
    print(':'.join([a, b, c]))
    # better
    print(a, b, c, sep=':')

    # But use '+' is not a good way to connect a large number of strings,
    # because the operaton will cause memory copying and garbage collection
    # To avoid:
    s = ''
    for p in parts:
        s += p
    # Use Generator expression to optimize
    data = ['ACME', 50, 91.1]
    print(','.join(str(d) for d in data))

    # When mixing I/O operations and string concatenation operations,
    # sometimes you need to study your program carefully.
    # version1
    # if the strings that need to connect are very small, this version is good,
    # because the I/0 operations always slow in general.
    str1, str2 = 'small size 1', 'small size 2'
    with open('./test.txt', 'w+') as f:
        f.write(str1 + str2)

    # version2
    # if the strings are very big, this version2 is more efficient. bacase it
    # avoid to create a big temporary results and copy large amounts of memory
    #  block data
    str1, str2 = 'big size 1', 'big size 2'
    with open('./test.txt', 'w+') as f:
        f.write(str1)
        f.write(str2)

    # The last, if you want to build a lot of small strings, you can use
    # generator expression
    def sample():
        yield 'Is'
        yield 'Chicago'
        yield 'Not'
        yield 'Chicago?'

    print(sample())

    with open('./test.txt', 'w+') as f:
        for part in sample():
            f.write(part)

    def combine(source, maxsize):
        parts = []
        size = 0
        for part in source:
            parts.append(part)
            size += len(part)
            if size > maxsize:
                yield ' '.join(parts)
                parts = []
                size = 0
        yield ' '.join(parts)

    # 结合文件操作
    print('111')
    with open('./test.txt', 'w+') as f:
        for part in combine(sample(), 32768):
            print(part)
            f.write(part)


# Question11: insert variables in string
def insert_variables_in_strings():
    # Use format()
    s = '{name} has {n} messages.'
    print(s.format(name='Guido', n=37))

    # If you want to find the variables that can be replaced in the
    # variable domain, You can use the format_map() and the vars()
    name = 'Guido'
    n = 37
    print(s.format_map(vars()))

    # Use vars() to represents a object
    class Info:
        def __init__(self, name, n):
            self.name = name
            self.n = n

    a = Info('Guido', 37)
    print(s.format_map(vars(a)))

    # but format() or format_map() can not solve the situation that variables
    # lost. So we need to definite a object that includes __missing__() method
    class safesub(dict):
        """防止key找不到"""

        def __missing__(self, key):
            return '{' + key + '}'

    del n
    print(s.format_map(safesub(vars())))

    # if the format or format_map is used a lot, you can do like this:
    import sys
    def sub(text):
        # Sys._getframe(1) returns the caller's stack frame. F_locals to get
        # local variables.
        return text.format_map(safesub(sys._getframe(1).f_locals))

    name = 'Guido'
    n = 37
    print(sub('Hello {name}'))
    print(sub('You have {n} messages.'))
    print(sub('Your favorite color is {color}'))

    # you should prefer choose format or format_map instead of following:
    import string
    s = string.Template('$name has $n messages.')
    print(s.substitute(vars()))


# Question12: Format the string with the specified column width
def format_string_with_the_specified_column_width():
    s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
    the eyes, not around the eyes, don't look around the eyes, \
    look into my eyes, you're under."

    # Use the textwrap
    import textwrap
    print(textwrap.fill(s, 70))
    print(textwrap.fill(s, 40))
    print(textwrap.fill(s, 40, initial_indent='    '))
    print(textwrap.fill(s, 40, subsequent_indent='    '))

    # To get the terminal length
    import os
    print(os.get_terminal_size().columns)


# Question13: handle html and xml in string
def handle_html_and_xml_in_string():
    s = 'Elements are written as "<tag>text</tag>".'
    import html
    print(s)
    print(html.escape(s))
    print(html.escape(s, quote=False))

    # If you want to deal ASCII text and add the not ASCII text into it.
    # you can use errors='xmlcharrefreplace'
    s = 'Spicy Jalapeño'
    print(s.encode('ascii', errors='xmlcharrefreplace'))

    # Use HTML Parser
    s = 'Spicy &quot;Jalape&#241;o&quot.'
    from html.parser import HTMLParser
    p = HTMLParser()
    print(p.unescape(s))
    t = 'The prompt is &gt;&gt;&gt;'
    from xml.sax.saxutils import unescape
    print(unescape(t))


# Qustion14: String token parser
def parse_a_token_scream_from_string():
    text = 'foo = 23 + 42 * 10'

    # As usual, you would like to transfer string to a tuple list
    tokens = [('NAME', 'foo'), ('EQ', '='), ('NUM', '23'), ('PLUS', '+'),
              ('NUM', '42'), ('TIMES', '*'), ('NUM', '10')]
    # To attain it, we need to  write a regex expression to match it.
    # we use ?P<TOKENNAME> to given string a name for later use.
    NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
    NUM = r'(?P<NUM>\d+)'
    PLUS = r'(?P<PLUS>\+)'
    TIMES = r'(?P<TIMES>\*)'
    EQ = r'(?P<EQ>=)'
    WS = r'(?P<WS>\s+)'
    import re
    master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))

    # Use scanner() to call match method over and over again to match the text
    scanner = master_pat.scanner('foo = 42')
    print(scanner.match())
    print(scanner.match())
    print(scanner.match())
    print(scanner.match())
    print(scanner.match())
    print(scanner.match())

    def generate_tokens(pat, text):
        from collections import namedtuple
        Token = namedtuple('Token', ['type', 'value'])
        scanner = pat.scanner(text)
        for m in iter(scanner.match, None):
            yield Token(m.lastgroup, m.group())

    # Example use
    for tok in generate_tokens(master_pat, 'foo = 42'):
        print(tok)
    print('----')
    # Produces output
    # Token(type='NAME', value='foo')
    # Token(type='WS', value=' ')
    # Token(type='EQ', value='=')
    # Token(type='WS', value=' ')
    # Token(type='NUM', value='42')

    tokens = (tok for tok in generate_tokens(master_pat, text)
              if tok.type != 'WS')
    for tok in tokens:
        print(tok)
    print('----')

    # The first important thing that you should know is you must  certain the
    # regex expression that you write must include all the situations of text
    # sequence. If not, the scanner will be stopped.
    text = 'foo = 23 ? 42 * 10'
    tokens = (tok for tok in generate_tokens(master_pat, text)
              if tok.type != 'WS')
    for tok in tokens:
        print(tok)
    print('----')

    # The second thing that you should know if a pattern is sub string of a more
    # long pattern. ：You need to make sure the long mode is written in front.

    LT = r'(?P<LT><)'
    LE = r'(?P<LE><=)'
    EQ = r'(?P<EQ>=)'
    master_pat = re.compile('|'.join([LE, LT, EQ])) # Correct
    # master_pat = re.compile('|'.join([LT, LE, EQ])) # Incorrect

    # And the last, you need to check the patter of sub string
    PRINT = r'(?P<PRINT>print)'
    NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'

    master_pat = re.compile('|'.join([PRINT, NAME]))

    for tok in generate_tokens(master_pat, 'printer'):
        print(tok)

    # Outputs :
    # Token(type='PRINT', value='print')
    # Token(type='NAME', value='er')


if __name__ == '__main__':
    # split_complex_string()

    # match_the_head_or_end()

    # use_strings_with_shell_wildcards()

    # match_the_head_or_end()

    # search_and_replace_text()

    # the_shortest_match_mode()

    # multi_line_matching_mode()

    # match_unicode_in_regex()

    # delete_unwanted_characters_in_a_string()

    # clean_text_string()

    # convert_string_to_int()

    # standardize_unicode_text()

    # string_alignment()

    # merge_multiple_string_to_a_big_one()

    # insert_variables_in_strings()

    # handle_html_and_xml_in_string()

    parse_a_token_scream_from_string()
