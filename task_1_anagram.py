def quick_sort(array):
    '''
    This is a quick sorting algorithm

    :param array:
    :return: list_store
    :complexity worst case O(N) best case O(NlogN)


    '''
    try:
        start = 0
        end = len(array) - 1
        quick_sort_aux(array, start, end)
        return array
    except TypeError:
        list_store = []
        for i in range(end + 1):
            list_store.append(array[i])
        quick_sort_aux(list_store, start, end)
        list_store = ''.join(list_store)
        return list_store


def quick_sort_aux(array, start, end):
    '''

    :param array:
    :param start:
    :param end:
    :return:
    '''
    if start < end:
        boundary = partition(array, start, end)
        quick_sort_aux(array, start, boundary - 1)
        quick_sort_aux(array, boundary + 1, end)


def partition(array, start, end):
    '''
    This partitions the list

    :param array:
    :param start:
    :param end:
    Complexity O(N)
    :return:
    '''
    mid = (start + end) // 2
    pivot = array[mid]
    array[mid], array[start] = array[start], array[mid]
    index = start
    for k in range(index + 1, end + 1):
        if array[k] < pivot:
            index += 1
            array[k], array[index] = array[index], array[k]
    array[start], array[index] = array[index], array[start]
    return index



