from .BaseQuery import BaseQuery
from .Component import LimitOffset
from ..Builder import BaseBuilder, InsertBuilder
from ..Structure import Table, Value

class Insert(BaseQuery, LimitOffset) :

    def __init__(self, translator: int, bindingOption: int) :
        BaseQuery.__init__(self)
        self.builder = InsertBuilder()
        self.builder.builderType(BaseBuilder.INSERT)
        self.translator = translator
        self.bindingOption = bindingOption
        LimitOffset.__init__(self)

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
