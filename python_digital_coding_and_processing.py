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


