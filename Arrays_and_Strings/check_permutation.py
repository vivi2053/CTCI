
from collections import defaultdict


# Time Complexity: O(m+n)
# Space Complexity: O(c) where c is the size of the character set
def cp_hashmap(string_tup):
    s1, s2 = string_tup
    if len(s1) != len(s2):
        return False
    hash1, hash2 = defaultdict(int),  defaultdict(int)
    for c in s1:
        hash1[c] += 1
    for c in s2:
        hash2[c] += 1

    if hash1 == hash2:
        return True
    else:
        return False


# Time Complexity: O(nlogn)
# Space Complexity: O(n)
def cp_sort_and_check(string_tup):
    s1, s2 = string_tup
    s1, s2 = list(s1), list(s2)
    if len(s1) != len(s2):
        return False
    s1.sort()
    s2.sort()
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True


if __name__ == '__main__':
    test_cases = [("gasd", "agds"), ("lkjh", "lkfj"), ("faster", "rastef"), ("a", "")]
    for test in test_cases:
        print(cp_sort_and_check(test))
