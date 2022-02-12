class Limit :

    NOT_SET = -1

    def __init__(self, limit: int, offset: int) :
        self.__limit = limit
        self.__offset = offset

    def limit(self) -> int :
        return self.__limit

    def offset(self) -> int :
        return self.__offset
