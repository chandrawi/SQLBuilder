from .Column import Column

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
