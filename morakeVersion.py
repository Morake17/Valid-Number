class morakeVersion:
    def isNumber(s: str) -> bool:
        i = 0
        num_signs = 0
        curr = s[i]
        string_len = len(s)
        valid_chars = "1234567890"
        while i < string_len:
            curr = s[i]
            if curr == "+" or curr == "-":
                num_signs += 1
            if curr == ".":
                break
            if not morakeVersion.is_present(valid_chars, curr) or num_signs > 1:
                return False
            i+=1

        return True

    def is_present(data, entry):
        for el in data:
            if el == entry:
                return True
        return False

    def validNumSigns(number: str):
        numPlus = number.count("+")
        numMinus = number.count("-")

        return numPlus + numMinus <= 1


numbers = ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]
not_numbers = ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]

for num in numbers:
    if morakeVersion.isNumber(num):
        print(num, " is a number")
    else:
        print(num, " is not a number")

print("******************************")
for num in not_numbers:
    if morakeVersion.isNumber(num):
        print(num, " is a number")
    else:
        print(num, " is not a number")