import BreakObject

import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)

from SQLBuilder import QueryBuilder

builder = QueryBuilder() \
    .delete('data_table') \
    .where('col1', '>=', 0) \
    .orWhere('col3', 'BETWEEN', ['minValue', 'maxValue']) \
    .limit(100)
builderObject = builder.getBuilder()

BreakObject.printDeleteBuilder(builderObject)
