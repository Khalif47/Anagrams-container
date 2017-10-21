from task_2_Sorted_Linked import SortedList


def test():
    t = SortedList()
    t.add(3)
    t.add(1)
    t.add(3)
    assert str(t) == "1, 3, ", "wrong list"
    t.add(12)
    t.add(-4)
    assert str(t) == "-4, 1, 3, 12, ", "wrong list"


if __name__ == '__main__':
    test()
    print('All test cases passing! ')
