import BreakObject

import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)

from SQLBuilder import QueryBuilder

builder = QueryBuilder() \
    .update('data_table') \
    .values({'col1': 'val1.1', 'col2': 'val2.1'}) \
    .where('col1', '>=', 0) \
    .orWhere('col3', 'BETWEEN', ['minValue', 'maxValue']) \
    .limit(100)
builderObject = builder.getBuilder()

BreakObject.printUpdateBuilder(builderObject)
