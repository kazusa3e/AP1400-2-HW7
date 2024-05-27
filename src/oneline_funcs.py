def adjacentElementsProduct(inputArray):
    return max([inputArray[i] * inputArray[i + 1] for i in range(len(inputArray) - 1)])

def allLongestStrings(inputArray):
    return [_ for _ in inputArray if len(_) == max([len(_) for _ in inputArray])]

def checkPalindrome(inputArray):
    return inputArray == inputArray[::-1]

def commonCharacterCount(s1, s2):
    return sum([min(s1.count(c), s2.count(c)) for c in set(s1)])

def areSimilar(A, B):
    return sorted(A) == sorted(B) and sum([a != b for a, b, in zip(A, B)]) <= 2

def palindromeRearranging(inputString):
    return sum([inputString.count(_) % 2 for _ in set(inputString)]) <= 1

def arrayReplace(inputArray, elemToReplace, substitutionElem):
    return [(_ if _ != elemToReplace else substitutionElem) for _ in inputArray]

def evenDigitsOnly(n):
    return all([int(ch) % 2 == 0 for ch in str(n)])

def alphabeticShift(inputString):
    return ''.join([chr(((ord(_) - ord('a') + 1) % 26) + ord('a')) for _ in inputString])

def firstDigit(inputString):
    return int(list(filter(lambda ch: ch >= '0' and ch <= '9', inputString))[0])