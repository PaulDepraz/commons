from commons.generics.model import Model


class Identificacao(Model):
    def __init__(self, pessoa, identificador, rotulo):
        self.validar(identificador)
        self.pessoa = pessoa
        self.identificador = identificador
        self.rotulo = rotulo
        super().__init__()

    def validar(self, identificador):
        pass


class IdentificacaoPessoaFisica(Model):
    def __init__(self, pessoa_fisica, identificador):
        self.validar(identificador)
        self.pessoa_fisica = pessoa_fisica
        self.identificador = identificador
        self.rotulo = self.__class__.__name__
        super().__init__()

    def validar(self, identificador):
        pass


class IdentificacaoPessoaJuridica(Model):
    def __init__(self, pessoa_juridica, identificador):
        self.validar(identificador)
        self.pessoa_juridica = pessoa_juridica
        self.identificador = identificador
        self.rotulo = self.__class__.__name__
        super().__init__()

    def validar(self, identificador):
        pass


class Telefone(Identificacao):
    pass


class Email(Identificacao):
    pass


class Website(Identificacao):
    pass


class CPF(IdentificacaoPessoaFisica):
    pass


class CNPJ(IdentificacaoPessoaJuridica):
    pass


class InscricaoEstadual(IdentificacaoPessoaJuridica):
    pass


class InscricaoMunicipal(IdentificacaoPessoaJuridica):
    pass


class LocalRegistroPessoaJuridica(Model):
    def __init__(self, pessoa_juridica, uf, cidade):
        self.pessoa_juridica = pessoa_juridica
        self.uf = str(uf).upper()
        self.cidade = str(cidade).title()
        super().__init__()

    def validar(self, uf, cidade):
        pass


class Endereco(Model):
    def __init__(self, pessoa, cep, numero, complemento, logradouro, bairro, uf, cidade):
        self.pessoa = pessoa
        self.cep = cep
        self.numero = numero
        self.complemento = complemento
        self.logradouro = str(logradouro).title()
        self.bairro = str(bairro).title()
        self.uf = str(uf).upper()
        self.cidade = str(cidade).title()
        super().__init__()


class Pessoa(Model):
    def __init__(self, nome):
        self.nome = str(nome)
        super().__init__()


class PessoaFisica(Pessoa):
    def __init__(self, nome, sobrenome):
        self.sobrenome = str(sobrenome)
        Pessoa.__init__(self, nome)


class PessoaJuridica(Pessoa):
    def __init__(self, nome, nome_fantasia):
        self.nome_fantasia = str(nome_fantasia)
        Pessoa.__init__(self, nome)

"""
class ClientePessoaFisica(Model):
    def __init__(self, pessoa_fisica, cliente):
        self.pessoa_fisica = pessoa_fisica
        self.cliente = cliente
        super().__init__()


class ClientePessoaJuridica(Model):
    def __init__(self, pessoa_juridica, cliente):
        self.pessoa_juridica = pessoa_juridica
        self.cliente = cliente
        super().__init__()


class InstituicaoPessoaJuridica(Model):
    def __init__(self, pessoa_juridica, instituicao):
        self.pessoa_juridica = pessoa_juridica
        self.instituicao = instituicao
        super().__init__()


class FornecedorPessoaJuridica(Model):
    def __init__(self, pessoa_juridica, fornecedor):
        self.pessoa_juridica = pessoa_juridica
        self.fornecedor = fornecedor
        super().__init__()
"""