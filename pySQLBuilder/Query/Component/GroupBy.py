from ...Structure import Column
from typing import Mapping

class GroupBy :

    def groupBy(self, columns) -> tuple :
        if (isinstance(columns, Mapping) and len(columns) == 1) or isinstance(columns, str) :
            columnObjects = (Column.create(columns),)
        else :
            columnObjects = Column.createMulti(columns)
        for column in columnObjects :
            self.builder.addGroup(column)
        return self
