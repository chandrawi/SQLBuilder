from ...Structure import Clause, Expression
from ...Builder import WhereBuilder
from typing import Iterable

class Where :

    def beginWhere(self) :
        Clause.nestedConjunctive = Clause.CONJUNCTIVE_NONE
        Clause.nestedLevel -= 1
        return self

    def beginAndWhere(self) :
        Clause.nestedConjunctive = Clause.CONJUNCTIVE_AND
        Clause.nestedLevel -= 1
        return self

    def beginOrWhere(self) :
        Clause.nestedConjunctive = Clause.CONJUNCTIVE_OR
        Clause.nestedLevel -= 1
        return self

    def beginNotAndWhere(self) :
        Clause.nestedConjunctive = Clause.CONJUNCTIVE_NOT_AND
        Clause.nestedLevel -= 1
        return self

    def beginNotOrWhere(self) :
        Clause.nestedConjunctive = Clause.CONJUNCTIVE_NOT_OR
        Clause.nestedLevel -= 1
        return self

    def endWhere(self) :
        if isinstance(self.builder, WhereBuilder) :
            lastClause = self.builder.lastWhere()
            if lastClause is not None :
                lastLevel = lastClause.level()
                lastClause.level(lastLevel + 1)
        return self

    def __where(self, column, operator, value, conjunctive: int) :
        clauseObject = Clause.create(Clause.WHERE, column, operator, value, conjunctive)
        if isinstance(self.builder, WhereBuilder) :
            self.builder.addWhere(clauseObject)
        else :
            raise Exception('Builder object does not support WHERE query')
        return self

    def where(self, column, operator, value = None) :
        return self.__where(column, operator, value, Clause.CONJUNCTIVE_NONE)

    def andWhere(self, column, operator, value = None) :
        return self.__where(column, operator, value, Clause.CONJUNCTIVE_AND)

    def orWhere(self, column, operator, value = None) :
        return self.__where(column, operator, value, Clause.CONJUNCTIVE_OR)

    def notAndWhere(self, column, operator, value = None) :
        return self.__where(column, operator, value, Clause.CONJUNCTIVE_NOT_AND)

    def notOrWhere(self, column, operator, value = None) :
        return self.__where(column, operator, value, Clause.CONJUNCTIVE_NOT_OR)

    def whereExpression(self, expression, operator, value, params: Iterable = ()) :
        expressionObject = Expression.create(expression, '', params)
        return self.__where(expressionObject, operator, value, Clause.CONJUNCTIVE_AND)

    def orWhereExpression(self, expression, operator, value, params: Iterable = ()) :
        expressionObject = Expression.create(expression, '', params)
        return self.__where(expressionObject, operator, value, Clause.CONJUNCTIVE_OR)

    def notWhereExpression(self, expression, operator, value, params: Iterable = ()) :
        expressionObject = Expression.create(expression, '', params)
        return self.__where(expressionObject, operator, value, Clause.CONJUNCTIVE_NOT_AND)

    def notOrWhereExpression(self, expression, operator, value, params: Iterable = ()) :
        expressionObject = Expression.create(expression, '', params)
        return self.__where(expressionObject, operator, value, Clause.CONJUNCTIVE_NOT_OR)
