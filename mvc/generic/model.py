from rest.jsonable import JSONAble


class Model(JSONAble):
    """ MVC Concrete Model """

    def __init__(self, reg_id=None):
        """
        :param reg_id: Registry ID
        :return:
        """
        self.reg_id = reg_id

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.reg_id == other.reg_id

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        if self.reg_id is None:
            raise AssertionError('O objeto está desincronizado com o banco de dados.')
        return hash(''.join(dir(self))) ^ hash(self.reg_id)

    def __repr__(self):
        return '%s(%s)' % (self.__class__.__name__, self.reg_id)

    def __self__(self):
        return self


class AModel(type):
    """ MVC Abstract Model """

    def __new__(cls, cls_name, superclasses, attribute_dict):
        cls.reg_id = None
        return type.__new__(cls, cls_name, superclasses, attribute_dict)

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.reg_id == other.reg_id

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        if self.reg_id is None:
            raise AssertionError('O objeto está desincronizado com o banco de dados.')
        return hash(self.__class__.__name__) ^ hash(self.__dict__.keys()) ^ hash(self.reg_id)

    def __repr__(self):
        return '%s(%s, %s)' % (self.__class__.__name__, self.reg_id, self.__hash__())
