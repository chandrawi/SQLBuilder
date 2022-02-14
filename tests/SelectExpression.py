import BreakObject

import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)

import pySQLBuilder as sql

sql.translator = sql.TRANSLATOR_GENERIC
sql.bindingOption = sql.PARAM_NUM

builder = sql \
    .select('table') \
    .columnExpression("CONCAT_WS(?, `col1`, `col2`, `col3`)", 'cols', ['-']) \
    .column('col4') \
    .where('col1', '=', 'value1') \
    .whereExpression("UNIX_TIMESTAMP(`datetime`)%?", '=', 0, [3600])
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
