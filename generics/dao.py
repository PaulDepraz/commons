from abc import ABCMeta, abstractclassmethod
from generics.model import Model


class ABCSingleton(ABCMeta):
    instance = None

    def __call__(cls, *args, **kw):
        if not cls.instance:
            cls.instance = super().__call__(*args, **kw)
        return cls.instance


class DAO(metaclass=ABCMeta):
    """
    Data Access Object is an Abstract Class
    Must be initialized using 'DAO.register(<DAO>)'
    """

    @abstractclassmethod
    def create(self, obj): pass

    @abstractclassmethod
    def retrieve(self, _id): pass

    @abstractclassmethod
    def retrieve_all(self): pass

    @abstractclassmethod
    def update(self, obj): pass

    @abstractclassmethod
    def delete(self, obj): pass


class DAOSingleton(metaclass=ABCSingleton):
    """
    Data Access Object is an Abstract Class
    Must be initialized using 'DAO.register(<DAO>)'
    """

    @abstractclassmethod
    def create(self, obj): pass

    @abstractclassmethod
    def retrieve(self, _id): pass

    @abstractclassmethod
    def retrieve_all(self): pass

    @abstractclassmethod
    def update(self, obj): pass

    @abstractclassmethod
    def delete(self, obj): pass


class DAOFactory(metaclass=ABCSingleton):

    @abstractclassmethod
    def __init__(self): pass

    @abstractclassmethod
    def get_instance(self, cls): pass


class DAOI(DAO):
    """
    Generic interface for all DAO implementations
    This class garantees an interface between data objects and odbcs or orms connectors
    """

    def __init__(self, dao):
        if not isinstance(dao, DAO):
            raise
        self._dao = dao

    def create(self, obj):
        if not isinstance(obj, Model):
            raise
        return self._dao.create(obj)

    def retrieve(self, _id=None) -> object:
        return self._dao.retrieve(_id)

    def retrieve_all(self) -> list:
        return self._dao.retrieve_all()

    def update(self, obj):
        if not isinstance(obj, Model):
            raise
        return self._dao.update(obj)

    def delete(self, obj):
        if not isinstance(obj, Model):
            raise
        return self._dao.delete(obj)
