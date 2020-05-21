"""
    Author:W
    Purpose:
    Created:2020/4/26
"""
import getRandomData

def main():
    # create a new object
    data = getRandomData.GetRandomData()

    dataType = input("(1) Please input data type: ")
    # only 'int' and 'float' need dataRange and screenRange
    if dataType == 'int' or dataType == 'float':
        dataRange = list(map(int, input("(2) Please input data range (!Separate by space): ").strip().split()))
        screenFactor = list(map(int, input("(3) Please input data screen range (!Separate by space): ").strip().split()))
        num = input("(4) Please input the number of item: ")
        result = data.dataSampling(dataType, dataRange, int(num))
        screenResult = data.dataScreening(result, dataType, dataRange, screenFactor, int(num))
    # 'str' needs a substring to find
    elif dataType == 'str':
        screenFactor = input("(2) Please input the substring required (!No more than 8 digits): ")
        num = input("(3) Please input the number of item: ")
        result = data.dataSampling(dataType, " ", int(num))
        screenResult = data.dataScreening(result, dataType, " ", screenFactor, int(num))

    if len(result) == 0:
        print("& Randomly generated set is empty. ")
    else:
        print("& Randomly generated set is : " + str(result))
        print("& After screening, the set is :" + str(screenResult))

if __name__ == "__main__":
    main()
