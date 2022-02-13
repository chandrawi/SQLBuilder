from ...Structure import Column
from ...Builder import GroupByBuilder
from typing import Mapping

class GroupBy :

    def groupBy(self, columns) -> tuple :
        if (isinstance(columns, Mapping) and len(columns) == 1) or isinstance(columns, str) :
            columnObjects = (Column.create(columns),)
        else :
            columnObjects = Column.createMulti(columns)
        for column in columnObjects :
            if isinstance(self.builder, GroupByBuilder) :
                self.builder.addGroup(column)
            else :
                raise Exception('Builder object does not support GROUP BY query')
        return self
