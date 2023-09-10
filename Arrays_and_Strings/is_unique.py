
# Time complexity: O(min(c, n)) where c is the length of the character set
# Space complexity: O(c) or O(1)
def is_unique_list_approach(s):
    if len(s) > 128:
        return False
    flags = [False for _ in range(128)]
    for c in s:
        if flags[ord(c)]:
            return False
        else:
            flags[ord(c)] = True
    return True


# Time complexity O(n) where n is the length of the input string.
# Space complexity O(1) as the size of the string doesn't increase beyond the number of possible characters
def is_unique_hashset_approach(s) -> bool:
    char_set = set()
    for c in s:
        if c in char_set:
            return False
        else:
            char_set.add(c)
    return True


# Time complexity: O(n^2)
# Space complexity: O(n)
def is_unique_no_ds(s):
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                return False
    return True


# time complexity: O(nlogn)
# spacy complexity: O(n)
def is_unique_no_ds2(s):
    s_list = list(s)
    s_list.sort()
    for i in range(0, len(s_list)-1):
        if s_list[i] == s_list[i+1]:
            return False
    return True


if __name__ == "__main__":
    test_cases = ["abcdea", "b", "", "jlodsg"]
    for test in test_cases:
        # print(is_unique_hashset_approach(test))
        # print(is_unique_list_approach(test))
        print(is_unique_no_ds(test))
