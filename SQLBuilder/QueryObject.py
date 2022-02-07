class QueryObject :

    def __init__(self) :
        self.__parts = []
        self.__params = []
        self.__bindMarkNum = '?'
        self.__bindMarkAssoc = ':'
        self.__stringQuote = '\''

    def parts(self) :
        return self.__parts

    def params(self) :
        return self.__params

    def add(self, queryPart, paramFlag: bool = False) :
        if paramFlag :
            self.__params.append(queryPart)
        else :
            self.__parts.append(queryPart)

    def bindMarkNum(self) :
        return self.__bindMarkNum

    def bindMarkAssoc(self) :
        return self.__bindMarkAssoc

    def stringQuote(self) :
        return self.__stringQuote

    def setBindMark(self, bindMarkNum: str, bindMarkAssoc: str, stringQuote: str) :
        self.__bindMarkNum = bindMarkNum
        self.__bindMarkAssoc = bindMarkAssoc
        self.__stringQuote = stringQuote
