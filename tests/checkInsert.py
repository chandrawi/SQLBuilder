import BreakObject

import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)

from SQLBuilder import QueryBuilder

builder = QueryBuilder() \
    .insert('data_table') \
    .multiValues(({'col1': 'val1.1', 'col2': 'val2.1'}, {'col1': 'val1.2', 'col2': 'val2.2'})) \
    .limit(2)
builderObject = builder.getBuilder()

BreakObject.printInsertBuilder(builderObject)
