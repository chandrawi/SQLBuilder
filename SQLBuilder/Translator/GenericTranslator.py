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

    def translateInsert(self, query: QueryObject, builder: InsertBuilder) :
        self.firstKeyword(query, builder.builderType())

    def translateUpdate(self, query: QueryObject, builder: UpdateBuilder) :
        self.firstKeyword(query, builder.builderType())

    def translateDelete(self, query: QueryObject, builder: DeleteBuilder) :
        self.firstKeyword(query, builder.builderType())
