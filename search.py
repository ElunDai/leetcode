from typing import List, Tuple, Dict
from utils import Graph, LeetCode


class Graph1D(Graph):
    def value(self, path):
        return self.graph[path['loc']]

    def generate(self, path):
        locs = range(path['loc'] + 1, path['loc'] + 1 + self.value(path))
        return [self.path(loc=loc, deepth=path['deepth']+1) for loc in locs]

    def cut(self, path):
        if path['loc'] >= self.size:
            return True

    def visit(self, path):
        if path['loc'] >= self.size - 1:
            if self.min:
                self.min = min(path['deepth'], self.min)
            else:
                self.min = path['deepth']


class Solution1:
    """深度遍历"""
    def jump(self, nums: List[int]) -> int:
        g = Graph1D(nums, size=len(nums), min=None)
        g.dfs(g.path(loc=0, deepth=0))
        return g.min


class Solution2:
    """深度遍历"""
    def jump(self, nums: List[int]) -> int:
        nums_len = len(nums)
        max_rich = 0
        step = 0
        cur_step_range = 0
        for i, enegy in enumerate(nums):
            # 每步范围内选下一步可达位置最大的
            max_rich = max(i + enegy, max_rich)
            print('scan', i, enegy, max_rich)
            if i >= cur_step_range:
                # 不论更新了多少次max_rich，每一步范围内有且只跳可达位置最大那次
                if cur_step_range > nums_len:
                    break
                print('jump to', max_rich)
                step += 1
                cur_step_range = max_rich
        return step


if __name__ == '__main__':
    leetcode = LeetCode()
    leetcode.add_case(2, [2, 3, 1, 1, 4])
    leetcode.add_case(4, [6, 2, 6, 1, 7, 9, 3, 5, 3, 7, 2, 8, 9, 4, 7, 7, 2, 2, 8, 4, 6, 6, 1, 3])

    solution2 = Solution2()
    leetcode.test(solution2.jump)

    exit(0)

    solution1 = Solution1()
    leetcode.test(solution1.jump)
