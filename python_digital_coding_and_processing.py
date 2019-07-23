# Question1： read and write csv data
def read_and_write_csv_data():
    """
    stocks.csv
    Symbol,Price,Date,Time,Change,Volume
    "AA",39.48,"6/11/2007","9:36am",-0.18,181800
    "AIG",71.38,"6/11/2007","9:36am",-0.15,195500
    "AXP",62.58,"6/11/2007","9:36am",-0.46,935000
    "BA",98.31,"6/11/2007","9:36am",+0.12,104800
    "C",53.08,"6/11/2007","9:36am",-0.25,360900
    "CAT",78.29,"6/11/2007","9:36am",-0.23,225400
    :return:
    """

    import csv
    with open('stocks.csv') as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        for row in f_csv:
            pass

    # more maintainer
    from collections import namedtuple
    with open('stock.csv') as f:
        f_csv = csv.reader(f)
        headings = next(f_csv)
        Row = namedtuple('Row', headings)
        for r in f_csv:
            row = Row(*r)
            # Process row

    # Another method： Using the DictReader
    import csv
    with open('stocks.csv') as f:
        f_csv = csv.DictReader(f)
        for row in f_csv:
            # process row
            # row['Symbol'] row['Change']
            pass

    # Write to CSV datas by using the writer object
    headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
    rows = [('AA', 39.48, '6/11/2007', '9:36am', -0.18, 181800),
            ('AIG', 71.38, '6/11/2007', '9:36am', -0.15, 195500),
            ('AXP', 62.58, '6/11/2007', '9:36am', -0.46, 935000),
            ]

    with open('stocks.csv', 'w') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(rows)

    # 如果你有一个字典序列的数据，可以像这样做：
    headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
    rows = [{'Symbol': 'AA', 'Price': 39.48, 'Date': '6/11/2007',
             'Time': '9:36am', 'Change': -0.18, 'Volume': 181800},
            {'Symbol': 'AIG', 'Price': 71.38, 'Date': '6/11/2007',
             'Time': '9:36am', 'Change': -0.15, 'Volume': 195500},
            {'Symbol': 'AXP', 'Price': 62.58, 'Date': '6/11/2007',
             'Time': '9:36am', 'Change': -0.46, 'Volume': 935000},
            ]

    with open('stocks.csv', 'w') as f:
        f_csv = csv.DictWriter(f, headers)
        f_csv.writeheader()
        f_csv.writerows(rows)

    # Preference for csv module partitioning or parsing CSV data
    # this way is not recommended
    with open('stocks.csv') as f:
        for line in f:
            row = line.split(',')
    # 使用这种方式的一个缺点就是你仍然需要去处理一些棘手的细节问题。 比如，如果某些字段值被
    # 引号包围，你不得不去除这些引号。 另外，如果一个被引号包围的字段碰巧含有一个逗号，那么
    # 程序就会因为产生一个错误大小的行而出错。
    # 默认情况下，csv 库可识别Microsoft Excel所使用的CSV编码规则。
    # Example of reading tab-separated values
    with open('stock.tsv') as f:
        f_tsv = csv.reader(f, delimiter='\t')
        for row in f_tsv:
            # Process row
            ...
    # 如果你正在读取CSV数据并将它们转换为命名元组，需要注意对列名进行合法性认证。
    # 例如，一个CSV格式文件有一个包含非法标识符的列头行，类似下面这样：
    # Street Address,Num-Premises,Latitude,Longitude 5412 N CLARK,10,41.980262,-87.668452
    import re
    with open('stock.csv') as f:
        f_csv = csv.reader(f)
        headers = [re.sub('[^a-zA-Z_]', '_', h) for h in next(f_csv)]
        Row = namedtuple('Row', headers)
        for r in f_csv:
            row = Row(*r)
            # Process row
            ...
    # 还有重要的一点需要强调的是，csv产生的数据都是字符串类型的，它不会做任何其他类型的转换。
    # 如果你需要做这样的类型转换，你必须自己手动去实现。 下面是一个在CSV数据上执行其他类型
    # 转换的例子：
    # this convert 实际是传递的一个闭包
    col_types = [str, float, str, str, float, int]
    with open('stocks.csv') as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        for row in f_csv:
            # Apply conversions to the row items
            row = tuple(
                convert(value) for convert, value in zip(col_types, row))
            ...
    # 另外，下面是一个转换字典中特定字段的例子：
    print('Reading as dicts with type conversion')
    field_types = [('Price', float),
                   ('Change', float),
                   ('Volume', int)]

    with open('stocks.csv') as f:
        for row in csv.DictReader(f):
            row.update((key, conversion(row[key]))
                       for key, conversion in field_types)
            print(row)


# Question2: read and write json data
def read_and_write_json_data():
    # To json
    import json

    data = {
        'name': 'ACME',
        'shares': 100,
        'price': 542.23
    }

    json_str = json.dumps(data)

    # To string
    data = json.loads(json_str)

    # handle with file
    # Writing JSON data
    with open('data.json', 'w') as f:
        json.dump(data, f)

    # Reading data back
    with open('data.json', 'r') as f:
        data = json.load(f)

    # SON编码支持的基本数据类型为 None ， bool ， int ， float 和 str ， 以及包含这些
    # 类型数据的lists，tuples和dictionaries。
    # 比如，True会被映射为true，False被映射为false，而None会被映射为null。
    json.dumps(False)  # false
    d = {'a': True,
         'b': 'Hello',
         'c': None}
    json.dumps(d)  # '{"b": "Hello", "c": null, "a": true}'

    # Using pprint let the code more beauty
    from pprint import pprint
    pprint(d)

    # 一般来讲，JSON解码会根据提供的数据创建dicts或lists。 如果你想要创建其他类型的对象，
    # 可以给 json.loads() 传递object_pairs_hook或object_hook参数。
    # 例如，下面是演示如何解码JSON数据并在一个OrderedDict中保留其顺序的例子：
    s = '{"name": "ACME", "shares": 50, "price": 490.1}'
    from collections import OrderedDict
    data = json.loads(s, object_pairs_hook=OrderedDict)
    print(data)

    # 下面是如何将一个JSON字典转换为一个Python对象例子：
    class JSONObject:
        def __init__(self, d):
            self.__dict__ = d
    data = json.loads(s, object_hook=JSONObject)
    print(data.name)
    print(data.shares)
    print(data.price)

    data = json.loads(s, object_pairs_hook=OrderedDict)
    print(json.dumps(data))
    print(json.dumps(data, indent=4))

    # 如果你想序列化对象实例，你可以提供一个函数，它的输入是一个实例，
    # 返回一个可序列化的字典。例如：
    def serialize_instance(obj):
        d = {'__classname__': type(obj).__name__}
        d.update(vars(obj))
        return d
    # 如果你想反过来获取这个实例，可以这样做：
    # Dictionary mapping names to known classes
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    classes = {
        'Point': Point
    }

    def unserialize_object(d):
        clsname = d.pop('__classname__', None)
        if clsname:
            cls = classes[clsname]
            obj = cls.__new__(cls)  # Make instance without calling __init__
            for key, value in d.items():
                setattr(obj, key, value)
            return obj
        else:
            return d

    p = Point(2, 3)
    s = json.dumps(p, default=serialize_instance)
    print(s)  # '{"__classname__": "Point", "y": 3, "x": 2}'
    a = json.loads(s, object_hook=unserialize_object)
    print(a)
    print(a.x)
    print(a.y)


# Question3: Encoding and decoding hexadecimal numbers
def encoding_and_decoding_hexadecimal_numbers():
    # You want to decode a hex string into a byte string or encode a byte string
    # into a hex string
    # Initial byte string
    s = b'hello'
    # Encode as hex
    import binascii
    h = binascii.b2a_hex(s)
    print(h)
    # Decode back to bytes
    print(binascii.a2b_hex(h))


# Question4: Encoding and decoding Base64 data
def encoding_and_decoding_base64_data():
    # Some byte data
    s = b'hello'
    import base64
    # Encode as Base64
    a = base64.b64encode(s)
    print(a)

    # Decode from Base64
    print(base64.b64decode(a))

    # Base64编码仅仅用于面向字节的数据比如字节字符串和字节数组。 此外，编码处理的输出结果
    # 总是一个字节字符串。 如果你想混合使用Base64编码的数据和Unicode文本，你必须添加一个
    # 额外的解码步骤。例如：
    a = base64.b64encode(s).decode('ascii')
    print(a)


if __name__ == '__main__':
    # read_and_write_csv_data()
    # read_and_write_json_data()
    # encoding_and_decoding_hexadecimal_numbers()
    encoding_and_decoding_base64_data()