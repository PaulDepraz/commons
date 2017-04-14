import pickle
import os


def get_pickle(path):
    """
    Unpickle ;)
    :param path: file path
    """
    with os.open(path) as obj_file:
        obj = pickle.load(obj_file)
    return obj


def save_pickle(obj, path):
    """
    Save pickle replacing the old one
    :param path: file path
    :param obj: object you want to store
    """
    pickled_data = pickle.dumps(obj, protocol=2)
    file_ = open(path, 'w+')
    file_.truncate()
    print >> file_, pickled_data
