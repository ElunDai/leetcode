from typing import List, Tuple, Dict
from utils import LeetCode, Graph, array2D


class Map(Graph):
    def __init__(self, graph, **kwargs):
        self.graph = graph
        self.high = len(graph)
        self.width = len(graph[0])
        self.visited =array2D(self.high, self.width)
        self.__dict__.update(**kwargs)

    def value(self, path):
        """从graph中获取path对应的值"""
        return self.graph[path[0]][path[1]]
    
    def generate(self, path):
        gen = []
        for shift_i, shift_j in [(0, 1), (-1, 0), (-1, 0), (1, 0)]:
            next_path = [path[0] + shift_i, path[1] + shift_j]
            if next_path[0] >= 0 and next_path[0] < self.high and \
                    next_path[1] >= 0 and next_path[1] < self.width and \
                    not self.visited[next_path[0]][next_path[1]]:
                    gen.append(next_path)
        return gen
    
    def visit(self, path):
        """访问路径，对路径进行操作"""
        print(path)
        self.visited[path[0]][path[1]] = 1
        print(self.visited)

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        mp = Map(graph = grid)
        mp.bfs([0, 0])


class Solution2:
    def distance(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def maxDistance(self, grid: List[List[int]]) -> int:
        land = []
        sea = []
        for r, row in enumerate(grid):
            for c, col in enumerate(row):
                if col == 1:
                    land.append((r, c))
                else:
                    sea.append((r, c))
        if not (land and sea):
            return -1
        print(land)
        print(sea)

        nearist = 0
        for s_i, s_aria in enumerate(sea):
            cur_nearest = None
            for l_i, l_aria in enumerate(land):
                dist = self.distance(s_aria, l_aria)
                cur_nearest = min(dist, cur_nearest) if cur_nearest else dist
            if cur_nearest > nearist:
                print('update farest sea aria to {} with min distanc of {}'.format(s_aria, cur_nearest))
                nearist = cur_nearest
        print(s_aria, nearist)
        return nearist


if __name__ == '__main__':

    leetcode = LeetCode()
    leetcode.add_case(-1, [[0,0,0],[0,0,0],[0,0,0]])
    leetcode.add_case(-1, [[1,1,1],[1,1,1],[1,1,1]])
    leetcode.add_case(2, [[1,0,1],[0,0,0],[1,0,1]])
    leetcode.add_case(4, [[1,0,0],[0,0,0],[0,0,0]])

    solution = Solution()
    leetcode.test(solution.maxDistance)
