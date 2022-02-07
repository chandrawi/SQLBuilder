class Table :

    def __init__(self, name: str, alias: str = '') :
        self.name = name
        self.alias = alias

class Column :

    def __init__(self, table: str, name: str, function: str = '', alias: str = '') :
        self.table = table
        self.name = name
        self.function = function
        self.alias = alias

class Value :

    def __init__(self, table: str, columns: tuple, values: tuple) :
        self.table = table
        lenCol = len(columns)
        lenVal = len(values)
        if lenCol < lenVal :
            self.columns = columns
            self.values = values[:lenCol]
        else :
            self.columns = columns[:lenVal]
            self.values = values
