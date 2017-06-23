from contextlib import contextmanager


class API:
    def __init__(self, bo, daof):
        self.__bo = bo(daof())

    @contextmanager
    def executar(self):
        with self.__bo.session_scope() as sessao:
            yield sessao

    def __persistir(self, metodo, obj):
        return metodo(obj)

    def listar(self) -> object:
        return self.__bo.recuperar()

    def buscar(self, reg_id) -> object:
        return self.__bo.recuperar(reg_id)

    def busca_atributo(self, **args) -> object:
        return self.__bo.recuperar(**args)

    def cadastrar(self, obj) -> object:
        reg = self.__persistir(self.__bo.cadastrar, obj)
        return reg

    def atualizar(self, obj) -> object:
        reg = self.__persistir(self.__bo.atualizar, obj)
        return reg

    def excluir(self, obj) -> object:
        reg = self.__persistir(self.__bo.excluir, obj)
        return reg