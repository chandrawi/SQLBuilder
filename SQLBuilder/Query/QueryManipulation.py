from ..Structure import Table, Column, Value

class QueryManipulation :

### TABLE, COLUMN, VALUES QUERY ###

    _table = ''

    def createTable(self, table) -> Table :
        name = ''
        alias = ''
        if isinstance(table, str) :
            self._table = table
            name = table
            return Table(table)
        elif isinstance(table, dict) :
            if len(table) == 1 :
                alias = tuple(table.keys())[0]
                name = table[alias]
                self._table = str(alias)
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
        table = self._table
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
        table = self._table
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
        return Value(self._table, columns, values)

    def parseValuePair(self, pairs) :
        columns = []
        values = []
        for pair in pairs :
            if isinstance(pair, tuple) or isinstance(pair, list) :
                if len(pair) == 2 :
                    columns.append(pair[0])
                    values.append(pair[1])
        return (tuple(columns), tuple(values))
