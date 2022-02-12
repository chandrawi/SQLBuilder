import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)

from pySQLBuilder.QueryObject import QueryObject
from pySQLBuilder.Builder import SelectBuilder, InsertBuilder, UpdateBuilder, DeleteBuilder
from pySQLBuilder.Structure import Table, Column, Value, Clause, Order, Limit

def table(table: Table) -> tuple :
    return (table.name(), table.alias())

def column(column: Column) -> tuple :
    return (column.table(), column.name(), column.function(), column.alias())

def value(value: Value) -> tuple :
    pairs = ()
    for i in range(len(value.columns())) :
        pairs = pairs + (value.columns()[i], value.values()[i])
    return pairs

def clause(clause: Clause) -> tuple :
    col = column(clause.column())
    return (col, clause.operator(), clause.value(), clause.conjunctive(), clause.level())

def order(order: Order) -> tuple :
    col = column(order.column())
    return (col, order.orderType())

def limit(limit: Limit) -> tuple :
    return (limit.limit(), limit.offset())

def printTable(tableObject: Table) :
    tableBreak = table(tableObject)
    print("Table{}".format(tableBreak))

def printColumn(columnObject: Column, label = "Column") :
    columnBreak = column(columnObject)
    print("{0}{1}".format(label, columnBreak))

def printValue(valueObject: Value) :
    valueBreak = value(valueObject)
    print("Value{}".format(valueBreak))

def printClause(clauseObject: Clause, label = "Where") :
    clauseBreak = clause(clauseObject)
    print("{0}{1}".format(label, clauseBreak))

def printOrder(orderObject: Order) :
    orderBreak = order(orderObject)
    print("Order{}".format(orderBreak))

def printLimit(limitObject: Limit) :
    limitBreak = limit(limitObject)
    print("Limit{}".format(limitBreak))

def printSelectBuilder(selectBuilder: SelectBuilder) :
    print("Type: {}".format(selectBuilder.builderType()))
    printTable(selectBuilder.getTable())
    for col in selectBuilder.getColumns() :
        printColumn(col)
    for where in selectBuilder.getWhere() :
        printClause(where, "Where")
    for group in selectBuilder.getGroup() :
        printColumn(group, "Group")
    for where in selectBuilder.getHaving() :
        printClause(where, "Having")
    for order in selectBuilder.getOrder() :
        printOrder(order)
    if selectBuilder.hasLimit() :
        printLimit(selectBuilder.getLimit())

def printInsertBuilder(insertBuilder: InsertBuilder) :
    print("Type: {}".format(insertBuilder.builderType()))
    printTable(insertBuilder.getTable())
    for val in insertBuilder.getValues() :
        printValue(val)
    if insertBuilder.hasLimit() :
        printLimit(insertBuilder.getLimit())

def printUpdateBuilder(updateBuilder: UpdateBuilder) :
    print("Type: {}".format(updateBuilder.builderType()))
    printTable(updateBuilder.getTable())
    for val in updateBuilder.getValues() :
        printValue(val)
    for where in updateBuilder.getWhere() :
        printClause(where, "Where")
    if updateBuilder.hasLimit() :
        printLimit(updateBuilder.getLimit())

def printDeleteBuilder(deleteBuilder: DeleteBuilder) :
    print("Type: {}".format(deleteBuilder.builderType()))
    printTable(deleteBuilder.getTable())
    for where in deleteBuilder.getWhere() :
        printClause(where, "Where")
    if deleteBuilder.hasLimit() :
        printLimit(deleteBuilder.getLimit())

def query(query: QueryObject) -> tuple :
    queryParts = query.parts()
    queryParams = query.params()
    queryPair = ()
    for i in range(len(queryParts)) :
        param = None
        if len(queryParams) > i : param = queryParams[i]
        queryPair += ((queryParts[i], param),)
    return queryPair

def printQuery(queryObject: QueryObject) :
    pairs = query(queryObject)
    string = ""
    for pair in pairs :
        print("{}  ||  {}".format(pair[0], pair[1]))
