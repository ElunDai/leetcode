from typing import List, Tuple, Dict
from utils import LeetCode

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        ax1, ay1, ax2, ay2 = rec1
        bx1, by1, bx2, by2 = rec2

        # right
        # left
        # top
        # bottom
        if ax1 >= bx2 or \
           ax2 <= bx1 or \
           ay1 >= by2 or \
           ay2 <= by1:
            return False
        return True


if __name__ == '__main__':

    leetcode = LeetCode()
    leetcode.add_case(True, [0,0,2,2], [1,1,3,3])
    leetcode.add_case(False, [0,0,1,1], [1,0,2,1])
    leetcode.add_case(True, [0,0,1,1], [0,0,1,1])

    solution = Solution()
    leetcode.test(solution.isRectangleOverlap)
