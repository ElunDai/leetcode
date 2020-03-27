#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List, Tuple, Dict
from utils import LeetCode

def febonacci(N):
    yield 1
    last = 1
    cur = 1
    for _ in range(N-1):
        ret = cur + last
        yield ret
        last = cur
        cur = ret

class Solution:
    @staticmethd
    def run(self, s):
        slen = len(s)
        for i in range(slen):
            j = i
            while j < slen:
                print(s[i:j + 1])
                j += 1

if __name__ == "__main__":
    leetcode = LeetCode()
    leetcode.add_case({'a', 'abc', 'b', 'c'}, "abc")
    leetcode.add_case(["a", "aa", "aab", "aabc", "ab", "abc", "b", "bc", "bcd", "c", "cd"], "abcd")

    feb = list(febonacci(26))

    leetcode.test()
