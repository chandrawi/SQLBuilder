class Table :

    def __init__(self, name: str, alias: str = '') :
        self.__name = name
        self.__alias = alias

    def name(self) -> str :
        return self.__name

    def alias(self) -> str :
        return self.__alias

class Column :

    def __init__(self, table: str, name: str, function: str = '', alias: str = '') :
        self.__table = table
        self.__name = name
        self.__function = function
        self.__alias = alias

    def table(self) -> str :
        return self.__table

    def name(self) -> str :
        return self.__name

    def function(self) -> str :
        return self.__function

    def alias(self) -> str :
        return self.__alias

class Value :

    def __init__(self, table: str, columns: tuple, values: tuple) :
        self.__table = table
        lenCol = len(columns)
        lenVal = len(values)
        lenMin = lenCol
        if lenCol > lenVal : lenMin = lenVal
        self.__columns = ()
        self.__values = values[:lenMin]
        for i in range(lenMin) :
            self.__columns += (str(columns[i]),)

    def table(self) -> str :
        return self.__table

    def columns(self) -> tuple :
        return self.__columns

    def values(self) -> tuple :
        return self.__values

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
        self.__column = column
        if operator > 0 and operator <= 14 :
            self.__operator = operator
        else :
            self.__operator = self.OPERATOR_DEFAULT
        self.__value = value
        if conjunctive >= 6 and conjunctive <= 9 :
            self.__conjunctive = conjunctive
        else :
            self.__conjunctive = self.CONJUNCTIVE_NONE
        self.__nestedConjunctive = nestedConjunctive

    def column(self) :
        return self.__column

    def operator(self) -> int :
        return self.__operator

    def value(self) :
        return self.__value

    def conjunctive(self) -> int :
        return self.__conjunctive

    def nestedConjunctive(self, input: int = -1) -> int :
        if input != -1 : self.__nestedConjunctive = input
        return self.__nestedConjunctive

class Order :

    ORDER_NONE = 0
    ORDER_ASC = 1
    ORDER_DESC = 2

    def __init__(self, column: Column, orderType: int) :
        self.__column = column
        self.__orderType = orderType

    def column(self) -> Column :
        return self.__column

    def orderType(self) -> int :
        return self.__orderType

class Limit :

    NOT_SET = -1

    def __init__(self, limit: int, offset: int) :
        self.__limit = limit
        self.__offset = offset

    def limit(self) -> int :
        return self.__limit

    def offset(self) -> int :
        return self.__offset
