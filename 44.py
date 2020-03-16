from typing import List, Tuple, Dict
from utils import LeetCode
from fnmatch import fnmatch

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return fnmatch(s, p)


if __name__ == '__main__':

    leetcode = LeetCode()
    leetcode.add_case(False, "aa", "a")
    leetcode.add_case(True, "aa", "*")
    leetcode.add_case(False, "cb", "?a")
    leetcode.add_case(True, "adceb", "*a*b")
    leetcode.add_case(False, "acdcb", "a*c?b")
    leetcode.add_case(None,
            "aaaabaaaabbbbaabbbaabbaababbabbaaaababaaabbbbbbaabbbabababbaaabaabaaaaaabbaabbbbaababbababaabbbaababbbba",
           "*****b*aba***babaa*bbaba***a*aaba*b*aa**a*b**ba***a*a*")

    solution = Solution()
    leetcode.test(solution.isMatch)
