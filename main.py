def numtoword(num):
    if num == 0:
        return "zero"
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
             "nineteen"]
    words = ""
    if num >= 1000:
        words += ones[num // 1000] + " thousand "
    num %= 1000
    if num >= 100:
        words += ones[num // 100] + " hundred "
    num %= 100
    if 10 <= num <= 19:
        words += teens[num - 10] + " "
        num = 0
    elif num >= 20:
        words += tens[num // 10] + " "
        num %= 10
    if 1 <= num <= 9:
        words += ones[num] + " "
    return words.strip()


n = int(input())
word = numtoword(n)
print(word)
