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
