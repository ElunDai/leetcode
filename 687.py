from typing import List, Tuple, Dict
from utils import LeetCode, Graph


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class TreeGraph(Graph):
    def value(self, path):
        """从graph中获取path对应的值"""
        return path.val

    def generate(self, path):
        """下一步可选择的路径列表"""
        return [path.left, path.right]

    def cut(self, path):
        """如果返回True则剪枝该条路径"""
        return False

    def path(self, **kwargs):
        """路径的工厂函数"""
        return TreeNode(**kwargs)

    def visit(self, path):
        """访问路径，对路径进行操作"""
        print(path.val)




class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        tree = TreeGraph(graph=root)
        tree.dfs(root)


if __name__ == '__main__':

    pass
    #  leetcode = LeetCode()
    #  leetcode.add_case(,)
    #  
    #  solution = Solution()
    #  leetcode.test(solution.)
