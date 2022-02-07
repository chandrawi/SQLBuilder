from ..QueryObject import QueryObject
from ..Builder import BaseBuilder
from ..Structure import Table, Column, Value, Clause, Order, Limit

class BaseTranslator :

    quote = "`"
    equal = "="
    open_bracket = "("
    close_bracket = ")"
    dot = "."
    comma = ","
    end_query = ""

    def firstKeyword(self, query: QueryObject, builderType: int) :
        if builderType == BaseBuilder.SELECT :
            query.add('SELECT ')
        elif builderType == BaseBuilder.INSERT :
            query.add('INSERT ')
        elif builderType == BaseBuilder.UPDATE :
            query.add('UPDATE ')
        elif builderType == BaseBuilder.DELETE :
            query.add('DELETE')

    def fromTable(self, query: QueryObject, table: Table) :
        name = table.name()
        alias = table.alias()
        query.add(' FROM ' + self.quote)
        query.add(name)
        query.add(self.quote)
        if alias :
            query.add(' AS ' + self.quote + alias + self.quote)

    def intoTable(self, query: QueryObject, table: Table) :
        name = table.name()
        query.add('INTO ' + self.quote)
        query.add(name)
        query.add(self.quote)

    def tableSet(self, query: QueryObject, table: Table) :
        name = table.name()
        query.add(self.quote)
        query.add(name)
        query.add(self.quote)

    def columnList(self, query: QueryObject, columns: tuple, count: int) :
        if count == 0 :
            query.add('*')
            return
        for column in columns :
            if isinstance(column, Column) :
                name = column.name()
                alias = column.alias()
                function = column.function()
                if function :
                    query.add(function + self.open_bracket)
                query.add(self.quote)
                query.add(name)
                query.add(self.quote)
                if function :
                    query.add(self.close_bracket)
                if alias :
                    query.add(' AS ' + self.quote + alias + self.quote)
                count -= 1
                if count > 0 : query.add(self.comma)

    def columnListInsert(self, query: QueryObject, values: tuple, count: int) :
        if count == 0 :
            query.add(' ' + self.open_bracket)
            query.add(self.close_bracket)
            return
        value = values[0]
        if isinstance(value, Value) :
            columns = value.columns()
            count = len(columns)
            query.add(' ' + self.open_bracket)
            for column in columns : 
                query.add(self.quote)
                query.add(column)
                query.add(self.quote)
                count -= 1
                if count > 0 : query.add(self.comma)
            query.add(self.close_bracket)

    def valuesInsert(self, query: QueryObject, values: tuple, count: int) :
        query.add(' VALUES ')
        if count == 0 :
            query.add(self.open_bracket)
            query.add(self.close_bracket)
            return
        for value in values :
            if isinstance(value, Value) :
                vals = value.values()
                countVals = len(vals)
                query.add(self.open_bracket)
                for val in vals :
                    query.add(val, True)
                    countVals -= 1
                    if countVals > 0 : query.add(self.comma)
                query.add(self.close_bracket)
            count -= 1
            if count > 0 : query.add(self.comma)

    def valuesUpdate(self, query:QueryObject, values: tuple, count: int) :
        query.add(' SET ')
        for value in values :
            if isinstance(value, Value) :
                columns = value.columns()
                vals = value.values()
                countVals = len(vals)
                for i, val in enumerate(vals) :
                    query.add(self.quote)
                    query.add(columns[i])
                    query.add(self.quote + self.equal)
                    query.add(val, True)
                    countVals -= 1
                    if countVals > 0 : query.add(self.comma)
            count -= 1
            if count > 1 : query.add(self.comma)
