from Node import Node
from Iterator import ListIterator

class SortedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def __len__(self):
        '''
        Finds length of list

        :return self.count:
        :complexity O(1)
        '''
        return self.count

    def __iter__(self):
        '''
        Iterates through list

        :complexity O(N)
        :return:
        '''
        return ListIterator(self.head)

    def is_empty(self):
        '''
        Checks if list is empty

        :return boolean:
        :complexity best case O(1)
        '''
        return self.count == 0

    def reset(self):
        '''
        resets the lists

        :return:
        complexity O(1)
        '''
        self.__init__()

    def _get_node(self, index):
        '''
        accesses the node specified

        :param index:
        :return node:
        :complexity O(N)
        '''
        assert 0 <= index < self.count, "index error"
        node = self.head
        for _ in range(index):
            node = node.next
        return node

    def add(self, item):
        '''
        adds an item to the list and maintains sorted order

        :param item:
        :return:
        :complexity best case O(1) and worst case O(N)
        '''
        if self.is_empty():
            self.head = Node(item)
            self.count += 1
        elif self.count > 0:
            check = self.count - 1
            while check > 0 and self._get_node(check).item > item:
                check = check - 1
            if self._get_node(check).item == item:
                node = self._get_node(check)
                node.item = item
            elif check == 0 and self._get_node(check).item > item:
                self.head = Node(item, self.head)
                self.count += 1
            else:
                node = self._get_node(check)
                node.next = Node(item, node.next)
                self.count += 1

    # def __str__(self):
    #     ret = ""
    #     for i in range(self.count):
    #         ret += self._get_node(i).item + ", "
    #     return ret
    #
    def __str__(self):
        ret = ""
        for i in self:
            ret += str(i) + ", "
        return ret


