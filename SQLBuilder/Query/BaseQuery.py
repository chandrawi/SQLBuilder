from ..QueryObject import QueryObject
from ..Structure import Table, Column, Value
from ..Builder import BaseBuilder, SelectBuilder, InsertBuilder, UpdateBuilder, DeleteBuilder

class BaseQuery :

    query = QueryObject()
    builder = BaseBuilder()

    _options = ()
    _statement = None

    def queryObject(self) :
        return self.query

    def getBuilder(self) :
        return self.builder
