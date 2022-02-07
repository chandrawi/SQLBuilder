from .BaseTranslator import BaseTranslator
from ..QueryObject import QueryObject
from ..Builder import SelectBuilder, InsertBuilder, UpdateBuilder, DeleteBuilder

class GenericTranslator(BaseTranslator) :

    def __init__(self, query: QueryObject) :
        self.quote = ""
        self.equal = "="
        self.open_bracket = "("
        self.close_bracket = ")"
        self.dot = "."
        self.comma = ", "
        self.end_query = ""

    def translateSelect(self, query: QueryObject, builder: SelectBuilder) :
        self.firstKeyword(query, builder.builderType())
        self.columnList(query, builder.getColumns(), builder.countColumns())
        self.fromTable(query, builder.getTable())

    def translateInsert(self, query: QueryObject, builder: InsertBuilder) :
        self.firstKeyword(query, builder.builderType())
        self.intoTable(query, builder.getTable())
        self.columnListInsert(query, builder.getValues(), builder.countValues())
        self.valuesInsert(query, builder.getValues(), builder.countValues())

    def translateUpdate(self, query: QueryObject, builder: UpdateBuilder) :
        self.firstKeyword(query, builder.builderType())
        self.tableSet(query, builder.getTable())
        self.valuesUpdate(query, builder.getValues(), builder.countValues())

    def translateDelete(self, query: QueryObject, builder: DeleteBuilder) :
        self.firstKeyword(query, builder.builderType())
        self.fromTable(query, builder.getTable())
