import BreakObject

import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)

import pySQLBuilder

builder = pySQLBuilder \
    .update('data_table') \
    .values({'col1': 'val1.1', 'col2': 'val2.1'}) \
    .where('col1', '>=', 0) \
    .orWhere('col3', 'BETWEEN', ['minValue', 'maxValue']) \
    .limit(100)
builderObject = builder.getBuilder()
builder.translate()
queryObject = builder.getQueryObject()

print("--------------\nBUILDER OBJECT\n--------------")
BreakObject.printUpdateBuilder(builderObject)

print("------------\nQUERY OBJECT\n------------")
BreakObject.printQuery(queryObject)

print("-----\nQUERY\n-----")
print(builder.query())

print("------\nPARAMS\n------")
print(builder.params())
