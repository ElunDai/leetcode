from typing import List, Tuple, Dict
from utils import LeetCode

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        lasts = {char : i for i, char in enumerate(S)}
        print(lasts)
        start = 0
        last = 0
        ret = []
        for i, char in enumerate(S):
            last = max(last, lasts[char])
            if last == i:
                print('end range {} to {}'.format(start, last))
                ret.append(last - start + 1)
                start = last + 1
        return ret


if __name__ == '__main__':
    leetcode = LeetCode()
    leetcode.add_case([9, 7, 8], "ababcbacadefegdehijhklij")

    solution = Solution()
    leetcode.test(solution.partitionLabels)
