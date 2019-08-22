# author : YANG CUI
"""
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first
non-whitespace character is found. Then, starting from this character, takes an optional
initial plus or minus sign followed by as many numerical digits as possible, and interprets
them as a numerical value.

The string can contain additional characters after those that form the integral number,
which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number,
or if no such sequence exists because either str is empty or it contains only whitespace
characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.
"""
import re
def atoi(inputString):
    # compute the length of the inputString
    stringLen = len(inputString)
    metFirstNonWhiteSpace = False
    # signs = 0 for positive 1 for negative
    signs = 0
    convertedNum = 0
    # check for null string
    if inputString == "":
        return convertedNum
    # basic loop structure
    for i in range(stringLen):
        if (re.match('[0-9]',inputString[i]) or re.match('[+|-]',inputString[i])) and metFirstNonWhiteSpace == False:
            metFirstNonWhiteSpace = True
            if re.match('[0-9]',inputString[i]):
                signs = 0
                convertedNum = convertedNum * 10 + int(inputString[i])
            elif re.match('[+|-]',inputString[i]):
                if inputString[i] == "+":
                    signs = 0
                else:
                    signs = 1
        elif not (re.match('[0-9]',inputString[i]) or re.match('[+|-]',inputString[i]) or inputString[i] == ' ') and metFirstNonWhiteSpace == False:
            return 0
        elif (re.match('[0-9]',inputString[i])) and metFirstNonWhiteSpace == True:
            convertedNum = convertedNum * 10 + int(inputString[i])
        elif not (re.match('[0-9]',inputString[i])) and metFirstNonWhiteSpace == True:
            if convertedNum > 2 ** 31 - 1 and signs == 0:
                convertedNum = 2 ** 31 - 1
                return convertedNum
            elif convertedNum > 2 ** 31 and signs == 1:
                convertedNum = -2 ** 31
                return convertedNum
            elif convertedNum == 0 or signs == 0:
                return convertedNum
            else:
                return -convertedNum
        if i == stringLen - 1:
            if convertedNum > 2 ** 31 - 1 and signs == 0:
                convertedNum = 2 ** 31 - 1
                return convertedNum
            elif convertedNum > 2 ** 31 and signs == 1:
                convertedNum = -2 ** 31
                return convertedNum
            elif convertedNum == 0 or signs == 0:
                return convertedNum
            else:
                return -convertedNum



print(atoi("2147483648"))