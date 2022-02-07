from .Structure import Table, Column, Value, Clause, Order, Limit

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
    _limit = None

    def getWhere(self) -> tuple:
        return self._where

    def lastWhere(self) -> Clause :
        count = len(self._where)
        if count > 0 :
            return self._where[count-1]
        return None

    def countWhere(self) -> int :
        return len(self._where)

    def addWhere(self, where: Clause) :
        self._where += (where,)

    def editWhereNested(self, nestedConjunctive: int) :
        count = len(self._where)
        if count > 0 :
            self._where[count-1].nestedConjunctive = nestedConjunctive

    def getHaving(self) -> tuple :
        return self._having

    def lastHaving(self) -> Clause :
        count = len(self._having)
        if count > 0 :
            return self._having[count-1]
        return None

    def countHaving(self) -> int :
        return len(self._having)

    def addHaving(self, having: Clause) :
        self._having += (having,)

    def editHavingNested(self, nestedConjunctive: int) :
        count = len(self._having)
        if count > 0 :
            self._having[count-1].nestedConjunctive = nestedConjunctive

    def getGroup(self) -> tuple :
        return self._groupBy

    def countGroup(self) -> int :
        return len(self._groupBy)

    def addGroup(self, groupBy: Column) :
        self._groupBy = self._groupBy + (groupBy,)

    def getOrder(self) -> tuple :
        return self._orderBy

    def countOrder(self) -> int :
        return len(self._orderBy)

    def addOrder(self, orderBy: Order) :
        self._orderBy = self._orderBy + (orderBy,)

    def getLimit(self) -> tuple :
        return self._limit

    def hasLimit(self) -> bool :
        if self._limit is None : return False
        else : return True

    def setLimit(self, limit: Limit) :
        self._limit = limit

class InsertBuilder(BaseBuilder) :

    _limit = None

    def getLimit(self) -> tuple :
        return self._limit

    def hasLimit(self) -> bool :
        if self._limit is None : return False
        else : return True

    def setLimit(self, limit: Limit) :
        self._limit = limit

class UpdateBuilder(BaseBuilder) :

    _where = ()
    _limit = None

    def getWhere(self) -> tuple:
        return self._where

    def lastWhere(self) -> Clause :
        count = len(self._where)
        if count > 0 :
            return self._where[count-1]
        return None

    def countWhere(self) -> int :
        return len(self._where)

    def addWhere(self, where: Clause) :
        self._where += (where,)

    def editWhereNested(self, nestedConjunctive: int) :
        count = len(self._where)
        if count > 0 :
            self._where[count-1].nestedConjunctive = nestedConjunctive

    def getLimit(self) -> tuple :
        return self._limit

    def hasLimit(self) -> bool :
        if self._limit is None : return False
        else : return True

    def setLimit(self, limit: Limit) :
        self._limit = limit

class DeleteBuilder(BaseBuilder) :

    _where = ()
    _limit = None

    def getWhere(self) -> tuple:
        return self._where

    def lastWhere(self) -> Clause :
        count = len(self._where)
        if count > 0 :
            return self._where[count-1]
        return None

    def countWhere(self) -> int :
        return len(self._where)

    def addWhere(self, where: Clause) :
        self._where += (where,)

    def editWhereNested(self, nestedConjunctive: int) :
        count = len(self._where)
        if count > 0 :
            self._where[count-1].nestedConjunctive = nestedConjunctive

    def getLimit(self) -> tuple :
        return self._limit

    def hasLimit(self) -> bool :
        if self._limit is None : return False
        else : return True

    def setLimit(self, limit: Limit) :
        self._limit = limit
