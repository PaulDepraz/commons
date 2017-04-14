def flatten(a):
    """
    Joins a sequence of sequences into a single sequence.  (One-level flattening.)
    E.g., join([(1,2,3), [4, 5], [6, (7, 8, 9), 10]]) = [1,2,3,4,5,6,(7,8,9),10]
    This is very efficient, especially when the subsequences are long.
    """
    n = sum([len(b) for b in a])
    l = [None]*n
    i = 0
    for b in a:
        j = i+len(b)
        l[i:j] = b
        i = j
    return l


def chunks(_list, chunck_size):
    """
    Yield successive n-sized chunks from list.
    :param chunck_size: int
    :param _list: [list]
    """
    for index in xrange(0, len(_list), chunck_size):
        yield _list[index: index + chunck_size]