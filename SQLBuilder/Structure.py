class Table :

    def __init__(self, name: str, alias: str = '') :
        self.name = name
        self.alias = alias

class Column :

    def __init__(self, table: str, name: str, function: str = '', alias: str = '') :
        self.table = table
        self.name = name
        self.function = function
        self.alias = alias

class Value :

    def __init__(self, table: str, columns: tuple, values: tuple) :
        self.table = table
        lenCol = len(columns)
        lenVal = len(values)
        lenMin = lenCol
        if lenCol > lenVal : lenMin = lenVal
        self.columns = ()
        self.values = values[:lenMin]
        for i in range(lenMin) :
            self.columns += (str(columns[i]),)

class Clause :

    OPERATOR_DEFAULT = 0
    OPERATOR_EQUAL = 1
    OPERATOR_NOT_EQUAL = 2
    OPERATOR_GREATER = 3
    OPERATOR_GREATER_EQUAL = 4
    OPERATOR_LESS = 5
    OPERATOR_LESS_EQUAL = 6
    OPERATOR_LIKE = 7
    OPERATOR_NOT_LIKE = 8
    OPERATOR_BETWEEN = 9
    OPERATOR_NOT_BETWEEN = 10
    OPERATOR_IN = 11
    OPERATOR_NOT_IN = 12
    OPERATOR_NULL = 13
    OPERATOR_NOT_NULL = 14

    CONJUNCTIVE_BEGIN = 1
    CONJUNCTIVE_AND_BEGIN = 2
    CONJUNCTIVE_OR_BEGIN = 3
    CONJUNCTIVE_NOT_AND_BEGIN = 4
    CONJUNCTIVE_NOT_OR_BEGIN = 5
    CONJUNCTIVE_AND = 6
    CONJUNCTIVE_OR = 7
    CONJUNCTIVE_NOT_AND = 8
    CONJUNCTIVE_NOT_OR = 9
    CONJUNCTIVE_NONE = 10
    CONJUNCTIVE_END = 11

    def __init__(self, column, operator: int, value, conjunctive: int, nestedConjunctive: int) :
        self.column = column
        if operator > 0 and operator <= 14 :
            self.operator = operator
        else :
            self.operator = self.OPERATOR_DEFAULT
        self.value = value
        if conjunctive >= 6 and conjunctive <= 9 :
            self.conjunctive = conjunctive
        else :
            self.conjunctive = self.CONJUNCTIVE_NONE
        self.nestedConjunctive = nestedConjunctive

class Order :

    ORDER_NONE = 0
    ORDER_ASC = 1
    ORDER_DESC = 2

    def __init__(self, column: Column, orderType: int) :
        self.column = column
        self.orderType = orderType

class Limit :

    NOT_SET = -1

    def __init__(self, limit: int, offset: int) :
        self.limit = limit
        self.offset = offset
