import BreakObject

import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)

import pySQLBuilder as sql

sql.translator = sql.TRANSLATOR_GENERIC
sql.bindingOption = sql.PARAM_NUM

builder = sql \
    .select('baseTable') \
    .columns(['col1', 'col2', 'MAX(col3)']) \
    .leftJoin('joinTable') \
    .on('baseCol1', 'joinCol1') \
    .on('baseCol2', 'joinCol2') \
    .columns(['col1', 'col2'])
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
