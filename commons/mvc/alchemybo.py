from commons.mvc.generic.bo import BO


class BO(BO):

    def __init__(self, daoi_cls, cls, dao_factory):
        super().__init__(daoi_cls, cls, dao_factory)

    def recuperar(self, _id=None, **attributes):
        if _id:
            return self._daoi.retrieve(self._cls, _id)
        if attributes:
            return self._daoi.find_by(self._cls, **attributes)
        return self._daoi.retrieve_all(self._cls)

    @property
    def session_scope(self):
        return self._daoi.session_scope
