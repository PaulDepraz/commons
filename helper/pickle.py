import os


def get_pickle(path, default={}):
    """
    Unpickle ;)
    :param default: default value for inexistent file
    :param path: file path
    """
    obj = default
    if os.path.exists(path):
        obj = pickle.load(open(path, 'rb'))
    return obj


def save_pickle(obj, path):
    """
    Save pickle replacing the old one
    :param path: file path
    :param obj: object you want to store
    """
    pickle.dump(obj, open(path, 'wb'))
