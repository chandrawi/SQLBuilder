from ...Structure import Join

class JoinBuilder :

    def __init__(self) :
        self.__join = ()

    def getJoin(self) -> tuple :
        return self.__join

    def lastJoin(self) -> Join :
        count = len(self.__join)
        if count > 0 :
            return self.__join[count-1]
        return None

    def countJoin(self) -> int :
        return len(self.__join)

    def addJoin(self, join: Join) :
        self.__join += (join,)
