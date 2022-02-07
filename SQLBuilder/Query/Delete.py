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

    def beginWhere(self) :
        self.query.beginClause()
        return self

    def beginAndWhere(self) :
        self.query.beginAndClause()
        return self

    def beginOrWhere(self) :
        self.query.beginOrClause()
        return self

    def beginNotAndWhere(self) :
        self.query.beginNotAndClause()
        return self

    def beginNotOrWhere(self) :
        self.query.beginNotOrClause()
        return self

    def endWhere(self) :
        self.query.endClause(self.builder)
        return self

    def where(self, column, operator: str, value = None) :
        clauseObject = self.query.andClause(column, operator, value)
        self.builder.addWhere(clauseObject)
        return self

    def andWhere(self, column, operator: str, value = None) :
        clauseObject = self.query.andClause(column, operator, value)
        self.builder.addWhere(clauseObject)
        return self

    def orWhere(self, column, operator: str, value = None) :
        clauseObject = self.query.orClause(column, operator, value)
        self.builder.addWhere(clauseObject)
        return self

    def notAndWhere(self, column, operator: str, value = None) :
        clauseObject = self.query.notAndClause(column, operator, value)
        self.builder.addWhere(clauseObject)
        return self

    def notOrWhere(self, column, operator: str, value = None) :
        clauseObject = self.query.notOrClause(column, operator, value)
        self.builder.addWhere(clauseObject)
        return self
