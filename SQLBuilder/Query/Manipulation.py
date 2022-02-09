from ..Structure import Table, Column, Value, Clause, Order, Limit
from typing import Iterable, Mapping

class Manipulation :

### TABLE, COLUMN, VALUES QUERY ###

    table = ''

    def createTable(self, table) -> Table :
        name = ''
        alias = ''
        if isinstance(table, str) :
            self.table = table
            name = table
            return Table(table)
        elif isinstance(table, Mapping) :
            if len(table) == 1 :
                alias = tuple(table.keys())[0]
                name = table[alias]
                self.table = str(alias)
        return Table(str(name), str(alias))

    def createColumn(self, column) -> Column :
        table = ''
        name = ''
        function = ''
        alias = ''
        if isinstance(column, str) :
            (table, name, function) = self.parseColumnStr(column)
        elif isinstance(column, Mapping) :
            (table, name, function, alias) = self.parseColumnMap(column)
        return Column(table, name, function, alias)

    def createColumns(self, columns) -> tuple :
        columnObjects = ()
        if isinstance(columns, Mapping) :
            keys = tuple(columns.keys())
            for i in range(len(keys)) :
                columnObjects += (self.createColumn({keys[i]: columns[keys[i]]}),)
        elif isinstance(columns, Iterable) :
            for col in columns :
                columnObjects += (self.createColumn(col),)
        return columnObjects

    def parseColumnStr(self, column: str) -> tuple :
        function = ''
        pos1 = column.find('(')
        pos2 = column.rfind(')')
        if pos1 > 0 and pos2 > 1 :
            function = column[0:pos1]
            column = column[pos1+1:pos2]
        table = self.table
        name = column
        split = column.split('.')
        if len(split) == 2 :
            table = split[0]
            name = split[1]
        return (table, name, function)

    def parseColumnMap(self, column: Mapping) -> tuple :
        alias = ''
        keys = tuple(column.keys())
        if len(column) == 1 :
            alias = str(keys[0])
            column = column[keys[0]]
        table = self.table
        name = ''
        function = ''
        if isinstance(column, str) :
            (table, name, function) = self.parseColumnStr(column)
        return (table, name, function, alias)

    def createValue(self, inputValue) -> Value :
        columns = ()
        values = ()
        if isinstance(inputValue, Mapping) :
            columns = tuple(inputValue.keys())
            values = tuple(inputValue.values())
        elif isinstance(inputValue, Iterable) :
            (columns, values) = self.parseValuePair(inputValue)
        return Value(self.table, columns, values)

    def createMultiValue(self, multiValues) -> tuple :
        valuesObjects = ()
        if isinstance(multiValues, Iterable) :
            for val in multiValues :
                valuesObjects += (self.createValue(val),)
        return valuesObjects

    def parseValuePair(self, pairs: Iterable) -> tuple :
        if isinstance(pairs[0], str) and len(pairs) == 2 :
            return ((pairs[0],), (pairs[1],))
        columns = ()
        values = ()
        for pair in pairs :
            if isinstance(pair, Mapping) :
                if len(pair) :
                    key = tuple(pair.keys())[0]
                    columns += (key,)
                    values += (pair[key],)
            elif isinstance(pair, Iterable) :
                if len(pair) == 2 :
                    columns += (pair[0],)
                    values += (pair[1],)
        return (columns, values)

### WHERE AND HAVING CLAUSE QUERY ###

    CLAUSE_DEFAULT = 0
    CLAUSE_WHERE = 1
    CLAUSE_HAVING = 2

    clauseType = CLAUSE_DEFAULT
    nestedConjunctive = Clause.CONJUNCTIVE_NONE
    nestedLevel = 0

    def createClause(self, clauseType: int, column, operator, values, conjunctive: int) -> Clause :
        columnObject = self.createColumn(column)
        validOperator = self.getOperator(operator)
        validValues = self.getValues(values, operator)
        conjunctive = self.getConjunctive(clauseType, conjunctive)
        nestedLevel = self.nestedLevel
        self.clauseType = clauseType
        self.nestedLevel = 0
        return Clause(columnObject, validOperator, validValues, conjunctive, nestedLevel)

    def getOperator(self, operator) -> int :
        if isinstance(operator, int) :
            validOperator = operator
        else :
            if operator == '=' or operator == '==' :
                validOperator = Clause.OPERATOR_EQUAL
            elif operator == '!=' or operator == '<>' :
                validOperator = Clause.OPERATOR_NOT_EQUAL
            elif operator == '>' :
                validOperator = Clause.OPERATOR_GREATER
            elif operator == '>=' :
                validOperator = Clause.OPERATOR_GREATER_EQUAL
            elif operator == '<' :
                validOperator = Clause.OPERATOR_LESS
            elif operator == '<=' :
                validOperator = Clause.OPERATOR_LESS_EQUAL
            elif operator == 'BETWEEN' :
                validOperator = Clause.OPERATOR_BETWEEN
            elif operator == 'NOT BETWEEN' :
                validOperator = Clause.OPERATOR_NOT_BETWEEN
            elif operator == 'LIKE' :
                validOperator = Clause.OPERATOR_LIKE
            elif operator == 'NOT LIKE' :
                validOperator = Clause.OPERATOR_NOT_LIKE
            elif operator == 'IN' :
                validOperator = Clause.OPERATOR_IN
            elif operator == 'NOT IN' :
                validOperator = Clause.OPERATOR_NOT_IN
            elif operator == 'NULL' or operator == 'IS NULL' :
                validOperator = Clause.OPERATOR_NULL
            elif operator == 'NOT NULL' or operator == 'IS NOT NULL' :
                validOperator = Clause.OPERATOR_NOT_NULL
            else :
                validOperator = Clause.OPERATOR_DEFAULT
        return validOperator
            
    def getValues(self, values, operator) :
        valid = True
        if operator == Clause.OPERATOR_BETWEEN or operator == Clause.OPERATOR_NOT_BETWEEN :
            if isinstance(values, Iterable) :
                valid = len(values) == 2
        if operator == Clause.OPERATOR_IN or operator == Clause.OPERATOR_NOT_IN :
            valid = isinstance(values, Iterable)
        if valid :
            return values
        else :
            raise Exception('Invalid input values for Where or Having clause')

    def getConjunctive(self, clauseType: int, conjunctive: int) -> int :
        if clauseType == self.clauseType :
            if conjunctive == Clause.CONJUNCTIVE_NONE :
                if self.nestedConjunctive == Clause.CONJUNCTIVE_NONE : return Clause.CONJUNCTIVE_AND
                else : return self.nestedConjunctive
            else :
                return conjunctive
        else :
            return Clause.CONJUNCTIVE_NONE

    def beginClause(self) :
        self.nestedConjunctive = Clause.CONJUNCTIVE_NONE
        self.nestedLevel -= 1

    def beginAndClause(self) :
        self.nestedConjunctive = Clause.CONJUNCTIVE_AND
        self.nestedLevel -= 1

    def beginOrClause(self) :
        self.nestedConjunctive = Clause.CONJUNCTIVE_OR
        self.nestedLevel -= 1

    def beginNotAndClause(self) :
        self.nestedConjunctive = Clause.CONJUNCTIVE_NOT_AND
        self.nestedLevel -= 1

    def beginNotOrClause(self) :
        self.nestedConjunctive = Clause.CONJUNCTIVE_NOT_OR
        self.nestedLevel -= 1

    def endClause(self, clauseType: int, builder) :
        if clauseType == self.CLAUSE_WHERE :
            lastNested = builder.lastWhere().nestedLevel()
            builder.editWhereNested(lastNested + 1)
        elif clauseType == self.CLAUSE_HAVING :
            lastNested = builder.lastHaving().nestedLevel()
            builder.editHavingNested(lastNested + 1)

    def andClause(self, clauseType: int, column, operator: str, value = None) -> Clause :
        return self.createClause(clauseType, column, operator, value, Clause.CONJUNCTIVE_AND)

    def orClause(self, clauseType: int, column, operator: str, value = None) -> Clause :
        return self.createClause(clauseType, column, operator, value, Clause.CONJUNCTIVE_OR)

    def notAndClause(self, clauseType: int, column, operator: str, value = None) -> Clause :
        return self.createClause(clauseType, column, operator, value, Clause.CONJUNCTIVE_NOT_AND)

    def notOrClause(self, clauseType: int, column, operator: str, value = None) -> Clause :
        return self.createClause(clauseType, column, operator, value, Clause.CONJUNCTIVE_NOT_OR)

### GROUP BY QUERY ###

    def createGroups(self, columns) -> tuple :
        if (isinstance(columns, Mapping) and len(columns) == 1) or isinstance(columns, str) :
            return (self.createColumn(columns),)
        else :
            return self.createColumns(columns)

### ORDER BY QUERY ###

    def createOrders(self, columns, orderType) -> tuple :
        if (isinstance(columns, Mapping) and len(columns) == 1) or isinstance(columns, str) :
            columnObjects = (self.createColumn(columns),)
        else :
            columnObjects = self.createColumns(columns)
        validType = self.getOrderType(orderType)
        orderObjects = ()
        for col in columnObjects :
            orderObjects += (Order(col, validType),)
        print(orderObjects)
        return orderObjects

    def getOrderType(self, orderType) -> int :
        if isinstance(orderType, int) :
            validType = orderType
        else :
            if orderType == 'ASCENDING' or orderType == 'ASC' or orderType == 'ascending' or orderType == 'asc' :
                validType = Order.ORDER_ASC
            elif orderType == 'DESCENDING' or orderType == 'DESC' or orderType == 'descending' or orderType == 'desc' :
                validType = Order.ORDER_DESC
            else :
                validType = Order.ORDER_NONE
        return validType

    def orderAsc(self, column) -> Order :
        return self.createOrders(column, Order.ORDER_ASC)

    def orderDesc(self, column) -> Order :
        return self.createOrders(column, Order.ORDER_DESC)

### LIMIT AND OFFSET QUERY ###

    def createLimit(self, limit, offset) -> Limit :
        validLimit = Limit.NOT_SET
        validOffset = Limit.NOT_SET
        if isinstance(limit, int) :
            if limit > 0: validLimit = limit
        if isinstance(offset, int) :
            if offset > 0: validOffset = offset
        return Limit(validLimit, validOffset)

    def offset(self, offset) -> Limit :
        return self.createLimit(Limit.NOT_SET, offset)
