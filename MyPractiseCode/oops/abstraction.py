from abc import ABC, abstractmethod


class Computer(ABC):
    @abstractmethod
    def features(self):
        pass


class DetailsInformation(Computer):
    def features(self):
        print("it have SSD Features")


if __name__ == '__main__':
    ob = DetailsInformation()
    ob.features()
