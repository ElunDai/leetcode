from typing import List, Tuple, Dict
from utils import LeetCode

# 最优装载问题 / 部分背包问题
# 本问题等于尽可能得把手头的饼干全部分完
# 胃口小的小朋友需要消耗的饼干代价小，优先满足胃口小的拿人头
# 饼干能发就发，题目没要求吃剩的饼干量，所以对当前胃口最小的小朋友能喂就喂，不能就丢
# 得出贪心策略：优先用最小的饼干满足胃口最小的小朋友

# 贪心法使用Exchange Argument证明：
# 假设存在一个非贪心的更优解，在前k步都与贪心完全一样，第k+1步交换为贪心策略的一个元素后新解不会更差，形成递推关系，所以贪心策略就是其中一个最优解。

# 证明优先使用最小的饼干：
# 有一个小朋友A，能满足他胃口的饼干有i和j（i <= j），假设给他分饼干j是最优的
# 现在把他的饼干更另一个分到更小饼干i的小朋友B交换饼干，A能被满足B也还是能被满足，因此贪心获得的新解不会更差

# 证明优先满足胃口最小的小朋友：
# 有一个饼干X，能满足胃口为ab的小朋友，假设把它分给小朋友b是最优的
# 现在把X分给的小朋友换成胃口更小的a，那么b将面临两种情况：
# 1. b能被另一块饼干满足，那若不交换这块饼干当然能满足a，不会减少被满足的人数
# 2. b不能被另一块饼干满足，那若不交换这块饼干当然也不能满足a，所以交换后能被满足的人数不变
# 所以贪心得出的新解不比最优解差，所以贪心算法就是其中一个最优解


class Solution:
    def findContentChildren(self, childs: List[int], biscuites: List[int]) -> int:
        childs.sort()  # 优先队列，优先满足最小的胃口的小朋友
        biscuites.sort()  # 优先队列，优先给最小的饼干给小朋友，满足不了才尝试更大的
        print(childs)
        print(biscuites)
        len_childs = len(childs)
        len_biscuite = len(biscuites)

        child_id = 0
        satisfied = 0
        biscuite_id = 0
        while biscuite_id < len_biscuite and child_id < len_childs:
            print("if {} >= {}:".format(biscuites[biscuite_id], childs[child_id]))
            if biscuites[biscuite_id] >= childs[child_id]:
                print('give him')
                satisfied += 1
                biscuite_id += 1
                child_id += 1
                continue
            biscuite_id += 1
        return satisfied


if __name__ == '__main__':
    leetcode = LeetCode()
    leetcode.add_case(1, [1, 2, 3], [1, 1])
    leetcode.add_case(2, [1, 2], [1, 2, 3])
    leetcode.add_case(2, [10,9,8,7], [5,6,7,8])
    leetcode.add_case(3, [1, 2, 4, 5, 6], [1, 1, 3, 4])
    leetcode.add_case(2, [1, 2, 4, 5, 6], [2, 2, 3])

    solution = Solution()
    leetcode.test(solution.findContentChildren)
