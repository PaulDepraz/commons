from contextlib import contextmanager

from commons.generics.dao import DAO, DAOFactory, DAOSingleton, DAOI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class AlchemyDAOFactory(DAOFactory):

    def __init__(self, db_url):
        self.__db_url = db_url

    def get_instance(self, *args):
        return AlchemyDAO(self.__db_url)


class AlchemyDAO(DAOSingleton):

    def __init__(self, db_url):
        DAO.register(AlchemyDAO)
        self.__db_url = db_url
        self.__session = None

    @contextmanager
    def session_scope(self):
        """Provide a transactional scope around a series of operations."""
        Session = sessionmaker(bind=create_engine(self.__db_url, echo=False))
        Session.expire_on_commit = False
        self.__session = Session()
        try:
            yield self.__session
            self.__session.commit()
        except Exception as e:
            self.__session.rollback()
            raise e
        finally:
            self.__session.close()

    def create(self, obj):
        self.__session.add(obj)
        self.__session.flush()
        return obj

    def create_all(self, obj):
        self.__session.add_all(obj)
        self.__session.flush()
        return obj

    def retrieve(self, cls, reg_id):
        return self.__session.query(cls).get(reg_id)

    def retrieve_all(self, cls):
        return self.__session.query(cls).all()

    def update(self, obj):
        return self.create(obj)

    def delete(self, obj):
        res = self.retrieve(obj.reg_id)
        self.__session.delete(res)
        self.__session.flush()
        return obj

    def find_by(self, cls, **attributes):
        return self.__session.query(cls).filter_by(**attributes).all()


class DAOI(DAOI):
    """
    SQLAlchemy specific changes to DAOI
    """
    def __init__(self, dao):
        super().__init__(dao)

    def retrieve(self, cls, _id=None) -> object:
        return self._dao.retrieve(cls, _id)

    def retrieve_all(self, cls) -> list:
        return self._dao.retrieve_all(cls)

    def find_by(self, cls, **attributes):
        return self._dao.find_by(cls, **attributes)

    @property
    def session_scope(self):
        return self._dao.session_scope
