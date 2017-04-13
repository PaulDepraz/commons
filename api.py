from contextlib import contextmanager
from log import log
from flask_restful import Resource, abort, reqparse
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import BadRequest


class API:
    def __init__(self, bo, daof):
        self.__bo = bo(daof())

    @contextmanager
    def executar(self):
        with self.__bo.session_scope() as sessao:
            yield sessao

    def _persistir(self, metodo, obj):
        return metodo(obj)

    def listar(self) -> object:
        return self.__bo.recuperar()

    def buscar(self, reg_id) -> object:
        return self.__bo.recuperar(reg_id)

    def busca_atributo(self, **args) -> object:
        return self.__bo.recuperar(**args)

    def cadastrar(self, obj) -> object:
        reg = self._persistir(self.__bo.cadastrar, obj)
        return reg

    def atualizar(self, obj) -> object:
        reg = self._persistir(self.__bo.atualizar, obj)
        return reg

    def excluir(self, obj) -> object:
        reg = self._persistir(self.__bo.excluir, obj)
        return reg


class RestAPI(Resource):
    def __init__(self, core_api, post_kwargs=[], to_parse=[], patch_kwargs=None, log_file=None):
        self._api = core_api
        self._post_kwargs = post_kwargs
        self._patch_kwargs = patch_kwargs
        self._to_parse = to_parse
        self._log_file = log_file

    def _parse_obj(self, api_cadastro, _id):
        if not _id:
            return None
        obj = api_cadastro.buscar(_id)
        if not obj:
            raise FileNotFoundError
        return obj

    def get(self, _id=None):
        with tratamento_excecoes(self._log_file):
            if _id is not None:
                with self._api.executar():
                    obj = self._api.buscar(_id)
                    json_dict = obj.to_dict()
                return json_dict
            with self._api.executar():
                obj = self._api.listar()
                json_dict = {"results": [o.to_dict() for o in obj]}
            return json_dict

    def post(self, **args):
        if not self._post_kwargs:
            return 'Objeto não cadastrável.', 405
        with tratamento_excecoes(self._log_file):
            parser = reqparse.RequestParser()
            for kwargs in self._post_kwargs:
                parser.add_argument(**kwargs)
            args = parser.parse_args()
            with self._api.executar() as sessao:
                for api_cadastro, kw in self._to_parse:
                    args[kw] = self._parse_obj(api_cadastro, args[kw])
                if hasattr(self, '_post_parse'):
                    self._post_parse(args)
                obj = self._api.cadastrar(**args)
                json_dict = obj.to_dict()
            return json_dict, 201

    def delete(self, _id):
        if not _id:
            return 'Objeto não removível.', 405
        with tratamento_excecoes(self._log_file):
            with self._api.executar():
                obj = self._api.buscar(_id)
                if not obj:
                    raise FileNotFoundError
                self._api.excluir(obj)
            return 'Objeto removido', 204

    def patch(self, _id):
        if not _id or not self._patch_kwargs:
            return 'Objeto não atualizável.', 405
        with tratamento_excecoes(self._log_file):
            parser = reqparse.RequestParser()
            for kwargs in self._patch_kwargs:
                parser.add_argument(**kwargs)
            args = parser.parse_args()
            with self._api.executar() as sessao:
                if hasattr(self, '_patch_parse'):
                    self._patch_parse(args)
                obj = self._api.atualizar(_id, **args)
                json_dict = obj.to_dict()
            return json_dict, 200


@contextmanager
def tratamento_excecoes(log_file):
    try:
        yield
    except TypeError:
        log(log_file)
        abort(400, message="Mensagem mal formada ou atributo requerido não encontrado.")
    except SyntaxError:
        log(log_file)
        abort(400, message="Mensagem mal formada ou atributo requerido não encontrado.")
    except ConnectionError:
        log(log_file)
        abort(500, message="Banco de dados fora do ar.")
    except ValueError:
        log(log_file)
        abort(400, message="Mensagem mal formada ou atributo requerido não encontrado.")
    except AttributeError:
        log(log_file)
        abort(404, message="O objeto solicitado não existe.")
    except BadRequest:
        abort(400, message="Mensagem mal formada ou atributo requerido não encontrado.")
    except FileNotFoundError:
        abort(404, message="O objeto solicitado não existe.")
    except IntegrityError:
        log(log_file)
        abort(409, message="O registro já existe.")
    except Exception:
        log(log_file)
        abort(500, message="Não foi possível processar sua solicitação. Tente novamente mais tarde.")
