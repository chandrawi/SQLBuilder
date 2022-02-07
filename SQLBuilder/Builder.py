from .Structure import Table, Column, Value

class BaseBuilder :

    SELECT = 1
    INSERT = 2
    UPDATE = 3
    DELETE = 4
    SELECT_DISTINCT = 5
    SELECT_UNION = 6
    SELECT_INTERSECT = 7
    SELECT_MINUS = 8
    INSERT_COPY = 9

    _builderType = 0
    _table = None
    _columns = ()
    _values = ()

    def builderType(self, type: int = 0) -> int :
        if (type > 0 and type <= 9) :
            self._builderType = type
        return self._builderType

    def setTable(self, table: Table) :
        self._table = table

    def getTable(self) -> Table :
        return self._table

    def addColumn(self, column) :
        if isinstance(column, Column) :
            self._columns = self._columns + (column,)

    def getColumns(self) -> tuple :
        return self._columns

    def countColumns(self) -> int :
        return len(self._columns)

    def addValue(self, value : Value) :
        self._values = self._values + (value,)

    def getValues(self) -> tuple :
        return self._values

    def countValues(self) -> int :
        return len(self._values)

class SelectBuilder(BaseBuilder) :

    _where = ()
    _groupBy = ()
    _having = ()
    _orderBy = ()
    _limit = ()

class InsertBuilder(BaseBuilder) :

    _limit = ()

class UpdateBuilder(BaseBuilder) :

    _where = ()
    _limit = ()

class DeleteBuilder(BaseBuilder) :

    _where = ()
    _limit = ()
