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

    CONJUNCTIVE_NONE = 0
    CONJUNCTIVE_AND = 1
    CONJUNCTIVE_OR = 2
    CONJUNCTIVE_NOT_AND = 3
    CONJUNCTIVE_NOT_OR = 4

    def __init__(self, column, operator: int, value, conjunctive: int, level: int) :
        self.__column = column
        if operator > 0 and operator <= 14 :
            self.__operator = operator
        else :
            self.__operator = self.OPERATOR_DEFAULT
        self.__value = value
        if conjunctive > 0 and conjunctive <= 4 :
            self.__conjunctive = conjunctive
        else :
            self.__conjunctive = self.CONJUNCTIVE_NONE
        self.__level = level

    def column(self) :
        return self.__column

    def operator(self) -> int :
        return self.__operator

    def value(self) :
        return self.__value

    def conjunctive(self) -> int :
        return self.__conjunctive

    def level(self, input: int = -1) -> int :
        if input != -1 : self.__level = input
        return self.__level
