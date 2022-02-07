from ..QueryObject import QueryObject
from ..Builder import BaseBuilder
from ..Structure import Table, Column, Value, Clause, Order, Limit

class BaseTranslator :

    quote = "`"
    equal = "="
    open_bracket = "("
    close_bracket = ")"
    dot = "."
    comma = ","
    end_query = ";"

    def firstKeyword(self, query: QueryObject, builderType: int) :
        if builderType == BaseBuilder.SELECT :
            query.add('SELECT ')
        elif builderType == BaseBuilder.INSERT :
            query.add('INSERT ')
        elif builderType == BaseBuilder.UPDATE :
            query.add('UPDATE ')
        elif builderType == BaseBuilder.DELETE :
            query.add('DELETE ')
