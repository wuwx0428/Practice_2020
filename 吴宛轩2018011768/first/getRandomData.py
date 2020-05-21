"""
    Author:W
    Purpose:
    Created:2020/4/26
"""
import random
import string
from collections.abc import Iterable

class GetRandomData:

    dataRange = string.ascii_letters + string.digits + "@#!~"

    def dataSampling(self, dataType, dataRange, num, strlen=8):
        '''
        purpose: randomly generated data
        :param dataRange: to creat a iterator
        :param num: the number of data
        :param strlen: the length of string
        :return: set()
        '''
        result = set()
        try:
            if (isinstance(dataRange, Iterable) == "false"):
                raise StopIteration
            while (len(result) < num):
                # int type
                if dataType == 'int':
                    it = iter(dataRange)
                    item = random.randint(next(it), next(it))
                    result.add(item)
                # float type
                elif dataType == 'float':
                    it = iter(dataRange)
                    item = random.uniform(next(it), next(it))
                    result.add(item)
                # str type
                elif dataType == 'str':
                    item = ''.join(random.SystemRandom().choice(GetRandomData.dataRange) for _ in range(strlen))
                    result.add(item)
                # Not supported type
                else:
                    raise TypeError
        except TypeError:
            print("Error: Sorry, this type is not supported.")
        except StopIteration:
            print("Error: Cannot iterate.")
        except MemoryError:
            print("Error: Out of memory.")
        finally:
            return result

    def dataScreening(self, result, dataType, dataRange, screenFactor, num):
        screenResult = set()
        # int type
        if dataType == 'int':
            for item in result:
                if item >= screenFactor[0] and item <= screenFactor[-1]:
                    screenResult.add(item)
        # float type
        elif dataType == 'float':
            for item in result:
                if item >= screenFactor[0] and item <= screenFactor[-1]:
                    screenResult.add(item)
        # str type
        elif dataType == 'str':
            for item in result:
                if screenFactor in item:
                    screenResult.add(item)
        return screenResult

