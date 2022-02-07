from .BaseQuery import BaseQuery
from .QueryManipulation import QueryManipulation
from ..Builder import BaseBuilder, SelectBuilder

class Select(BaseQuery) :

    query = QueryManipulation()

    def __init__(self, options: tuple = (), statement = None) :
        self.builder = SelectBuilder()
        self.builder.builderType(BaseBuilder.SELECT)
        self._options = options
        self._statement = statement

    def select(self, table) :
        if table :
            tableObject = self.query.createTable(table)
            self.builder.setTable(tableObject)
        else :
            raise Exception("Table name is not defined")
        return self

    def column(self, column) :
        columnObject = self.query.createColumn(column)
        self.builder.addColumn(columnObject)
        return self

    def columns(self, columns) :
        if isinstance(columns, dict) :
            keys = tuple(columns.keys())
            for i in range(len(keys)) :
                columnObject = self.query.createColumn({keys[i]: columns[keys[i]]})
                self.builder.addColumn(columnObject)
        elif isinstance(columns, list) or isinstance(columns, tuple) :
            for col in columns :
                columnObject = self.query.createColumn(col)
                self.builder.addColumn(columnObject)
        return self
