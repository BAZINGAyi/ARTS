# 遍历一个object的所有属性，并print每一个属性名？
def traverse_all_property_in_class():
    class Car:
        def __init__(self, name, loss):  # loss [价格，油耗，公里数]
            self.name = name
            self.loss = loss

        def getName(self):
            return self.name

        def getPrice(self):
            # 获取汽车价格
            return self.loss[0]

        def getLoss(self):
            # 获取汽车损耗值
            return self.loss[1] * self.loss[2]

    Bmw = Car("BMW", [60, 9, 500])  # 实例化一个宝马车对象
    print(getattr(Bmw, "name"))  # 使用getattr()传入对象名字,属性值。
    print(dir(Bmw))  # 获Bmw所有的属性和方法\


# Question2: Write a class and let it support as many operators as possible?
def support_many_operators():
    class Array:
        __list = []

        def __init__(self):
            print("constructor")

        def __del__(self):
            print("destruct")

        def __str__(self):
            return "this self-defined array class"

        def __getitem__(self, key):
            return self.__list[key]

        def __len__(self):
            return len(self.__list)

        def Add(self, value):
            self.__list.append(value)

        def Remove(self, index):
            del self.__list[index]

        def DisplayItems(self):
            print("show all items---")
            for item in self.__list:
                print(item)


if __name__ == '__main__':
    # traverse_all_property_in_class()
    support_many_operators()
