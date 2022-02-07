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
        self.query.endClause(self.builder, self.query.WHERE)
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
        self.query.endClause(self.builder, self.query.HAVING)
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

    def groupBy(self, columns) :
        if isinstance(columns, dict) :
            keys = tuple(columns.keys())
            for i in range(len(keys)) :
                columnObject = self.query.createColumn({keys[i]: columns[keys[i]]})
                self.builder.addGroup(columnObject)
        elif isinstance(columns, list) or isinstance(columns, tuple) :
            for col in columns :
                columnObject = self.query.createColumn(col)
                self.builder.addGroup(columnObject)
        else :
            columnObject = self.query.createColumn(columns)
            self.builder.addGroup(columnObject)
        return self

    def orderBy(self, columns, orderType) :
        if isinstance(columns, dict) :
            keys = tuple(columns.keys())
            for i in range(len(keys)) :
                orderObject = self.query.createOrder({keys[i]: columns[keys[i]]}, orderType)
                self.builder.addOrder(orderObject)
        elif isinstance(columns, list) or isinstance(columns, tuple) :
            for col in columns :
                orderObject = self.query.createOrder(col, orderType)
                self.builder.addOrder(orderObject)
        else :
            orderObject = self.query.createOrder(columns, orderType)
            self.builder.addOrder(orderObject)
        return self

    def orderAsc(self, column) :
        orderObject = self.query.orderAsc(column)
        self.builder.addOrder(orderObject)
        return self

    def orderDesc(self, column) :
        orderObject = self.query.orderDesc(column)
        self.builder.addOrder(orderObject)
        return self

    def limit(self, limit, offset = None) :
        limitObject = self.query.createLimit(limit, offset)
        self.builder.setLimit(limitObject)
        return self

    def offset(self, offset) :
        limitObject = self.query.offset(offset)
        self.builder.setLimit(limitObject)
        return self
