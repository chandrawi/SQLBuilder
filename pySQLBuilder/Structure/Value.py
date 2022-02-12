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
