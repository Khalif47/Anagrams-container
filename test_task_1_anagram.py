from task_1_anagram import quick_sort


def test_anagram():
    assert quick_sort('life') == 'efil', 'wrong sorting'
    assert quick_sort('mine') == 'eimn', 'wrong sorting'
    assert quick_sort('on') == 'no', 'wrong sorting'
    assert quick_sort('filler') == 'efillr', 'wrong sorting'
    assert quick_sort('smile') == 'eilms', 'wrong sorting'


if __name__ == '__main__':
    test_anagram()
    print('\n\nquick sort functioning properly')


