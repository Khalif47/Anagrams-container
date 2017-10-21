from task_2_Sorted_Linked import SortedList


class BinarySearchTreeNode:
    def __init__(self, key, item=None, left=None, right=None):
        self.key = key
        self.item = SortedList()
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.result = None

    def _is_empty(self):
        '''
        Checks if the list is empty

        complexity O(N)
        :return:
        '''
        return self.root is None

    def insert(self, key, value):
        '''

        :param key:
        :param value:
        :return:
        :complexity best case O(1) if root item is correct position worst case O(n**2)
        '''
        self.root = self.insert_aux(self.root, key, value)

    def insert_aux(self, current, key, value):
        if current is None:
            current = BinarySearchTreeNode(key)
            current.item.add(value)
            return current
        elif key < current.key:
            current.left = self.insert_aux(current.left, key, value)
            return current
        elif key > current.key:
            current.right = self.insert_aux(current.right, key, value)
            return current
        else:
            current.item.add(value)
            return current

    def search(self, key):
        '''
        searches

        :param key:
        :return:
        :complexity best case O(1) worst case O(N)
        '''
        self.search_aux(self.root, key)
        return self.result

    def search_aux(self, current, key):
        if current is not None:
            if key == current.key:
                self.result = str(current.item)
            elif key < current.key:
                self.search_aux(current.left, key)
            elif key > current.key:
                self.search_aux(current.right, key)

        else:
            raise KeyError('Key not in table')

    def print_preorder(self):
        '''
        prints everything in the BST including list items

        :return:
        :complexity O(N)
        '''
        self._print_preorder_aux(self.root)

    def _print_preorder_aux(self, current):
        if current is not None:
            print(str(current.key) + ': ' + str(current.item))
            self._print_preorder_aux(current.left)
            self._print_preorder_aux(current.right)


# if __name__ == '__main__':
#     t = BinarySearchTree()
#     t.insert(14, 'boo')
#     t.insert(15, 'res')
#     t.insert(13, 'ao')
#     t.insert(15, 'me')
#     t.insert(15, 'aie')
#     t.insert(100, 'no')
#     print(t.search(100))
#
#     t.print_preorder()
