from collections import defaultdict


# Time Complexity: O(n) where n is the length of the list
# Space Complexity: O(c) where c is the size of the character set

def palinperm_hashmap(s):
    count_ = defaultdict(int)
    odd_cnt = 0
    for c in s:
        if c != " ":
            count_[c] += 1

    for v in count_.values():
        if v % 2 != 0:
            if odd_cnt == 0:
                odd_cnt += 1
            else:
                return False
    return True


def palinperm_sort_check(s):
    s = list(s)
    s.sort()
    lp = rp = 0
    while (rp < len(s)):
        while ()


if __name__ == "__main__":
    test_cases = [("taco cat"), "batty cat"]
    for test in test_cases:
        print(palinperm_hashmap(test))
