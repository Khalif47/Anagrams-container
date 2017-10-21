from task_2_BST import BinarySearchTree
from task_1_anagram import quick_sort


class Anagram:
    def __init__(self):
        self.words = None
        self.binary = BinarySearchTree()

    def add_word(self, word):
        '''

        :param word:
        :return:
        :complexity best O(NlogN), worst O(N**2)
        '''
        anagram = quick_sort(word)
        self.binary.insert(anagram, word)

    def query(self, word):
        '''

        :param word:
        :return:
        :complexity best O(NlogN), worst O(N):
        '''
        anagram = quick_sort(word)
        return self.binary.search(anagram)

    def print(self):
        '''
        :complexity O(N):
        :return:
        '''
        self.binary.print_preorder()

    def file_read(self, filename):
        filename = open(filename)
        for line in filename:
            for word in line.split():
                word = word.strip(',')
                word = word.strip(':')
                word = word.strip('.')
                word = word.strip('_')
                word = word.strip('-')
                word = word.strip(';')
                word = word.strip('?')
                word = word.strip(',')
                self.add_word(word)
        filename.close()

