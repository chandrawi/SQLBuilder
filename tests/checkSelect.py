import BreakObject

import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)

from pySQLBuilder import QueryBuilder, QueryTranslator

builder = QueryBuilder() \
    .select({'data': 'data_table'}) \
    .column('UNIX_TIMESTAMP(ts)') \
    .columns({'alias1': 'col1', 'alias2': 'col2'}) \
    .columns(('col3', 'col4', 'col5')) \
    .where('col1', '>=', 0) \
        .beginAndWhere() \
        .where('col2', 'IN', ['value0', 'value1', 'value2']) \
        .orWhere('col3', 'BETWEEN', ['minValue', 'maxValue']) \
        .endWhere() \
    .groupBy('col1') \
    .having('col4', '=', 'havingValue') \
    .orderByAsc('col1') \
    .limit(100)
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
