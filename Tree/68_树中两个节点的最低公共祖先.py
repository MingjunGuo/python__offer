class Solution():
    def __init__(self, root, node1, node2):
        self.root = root
        self.node1 = node1
        self.node2 = node2

    def get_path(self, root, node, ret):
        '''
        获取节点的路径
        :param node:
        :param ret:
        :return:
        '''
        if not root or not node:
            return False
        ret.append(root)
        if root == node:
            return True
        left = self.get_path(root.left, node, ret)
        right = self.get_path(root.right, node, ret)
        if left or right:
            return True
        ret.pop()

    def get_last_common_node(self):
        '''
        获取公共节点
        :return:
        '''
        route1 = []
        route2 = []
        ret1 = self.get_path(self.root, self.node1, route1)
        ret2 = self.get_path(self.root, self.node2, route2)
        ret = None
        if ret1 and ret2:
            length = len(route1) if len(route1) <= len(route2) else len(route2)
            index = 0
            while index < length:
                if route1[index] == route2[index]:
                    return route1[index]
                index += 1
        return ret