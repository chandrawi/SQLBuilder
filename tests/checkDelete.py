import BreakObject

import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)

from SQLBuilder import QueryBuilder, QueryTranslator

builder = QueryBuilder() \
    .delete('data_table') \
    .where('col1', '>=', 0) \
    .orWhere('col3', 'BETWEEN', ['minValue', 'maxValue']) \
    .limit(100)
builderObject = builder.getBuilder()
builder.translate()
queryObject = builder.getQueryObject()

print("--------------\nBUILDER OBJECT\n--------------")
BreakObject.printDeleteBuilder(builderObject)

print("------------\nQUERY OBJECT\n------------")
BreakObject.printQuery(queryObject)

print("-----\nQUERY\n-----")
print(builder.query())

print("------\nPARAMS\n------")
print(builder.params())
