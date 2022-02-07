class QueryObject :

    def __init__(self) :
        self.parts = ()
        self.params = ()

    def add(self, queryPart, paramFlag: bool = False) :
        if paramFlag :
            self.params += (queryPart,)
        else :
            self.parts += (queryPart,)
