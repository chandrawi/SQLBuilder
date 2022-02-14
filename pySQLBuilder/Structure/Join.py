from .Table import Table
from .Column import Column
from typing import Mapping

class Join :

    NO_JOIN = 0
    INNER_JOIN = 1
    LEFT_JOIN = 2
    RIGHT_JOIN = 3
    OUTER_JOIN = 4

    table = ''

    def __init__(self, joinType: int, baseTable: str, joinTable: str, joinAlias: str = '') :
        self.__joinType = joinType
        self.__baseTable = baseTable
        self.__joinTable = joinTable
        self.__joinAlias = joinAlias
        self.__baseColumns = ()
        self.__joinColumns = ()
        self.__usingColumns = ()

    def joinType(self) -> int :
        return self.__joinType

    def baseTable(self) -> str :
        return self.__baseTable

    def joinTable(self) -> str :
        return self.__joinTable

    def joinAlias(self) -> str :
        return self.__joinAlias

    def baseColumns(self) -> tuple :
        return self.__baseColumns

    def joinColumns(self) -> tuple :
        return self.__joinColumns

    def usingColumns(self) -> tuple :
        return self.__usingColumns

    @classmethod
    def create(cls, joinTable, joinType) :
        cls.table = Table.table
        validType = cls.getType(joinType)
        if isinstance(joinTable, Mapping) :
            key = next(iter(joinTable.keys()))
            joinAlias = str(key)
            joinObject = Join(validType, Table.table, str(joinTable[key]), joinAlias)
            Table.table = joinAlias
        else :
            joinTable = str(joinTable)
            joinObject = Join(validType, Table.table, joinTable)
            Table.table = joinTable
        return joinObject

    @classmethod
    def getType(cls, joinType) -> int :
        if isinstance(joinType, int) :
            validType = joinType
            if joinType < 0 or joinType > 4 : validType = 0
        else :
            if joinType == 'INNER JOIN' or joinType == 'INNER' :
                validType = Join.INNER_JOIN
            elif joinType == 'LEFT JOIN' or joinType == 'LEFT' :
                validType = Join.LEFT_JOIN
            elif joinType == 'RIGHT JOIN' or joinType == 'RIGHT' :
                validType = Join.RIGHT_JOIN
            elif joinType == 'OUTER JOIN' or joinType == 'OUTER' :
                validType = Join.OUTER_JOIN
            else :
                validType = Join.NO_JOIN
        return validType

    def addColumn(self, baseColumn, joinColumn = None) :
        table = Table.table
        Table.table = Join.table
        baseColumnObject = Column.create(baseColumn)
        Table.table = table
        if joinColumn is None :
            self.__usingColumns += (baseColumnObject,)
        else :
            joinColumnObject = Column.create(joinColumn)
            self.__baseColumns += (baseColumnObject,)
            self.__joinColumns += (joinColumnObject,)
