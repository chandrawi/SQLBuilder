from .BaseQuery import BaseQuery
from .QueryManipulation import QueryManipulation
from ..Builder import BaseBuilder, UpdateBuilder

class Update(BaseQuery) :

    query = QueryManipulation()

    def __init__(self, options: tuple = (), statement = None) :
        self.builder = UpdateBuilder()
        self.builder.builderType(BaseBuilder.UPDATE)
        self._options = options
        self._statement = statement

    def update(self, table) :
        if table :
            tableObject = self.query.createTable(table)
            self.builder.setTable(tableObject)
        else :
            raise Exception("Table name is not defined")
        return self

    def values(self, values) :
        valueObject = self.query.createValue(values)
        self.builder.addValue(valueObject)
        return self
