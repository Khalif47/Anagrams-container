from task_2_BST import BinarySearchTree

def test():
    t = BinarySearchTree()
    t.insert(14, 'boo')
    t.insert(15, 'res')
    t.insert(13, 'ao')
    t.insert(15, 'me')
    t.insert(15, 'aie')
    t.insert(100, 'no')
    assert t.search(15) == "aie, me, res, ", "wrong list"



if __name__ == '__main__':
    test()
    print('all test cases passing')





