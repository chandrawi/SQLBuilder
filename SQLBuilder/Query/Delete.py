from .BaseQuery import BaseQuery
from .QueryManipulation import QueryManipulation
from ..Builder import BaseBuilder, DeleteBuilder

class Delete(BaseQuery) :

    query = QueryManipulation()

    def __init__(self, options: tuple = (), statement = None) :
        self.builder = DeleteBuilder()
        self.builder.builderType(BaseBuilder.DELETE)
        self._options = options
        self._statement = statement

    def delete(self, table) :
        if table :
            tableObject = self.query.createTable(table)
            self.builder.setTable(tableObject)
        else :
            raise Exception("Table name is not defined")
        return self
