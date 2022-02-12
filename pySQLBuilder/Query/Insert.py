from .BaseQuery import BaseQuery
from .Manipulation import Manipulation
from ..Builder import BaseBuilder, InsertBuilder
from ..Structure import Table, Value

class Insert(BaseQuery) :

    def __init__(self, translator: int, bindingOption: int) :
        BaseQuery.__init__(self)
        self.builder = InsertBuilder()
        self.builder.builderType(BaseBuilder.INSERT)
        self.translator = translator
        self.bindingOption = bindingOption
        self.man = Manipulation()

    def insert(self, table) :
        if table :
            tableObject = Table.create(table)
            self.builder.setTable(tableObject)
        else :
            raise Exception("Table name is not defined")
        return self

    def values(self, values) :
        valueObject = Value.create(values)
        self.builder.addValue(valueObject)
        return self

    def multiValues(self, multiValues) :
        valuesObjects = Value.createMulti(multiValues)
        for val in valuesObjects :
            self.builder.addValue(val)
        return self

    def limit(self, limit, offset = None) :
        limitObject = self.man.createLimit(limit, offset)
        self.builder.setLimit(limitObject)
        return self

    def offset(self, offset) :
        limitObject = self.man.offset(offset)
        self.builder.setLimit(limitObject)
        return self
