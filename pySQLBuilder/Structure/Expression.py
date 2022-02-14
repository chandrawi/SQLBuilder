from typing import Iterable

class Expression :

    def __init__(self, expression: tuple, alias: str = '', params: tuple = ()) :
        countExp = len(expression)
        countPar = len(params)
        if countExp < countPar :
            params = params[:countExp]
        if countExp > countPar :
            for i in range(countPar, countExp) : params += (None,)
        self.__expression = expression
        self.__alias = alias
        self.__params = params

    def expression(self) -> tuple :
        return self.__expression

    def alias(self) -> str :
        return self.__alias

    def params(self) -> tuple :
        return self.__params

    @classmethod
    def create(cls, expression, alias = '', params: Iterable = ()) :
        exps = ()
        if isinstance(expression, str) :
            exps = expression.split('?')
        elif isinstance(expression, Iterable) :
            exps = tuple(expression)
        return Expression(exps, str(alias), params)
