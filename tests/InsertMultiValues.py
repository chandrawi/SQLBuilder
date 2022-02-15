import BreakObject

import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)

import pySQLBuilder as sql

sql.translator = sql.TRANSLATOR_GENERIC
sql.binding = sql.PARAM_NUM

builder = sql \
    .insert('table') \
    .multiValues([
        {'col1': 'val_0_1', 'col2': 'val_0_2', 'col3': 'val_0_3'},
        {'col1': 'val_1_1', 'col2': 'val_1_2', 'col3': 'val_1_3'},
        {'col1': 'val_2_1', 'col2': 'val_2_2', 'col3': 'val_2_3'},
    ])
builderObject = builder.getBuilder()
builder.translate()
queryObject = builder.getQueryObject()

print("--------------\nBUILDER OBJECT\n--------------")
BreakObject.printInsertBuilder(builderObject)

print("------------\nQUERY OBJECT\n------------")
BreakObject.printQuery(queryObject)

print("-----\nQUERY\n-----")
print(builder.query())

print("------\nPARAMS\n------")
print(builder.params())
