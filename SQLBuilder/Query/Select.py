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

    def beginHaving(self) :
        self.query.beginClause()
        return self

    def beginAndHaving(self) :
        self.query.beginAndClause()
        return self

    def beginOrHaving(self) :
        self.query.beginOrClause()
        return self

    def beginNotAndHaving(self) :
        self.query.beginNotAndClause()
        return self

    def beginNotOrHaving(self) :
        self.query.beginNotOrClause()
        return self

    def endHaving(self) :
        self.query.endClause(self.builder)
        return self

    def having(self, column, operator: str, value = None) :
        clauseObject = self.query.andClause(column, operator, value)
        self.builder.addHaving(clauseObject)
        return self

    def andHaving(self, column, operator: str, value = None) :
        clauseObject = self.query.andClause(column, operator, value)
        self.builder.addHaving(clauseObject)
        return self

    def orHaving(self, column, operator: str, value = None) :
        clauseObject = self.query.orClause(column, operator, value)
        self.builder.addHaving(clauseObject)
        return self

    def notAndHaving(self, column, operator: str, value = None) :
        clauseObject = self.query.notAndClause(column, operator, value)
        self.builder.addHaving(clauseObject)
        return self

    def notOrHaving(self, column, operator: str, value = None) :
        clauseObject = self.query.notOrClause(column, operator, value)
        self.builder.addHaving(clauseObject)
        return self
