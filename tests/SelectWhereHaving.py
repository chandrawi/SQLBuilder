import BreakObject

import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)

import pySQLBuilder as sql

sql.translator = sql.TRANSLATOR_GENERIC
sql.bindingOption = sql.PARAM_NUM

builder = sql \
    .select('table') \
    .where('col1', '>=', 0) \
        .beginAndWhere() \
        .where('col3', 'IN', ['value0', 'value1', 'value2']) \
        .orWhere('col4', 'BETWEEN', ['minValue', 'maxValue']) \
        .endWhere() \
    .groupBy('col1') \
    .having('col5', '=', 'havingValue')
builderObject = builder.getBuilder()
builder.translate()
queryObject = builder.getQueryObject()

print("--------------\nBUILDER OBJECT\n--------------")
BreakObject.printSelectBuilder(builderObject)

print("------------\nQUERY OBJECT\n------------")
BreakObject.printQuery(queryObject)

print("-----\nQUERY\n-----")
print(builder.query())

print("------\nPARAMS\n------")
print(builder.params())
