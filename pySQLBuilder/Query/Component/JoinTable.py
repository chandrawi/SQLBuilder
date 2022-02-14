from ...Structure import Join
from ...Builder import JoinBuilder
from typing import Iterable

class JoinTable :

    def __join(self, joinTable, joinType) :
        joinObject = Join.create(joinTable, joinType)
        if isinstance(self.builder, JoinBuilder) :
            self.builder.addJoin(joinObject)
        else :
            raise Exception('Builder object does not support JOIN query')
        return self

    def innerJoin(self, joinTable) :
        return self.__join(joinTable, Join.INNER_JOIN)

    def leftJoin(self, joinTable) :
        return self.__join(joinTable, Join.LEFT_JOIN)

    def rightJoin(self, joinTable) :
        return self.__join(joinTable, Join.RIGHT_JOIN)

    def outerJoin(self, joinTable) :
        return self.__join(joinTable, Join.OUTER_JOIN)

    def on(self, baseColumn, joinColumn) :
        if isinstance(self.builder, JoinBuilder) :
            lastJoin = self.builder.lastJoin()
            if lastJoin is not None :
                lastJoin.addColumn(baseColumn, joinColumn)
        return self

    def using(self, columns) :
        if isinstance(columns, str) or not isinstance(columns, Iterable) :
            columns = (columns,)
        if isinstance(self.builder, JoinBuilder) :
            lastJoin = self.builder.lastJoin()
            if lastJoin is not None :
                for column in columns :
                    lastJoin.addColumn(column)
        return self
