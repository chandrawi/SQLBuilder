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
        if lenCol < lenVal :
            self.columns = columns
            self.values = values[:lenCol]
        else :
            self.columns = columns[:lenVal]
            self.values = values

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

    def __init__(self, column, operator: int, values: int, conjunctive: int, nestedConjunctive: int) :
        self.column = column
        if operator > 0 and operator <= 14 :
            self.operator = operator
        else :
            self.operator = self.OPERATOR_DEFAULT
        self.values = values
        if conjunctive >= 6 and conjunctive <= 9 :
            self.conjunctive = conjunctive
        else :
            self.conjunctive = self.CONJUNCTIVE_NONE
        self.nestedConjunctive = nestedConjunctive
