#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://leetcode-cn.com/problems/word-rectangle-lcci/
from typing import List, Tuple, Dict
from utils import LeetCode
from collections import defaultdict

class Solution:
    def maxRectangle(self, words: List[str]) -> List[str]:
        d = defaultdict(list)
        for word in words:
            d[len(word)].append(word)
        print(d)

if __name__ == "__main__":
    leetcode = LeetCode()
    leetcode.add_case(["aa","aa"], ["aa"])
    leetcode.add_case(["this", "real", "hard"], ["this", "real", "hard", "trh", "hea", "iar", "sld"])


    solution = Solution()
    leetcode.test(solution.maxRectangle)
