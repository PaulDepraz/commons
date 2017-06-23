from commons.mvc.generic.dao import DAOFactory, DAOI


class BO:
    def __init__(self, daoi_cls, cls, dao_factory):
        if not isinstance(dao_factory, DAOFactory) and issubclass(daoi_cls, DAOI):
            raise AssertionError('Please provide valid DAOFactory and DAOI instances.')
        dao = dao_factory.get_instance(cls)
        self._daoi = daoi_cls(dao)
        self._cls = cls

    @staticmethod
    def validar(obj):
        pass

    def cadastrar(self, obj):
        if not isinstance(obj, self._cls):
            raise AssertionError('Object does not belong to this Business Case.')
        self.validar(obj)
        return self._daoi.create(obj)

    def atualizar(self, obj):
        if not isinstance(obj, self._cls):
            raise AssertionError('Object does not belong to this Business Case.')
        self.validar(obj)
        return self._daoi.update(obj)

    def excluir(self, obj):
        return self._daoi.delete(obj)

    def recuperar(self, _id=None):
        if _id:
            return self._daoi.retrieve(_id)
        return self._daoi.retrieve_all()