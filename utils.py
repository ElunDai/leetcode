import time


class LeetCode:
    def __init__(self):
        self.cases = []

    def add_case(self, answer, *args, **kwargs):
        self.cases.append((answer, args, kwargs))

    def test(self, entry):
        for answer, args, kwargs in self.cases:
            start = time.time()
            ret = entry(*args, **kwargs)
            end = time.time()
            if answer is not None and ret != answer:
                print('Failed test case. Result: {}, Expect: {}'
                      .format(ret, answer))
                continue
            print('Result: {}. Pass test case in {} seconds.'
                  .format(ret, end - start))


class GraphPath:
    def __init__(self, **kwargs):
        self.__dict__.update(**kwargs)

    def __repr__(self):
        return str(self.__dict__)


class Graph:
    def __init__(self, graph, **kwargs):
        self.graph = graph
        self.__dict__.update(**kwargs)

    def value(self, path):
        """从graph中获取path对应的值"""
        return None

    def generate(self, path):
        """下一步可选择的路径列表"""
        return []

    def cut(self, path):
        """如果返回True则剪枝该条路径"""
        return False

    def path(self, **kwargs):
        """路径的工厂函数"""
        return dict(**kwargs)

    def visit(self, path):
        """访问路径，对路径进行操作"""
        pass

    def dfs(self, init_path):
        """从init_path路径开始深度搜索"""
        queue = [init_path]
        while len(queue) > 0:
            path = queue.pop(-1)
            if self.cut(path) is True:
                continue
            self.visit(path)
            queue.extend(self.generate(path))

