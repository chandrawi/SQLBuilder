class Table :

    def __init__(self, name: str, alias: str = '') :
        self.__name = name
        self.__alias = alias

    def name(self) -> str :
        return self.__name

    def alias(self) -> str :
        return self.__alias
