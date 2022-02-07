from ..Structure import Table, Column, Value, Clause, Order, Limit

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
        elif isinstance(table, dict) :
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
        elif isinstance(column, dict) :
            (table, name, function, alias) = self.parseColumnDict(column)
        return Column(table, name, function, alias)

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

    def parseColumnDict(self, column: dict) -> tuple :
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
        if isinstance(inputValue, dict) :
            columns = tuple(inputValue.keys())
            values = tuple(inputValue.values())
        elif isinstance(inputValue, tuple) or isinstance(inputValue, list) :
            (columns, values) = self.parseValuePair(inputValue)
        return Value(self.table, columns, values)

    def parseValuePair(self, pairs) :
        columns = []
        values = []
        for pair in pairs :
            if isinstance(pair, tuple) or isinstance(pair, list) :
                if len(pair) == 2 :
                    columns.append(pair[0])
                    values.append(pair[1])
        return (tuple(columns), tuple(values))

### WHERE AND HAVING CLAUSE QUERY ###

    WHERE = 1
    HAVING = 2

    nestedConjunctive = Clause.CONJUNCTIVE_NONE
    firstClause = True

    def createClause(self, column, operator, values, conjunctive: int = -1, nestedConjunctive: int = -1) -> Clause :
        self.firstClause = False
        columnObject = self.createColumn(column)
        validOperator = self.getOperator(operator)
        validValues = self.getValues(values, operator)
        return Clause(columnObject, validOperator, validValues, conjunctive, nestedConjunctive)

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
            if isinstance(values, tuple) or isinstance(values, list) :
                valid = len(values) == 2
        if operator == Clause.OPERATOR_IN or operator == Clause.OPERATOR_NOT_IN :
            valid = isinstance(values, tuple) or isinstance(values, list)
        if valid :
            return values
        else :
            raise Exception('Invalid input values for Where or Having clause')

    def getConjunctive(self, conjunctive: int) :
        if not self.firstClause and self.nestedConjunctive >= Clause.CONJUNCTIVE_NONE :
            return conjunctive
        else :
            return Clause.CONJUNCTIVE_NONE

    def beginClause(self) :
        if self.nestedConjunctive <= Clause.CONJUNCTIVE_BEGIN :
            self.nestedConjunctive -= 1
        else :
            self.nestedConjunctive = Clause.CONJUNCTIVE_BEGIN

    def beginAndClause(self) :
        self.nestedConjunctive = Clause.CONJUNCTIVE_AND_BEGIN

    def beginOrClause(self) :
        self.nestedConjunctive = Clause.CONJUNCTIVE_OR_BEGIN

    def beginNotAndClause(self) :
        self.nestedConjunctive = Clause.CONJUNCTIVE_NOT_AND_BEGIN

    def beginNotOrClause(self) :
        self.nestedConjunctive = Clause.CONJUNCTIVE_NOT_OR_BEGIN

    def endClause(self, builder, clauseType: int) :
        lastNested = Clause.CONJUNCTIVE_NONE
        if clauseType == self.WHERE :
            lastNested = builder.lastWhere().nestedConjunctive
        elif clauseType == self.HAVING :
            lastNested = builder.lastHaving().nestedConjunctive
        newNested = Clause.CONJUNCTIVE_NONE
        if lastNested >= Clause.CONJUNCTIVE_END : newNested = lastNested + 1
        elif lastNested == Clause.CONJUNCTIVE_NONE : newNested = Clause.CONJUNCTIVE_END
        elif lastNested == Clause.CONJUNCTIVE_AND_BEGIN : newNested = Clause.CONJUNCTIVE_AND
        elif lastNested == Clause.CONJUNCTIVE_OR_BEGIN : newNested = Clause.CONJUNCTIVE_OR
        elif lastNested == Clause.CONJUNCTIVE_NOT_AND_BEGIN : newNested = Clause.CONJUNCTIVE_NOT_AND
        elif lastNested == Clause.CONJUNCTIVE_NOT_OR_BEGIN : newNested = Clause.CONJUNCTIVE_NOT_OR
        if clauseType == self.WHERE :
            builder.editWhereNested(newNested)
        elif clauseType == self.HAVING :
            builder.editHavingNested(newNested)

    def andClause(self, column, operator: str, value = None) -> Clause :
        conjunctive = self.getConjunctive(Clause.CONJUNCTIVE_AND)
        return self.createClause(column, operator, value, conjunctive)

    def orClause(self, column, operator: str, value = None) -> Clause :
        conjunctive = self.getConjunctive(Clause.CONJUNCTIVE_OR)
        return self.createClause(column, operator, value, conjunctive)

    def notAndClause(self, column, operator: str, value = None) -> Clause :
        conjunctive = self.getConjunctive(Clause.CONJUNCTIVE_NOT_AND)
        return self.createClause(column, operator, value, conjunctive)

    def notOrClause(self, column, operator: str, value = None) -> Clause :
        conjunctive = self.getConjunctive(Clause.CONJUNCTIVE_NOT_OR)
        return self.createClause(column, operator, value, conjunctive)

### ORDER BY QUERY ###

    def createOrder(self, column, orderType) -> Order :
        columnObject = self.createColumn(column)
        validType = self.getOrderType(orderType)
        return Order(columnObject, validType)

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
        return self.createOrder(column, Order.ORDER_ASC)

    def orderDesc(self, column) -> Order :
        return self.createOrder(column, Order.ORDER_DESC)

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
