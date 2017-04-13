"""
 sector3.core.moeda

    >>> Moeda(10)
    10,00 R$
    >>> Moeda('10,78')
    10,78 R$
    >>> Moeda('2.638,69')
    2.638,69 R$
    >>> Moeda(10, r_partilha=False)/16
    [0,63 R$, 0,63 R$, 0,63 R$, 0,63 R$, 0,63 R$, 0,63 R$, 0,63 R$, 0,63 R$, 0,62 R$, 0,62 R$, 0,62 R$, 0,62 R$, 0,62 R$, 0,62 R$, 0,62 R$, 0,62 R$]
    >>> reduce(Moeda.__add__, Moeda(10)/16)
    10,00 R$
    >>> reduce(Moeda.__add__, Moeda(10)/300)
    10,00 R$
    >>> reduce(Moeda.__add__, Moeda(119)/16)
    119,00 R$
    >>> reduce(Moeda.__add__, Moeda(119.67)/16)
    119,67 R$
    >>> Moeda(-10)
    -10,00 R$
    >>> Moeda(-10, r_partilha=False)/3
    [-3,34 R$, -3,33 R$, -3,33 R$]
    >>> Moeda(-10, r_partilha=False)/3
    [-3,34 R$, -3,33 R$, -3,33 R$]
    >>> Moeda(-119, r_partilha=False)/16
    [-7,44 R$, -7,44 R$, -7,44 R$, -7,44 R$, -7,44 R$, -7,44 R$, -7,44 R$, -7,44 R$, -7,44 R$, -7,44 R$, -7,44 R$, -7,44 R$, -7,43 R$, -7,43 R$, -7,43 R$, -7,43 R$]
    >>> reduce(Moeda.__add__, Moeda(-119, r_partilha=False)/16)
    -119,00 R$
    >>> reduce(Moeda.__add__, Moeda(-119.67)/16)
    -119,67 R$
    >>> reduce(Moeda.__add__, Moeda(-10)/16)
    -10,00 R$
    >>> Moeda(10)/-3
    Traceback (most recent call last):
    TypeError: Only positive integers allowed to divide.
    >>> Moeda(10)/Moeda(1)
    Traceback (most recent call last):
    TypeError: Only positive integers allowed to divide.
    >>> Moeda(10)/-3.0
    Traceback (most recent call last):
    TypeError: Only positive integers allowed to divide.
    >>> Moeda(10)/2.0
    Traceback (most recent call last):
    TypeError: Only positive integers allowed to divide.
"""

from decimal import Decimal, ROUND_DOWN
from moneyed import Money, BRL
import locale
from random import shuffle


class Moeda(Money):
    def __init__(self, amount=Decimal('0.0'), currency=BRL, r_partilha=True):
        if isinstance(amount, str):
            amount = locale.atof(amount)
        Money.__init__(self, amount, currency)
        self.__random_div = r_partilha

    def __repr__(self):
        return locale.currency(self.amount, True, True)

    def __str__(self):
        return str(self.amount)

    def __truediv__(self, other):

        if not (isinstance(other, int) and other > 0):
            raise TypeError('Only positive integers allowed to divide.')

        # Calcula quociente da divisão
        divisor = other;
        quociente = (self.amount / divisor).quantize(Decimal('.01'), rounding=ROUND_DOWN)
        resultado = [Moeda(quociente) for r in range(divisor)]
        quocientes_somados = quociente * divisor

        return self.partilhar(divisor, quocientes_somados, resultado)

    def partilhar(self, divisor, quocientes_somados, resultado):
        # Verifica sinal do valor
        sinal = 1
        if self.amount < 0:
            sinal = -sinal

        # Partilha o resto
        resto = int((self.amount - quocientes_somados) * 100 * sinal)
        while resto > 0:
            for i in range(divisor):
                resultado[i] += (Moeda(0.01 * sinal))
                resto -= 1
                if resto < 1:
                    break

        # Retorna a lista embaralhada
        if self.__random_div:
            shuffle(resultado)
        return resultado


if __name__ == "__main__":
    import doctest
    import platform
    from functools import reduce

    if platform.system() == "Windows":
        LOCALE = "ptb_bra"
    else:
        LOCALE = "pt_BR"

    locale.setlocale(locale.LC_ALL, LOCALE)
    doctest.testmod()