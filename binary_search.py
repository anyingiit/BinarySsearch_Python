import math
import random


def generationRandomIntList(length: int, maxNumber: int) -> list[int]:
    """
    生成整数随机数组, 最小为0
    :param length: 数组最大长度
    :param maxNumber: 随机数最大数字
    :return: [length]长度的随机数数组, 其中最大数字为[maxNumber]
    """
    result: list[int] = []
    for _ in range(length):
        result.append(int(random.random() * maxNumber))
    return result


def generationRandomOrderIntList(length: int, maxNumber: int) -> list[int]:
    randomIntList = generationRandomIntList(length, maxNumber)
    randomIntList.sort()

    return randomIntList


def binary_search(numberList: [], item: float):
    """
    二分搜索
    :param numberList: 有序数字列表
    :param item: 目标数字
    :return: [下标] | None
    """
    print("数组长度为:", len(numberList))
    print("预估最坏查找次数:", math.log2(len(numberList)))

    countLoop = 0

    low = 0
    high = len(numberList) - 1
    while low <= high:
        countLoop += 1
        print("第", countLoop, "次查找")

        mid = (low + high) // 2
        guess = numberList[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


if __name__ == '__main__':
    # orderList = [1, 5, 6, 8, 11, 34, 40, 55]
    # searchResult = binary_search(orderList, 11)
    #
    # print(searchResult)

    for i in range(1000):
        randomOrderIntListMaxLength = 1000
        randomOrderIntListLength = int(random.random() * randomOrderIntListMaxLength)
        randomOrderIntListMaxNumberScope = 1000000
        randomOrderIntListMaxNumber = int(random.random() * randomOrderIntListMaxNumberScope)
        randomOrderIntList = generationRandomOrderIntList(randomOrderIntListLength, randomOrderIntListMaxNumber)
        searchTargetIndex = int(random.random() * randomOrderIntListLength)
        searchTargetItem = randomOrderIntList[searchTargetIndex]

        actuallyIndex = binary_search(randomOrderIntList, searchTargetItem)
        if actuallyIndex != searchTargetIndex:
            print("查找结果错误!")
        else:
            print("查找结果正确!!!")
        print("================================")
