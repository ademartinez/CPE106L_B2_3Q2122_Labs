"""
CPE106L_B1_3Q2122 Problem 1
Author: Neil Ade Martinez
Filename: stats.py
Program Description: Calculates mode, median, and mean from a list.
"""

def mode(list):
    if len(list) == 0:
        return 0

    theDictionary = {}
    for word in list:
        number = theDictionary.get(word, None)
        if number == None:
            theDictionary[word] = 1
        else:
            theDictionary[word] = number + 1

    theMaximum = max(theDictionary.values())
    modeList = []
    for key in theDictionary:
        if theDictionary[key] == theMaximum:
            modeList.append(key)
    return modeList   

def median(list):
    if len(list) == 0:
        return 0

    list.sort()
    midpoint = int(len(list) / 2)
    if len(list) % 2 == 1:
        return list[midpoint]      
    else:
        return (list[midpoint] + list[midpoint - 1]) / 2

def mean(list):
    if len(list) == 0:
        return 0

    listMean = 0
    for num in list:
        listMean += num
    return listMean / len(list)

def main():
    list = [17, 38, 4, 10, 16, 11, 16]
    print("The numbers in the list are:", list)
    print ("The Mode is:", mode(list))
    print ("The Median is:", median(list))
    print ("The Mean is:", mean(list))
main()