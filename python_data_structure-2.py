# Question1: delete repeated elements in list
def delete_repeated_elements():
    # Method1: Use the set()
    def distFunc1(a):
        """使用集合去重"""
        a = list(set(a))
        print(a)

    def distFunc2(a):
        """将一个列表的数据取出放到另一个列表中，中间作判断"""
        list = []
        for i in a:
            if i not in list:
                list.append(i)
        list.sort()
        print(list)

    def distFunc3(a):
        """使用字典"""
        b = {}
        b = b.fromkeys(a)
        c = list(b.keys())
        print(c)

    list_a = [1, 1, 2, 2, 3, 3]
    distFunc1(list_a)
    distFunc2(list_a)
    distFunc3(list_a)


if __name__ == '__main__':
    delete_repeated_elements()