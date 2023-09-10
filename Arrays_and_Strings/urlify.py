# Time Complexity: O(n)
# Space Complexity: O(1)
def urlify_simple(inputs):
    str_, len_ = list(inputs[0]), inputs[1]
    lp = len_-1
    rp = len_ + str_.count(" ") * 2
    rp = len(str_)-1
    while (lp >= 0):
        if str_[lp] != ' ':
            str_[rp] = str_[lp]
            lp -= 1
            rp -= 1
        else:
            rp -= 3
            str_[rp+1:rp+4] = ["%", "2", "0"]
            lp -= 1
    return "".join(str_)


if __name__ == "__main__":
    test_cases = [("Mr John Smith    ", 13)]
    for test in test_cases:
        print(urlify_simple(test))
