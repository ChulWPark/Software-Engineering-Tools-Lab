#! /user/local/bin/python3.4

def filterByLetter(sentence, c):
    sentence_split = sentence.split()
    perfect = []
    for i in sentence_split:
        if i[0] == c or i[-1] == c:
            if i not in perfect:
                perfect.append(i)

    return perfect

def getCumulativeSum():
    sum = 0
    perfect = []
    for i in range(1,101):
        sum = sum + i
        perfect.append(sum)

    return perfect

if __name__ == "__main__":
    print("TASK 1")
    print(filterByLetter("the power of this engine matches that of the one we had last year", "t"))
    print(filterByLetter("the power of this engine matches that of the one we had last year", "r"))
    print(filterByLetter("the power of this engine matches that of the one we had last year", "e"))
    print("TASK 2")
    print(getCumulativeSum())
